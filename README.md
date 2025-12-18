# WIDS-25 - GitHub Repository Guide Agent

## WEEK-1

A Python script that uses the **GitHub REST API** (via PyGithub) to fetch and display the `README.md` file of any public GitHub repository.

---

# Features

* Connects to GitHub using a Personal Access Token (PAT)
* Accepts repository input in `owner/repo` format
* Fetches the `README.md` file from the repository
* Decodes and prints README content in the terminal
* Handles common API and runtime errors gracefully

---

## Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ysdesha/wids25-github-repo-guide-agent.git
cd wids25-github-repo-guide-agent
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## GitHub Token Setup

1. Go to **GitHub → Settings → Developer settings → Personal access tokens**
2. Generate a token with **repo (read-only)** access
3. Create a `.env` file in the project root:

```
GITHUB_TOKEN=your_personal_access_token_here
```

 **Never commit your ****************************************`.env`**************************************** file**

---

##  How to Run

```bash
python week1.py
```

You will be prompted to enter:

* Repository owner name
* Repository name

Example:

```
Enter owner name: torvalds
Enter repo name: linux
```

The README content will be printed to the terminal.

---

##  Error Handling

The script handles:

* Invalid repository names (404)
* Missing README files
* Authentication failures
* Permission or rate-limit errors

User-friendly messages are displayed instead of raw errors.

---

