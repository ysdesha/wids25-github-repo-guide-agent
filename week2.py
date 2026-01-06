
from github import Github
from github import Auth
from github import GithubException
import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
github_token = os.getenv("GITHUB_TOKEN")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not github_token:
    print("GITHUB_TOKEN not found in .env file.")
    exit(1)

if not gemini_api_key:
    print("GEMINI_API_KEY not found in .env file.")
    exit(1)


auth = Auth.Token(github_token)
github_client = Github(auth=auth)

gemini_client =  genai.Client(api_key=gemini_api_key)

def fetch_readme(owner: str, repo_name: str) -> str:
    """
    Fetch README.md content from a GitHub repository.
    Returns decoded UTF-8 text.
    """
    try:
        repo = github_client.get_repo(f"{owner}/{repo_name}")

    except GithubException as e:
        if e.status == 404:
            raise ValueError("Repository not found. Check owner/repo name.") from e
        elif e.status == 401:
            raise PermissionError("GitHub authentication failed.") from e
        elif e.status == 403:
            raise PermissionError("Access denied or rate limit exceeded.") from e
        else:
            raise e
        
    try:
        readme = repo.get_readme()
        content = readme.decoded_content.decode("utf-8")
        return content
        
    except GithubException as e:
        if e.status == 404:
            raise FileNotFoundError("README.md not found in this repository.") from e
        else:
            raise e
        
    
def summarize_readme(readme_text: str) -> str:
    prompt = f"""
    
    You are an AI assistant that summarizes GitHub repositories.

    Given the README content below:
    - Explain what the project does
    - Identify its main purpose
    - List key features or components
    - Mention intended users or use cases

    Keep the summary concise and structured.
    Use bullet points where appropriate.

    README:
   {readme_text[:12000]}
    """
    
    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

def main():
    
    owner = input("Enter owner name: ").strip()
    repo_name =input("Enter repo name: ").strip()

    try:
        print("\n Fetching README...\n")
        readme_text = fetch_readme(owner, repo_name)

        summary = summarize_readme(readme_text)
        print("Summary:\n")
        print(summary)

    except ValueError as e:
        print(f" {e}")
    except FileNotFoundError as e:
        print(f" {e}")
    except PermissionError as e:
        print(f" {e}")
    except GithubException as e:
        print(f" GitHub error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")

if __name__ == "__main__":
    main()