from github import Github
from github import Auth
from github import GithubException
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
if not token:
    print("GITHUB_TOKEN not found in .env file.")
    exit(1)

auth = Auth.Token(token)
g = Github(auth=auth)

owner = input("Enter owner name: ").strip()
reponame =input("Enter repo name: ").strip()

try:
    repo = g.get_repo(f"{owner}/{reponame}")

    try:
        readme = repo.get_readme()
        content = readme.decoded_content.decode("utf-8")
        print(content)
    
    except GithubException as e:
        if e.status == 404:
            print("README not found in this repository.")
        else:
            print("Error fetching README:", e)
    
except GithubException as e:
    if e.status == 404:
        print("Repository not found. Check owner/repo name")
    elif e.status == 401:
        print("Authentication failed. Check your token.")
    elif e.status == 403:
        print("Access denied or rate limit exceeded.")
    else:
        print("Unexpected error:", e)