from github import Github, Auth, GithubException
import os
from dotenv import load_dotenv
from google import genai

# ------------------ Setup ------------------

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not github_token:
    raise RuntimeError("GITHUB_TOKEN not found in .env file.")

if not gemini_api_key:
    raise RuntimeError("GEMINI_API_KEY not found in .env file.")

github_client = Github(auth=Auth.Token(github_token))
gemini_client = genai.Client(api_key=gemini_api_key)

# ------------------ GitHub Utilities ------------------

def get_repo(owner: str, repo_name: str):
    try:
        return github_client.get_repo(f"{owner}/{repo_name}")
    except GithubException as e:
        if e.status == 404:
            raise ValueError("Repository not found.")
        elif e.status == 401:
            raise PermissionError("GitHub authentication failed.")
        elif e.status == 403:
            raise PermissionError("Access denied or rate limit exceeded.")
        else:
            raise


def fetch_readme(repo) -> str:
    try:
        readme = repo.get_readme()
        return readme.decoded_content.decode("utf-8")
    except GithubException as e:
        if e.status == 404:
            raise FileNotFoundError("README.md not found.")
        else:
            raise


def fetch_repo_tree(repo):
    try:
        branch = repo.default_branch
        tree = repo.get_git_tree(branch, recursive=True)
        return tree.tree
    except GithubException as e:
        raise RuntimeError("Failed to fetch repository structure.") from e

# ------------------ Tree Processing ------------------

IGNORE_DIRS = (
    "node_modules",
    ".venv",
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
)

IMPORTANT_FILES = (
    "README.md",
    "requirements.txt",
    "pyproject.toml",
    "package.json",
    "Dockerfile",
    "docker-compose.yml",
    "main.py",
    "app.py",
    "server.py",
)

def filter_tree(tree_items, max_depth=3):
    files = []

    for item in tree_items:
        if item.type != "blob":
            continue
        if item.path.startswith(IGNORE_DIRS):
            continue

        depth = item.path.count("/")
        if depth > max_depth:
            continue

        files.append(item.path)

    return files


def extract_important_files(files):
    important = []
    for f in files:
        for key in IMPORTANT_FILES:
            if f.endswith(key):
                important.append(f)
    return important

# ------------------ LLM Agent ------------------

MAX_README_CHARS = 8000

def generate_guided_tour(readme_text: str, important_files: list) -> str:
    if not important_files:
        important_files = ["No high-signal files detected."]

    prompt = f"""

You are a senior software engineer onboarding a new developer.

You are given:
1. README content
2. Key repository files

Your task:
- Explain what the project does
- Describe how the codebase is organized
- Identify important files and their roles
- Suggest a logical onboarding path

Produce a structured developer guide.

README:
{readme_text[:MAX_README_CHARS]}

Important Files:
{chr(10).join(important_files)}
"""

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

# ------------------ Entry Point ------------------

def main():
    owner = input("Enter owner name: ").strip()
    repo_name = input("Enter repo name: ").strip()

    try:
        print("\nFetching repository...")
        repo = get_repo(owner, repo_name)

        print("Fetching README...")
        readme_text = fetch_readme(repo)

        print("Fetching repository structure...")
        tree_items = fetch_repo_tree(repo)

        files = filter_tree(tree_items)
        important_files = extract_important_files(files)

        print("\nGenerating guided developer tour...\n")
        guide = generate_guided_tour(readme_text, important_files)
        print(guide)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
