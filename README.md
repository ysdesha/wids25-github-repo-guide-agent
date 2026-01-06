# WIDS-25: GitHub Repository Guide Agent

# **WEEK 1: README Fetcher**

A Python script that uses the **GitHub REST API** (via PyGithub) to fetch and display the `README.md` file of any public GitHub repository.

---

## Features

* Connects to GitHub using a Personal Access Token (PAT)
* Accepts repository input in `owner/repo` format
* Fetches the `README.md` file from the repository
* Decodes and prints README content in the terminal
* Handles common API and runtime errors gracefully

---

## Setup Instructions

### 1️. Clone the repository

```bash
git clone https://github.com/ysdesha/wids25-github-repo-guide-agent.git
cd wids25-github-repo-guide-agent
```

### 2️. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3️. Install dependencies

```bash
pip install -r requirements.txt
```

---

## GitHub Token Setup

1. Go to **GitHub → Settings → Developer settings → Personal access tokens**
2. Generate a token with **repo (read-only)** access
3. Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_personal_access_token_here
```

>  **Never commit your `.env` file to GitHub**

---

## How to Run

```bash
python week1.py
```

You will be prompted to enter:

* Repository owner name
* Repository name

Example:

```text
Enter owner name: PyGithub
Enter repo name: PyGithub
```

The README content will be printed to the terminal.

---

## Error Handling

The script handles:

* Invalid repository names (404)
* Missing README files
* Authentication failures
* Permission or rate-limit errors

> User-friendly messages are displayed instead of raw errors.

---

# **WEEK 2: AI Summarizer**

This project implements an AI-powered GitHub README summarizer using a Large Language Model (Google Gemini).  
It extends basic API usage into intelligent understanding and summarization of repository documentation.

The script fetches a repository’s `README.md`, sends it to Gemini, and generates a structured, human-readable summary in the terminal.

---

##  Features

- **Fetches README.md content** from any public GitHub repository.
- **Summarizes repository documentation** using the **Gemini 2.5 Flash LLM**.
- **Generates concise, structured summaries** highlighting:
  - What the project does
  - Its main purpose
  - Key features or components
  - Intended users or use cases
- **Handles common API and runtime errors gracefully.**

---

##  Gemini API Setup

- Generate an API key from Google AI Studio
- Add the key to your `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```
>  Do not share your API key publicly

---
##  How to Run

Run the script using:

```bash
python week2.py
```

You will be prompted to enter:

* Repository owner name
* Repository name

Example:

```text
Enter owner name: PyGithub
Enter repo name: PyGithub
```

The script will fetch the README and display the AI-generated summary in the terminal.

## Error Handling

The script handles:

- **Invalid repository names (404)**
- **Missing README.md file**
- **GitHub authentication failures (401)**
- **Permission or rate-limit errors (403)**
- **Unexpected errors or low-quality AI responses**

User-friendly messages are displayed instead of raw errors.

## Learning outcomes

Through this project across Week 1 and Week 2, I learned how to design a small but complete system that combines traditional APIs with AI-based reasoning.

### API & Platform Interaction
- **API Fundamentals:** Understood how APIs enable communication between applications and external platforms like GitHub.
- **Tools:** Gained hands-on experience using the **GitHub REST API** via PyGithub to access repositories and files.
- **Security:** Learned how authentication using **Personal Access Tokens** works and why environment variables are used to store secrets.
- **Robustness:** Learned to handle real-world API errors such as invalid repositories, missing files, authentication failures, and rate limits.

### Introduction to Large Language Models (LLMs)
- **Concepts:** Gained a conceptual understanding of what Large Language Models are and how they process text.
- **Effectiveness:** Learned why LLMs are effective for summarization tasks compared to rule-based approaches.
- **Constraints:** Understood limitations such as context size, probabilistic outputs, and the need for careful input selection.

### Prompt Engineering & AI Integration
- **Structure:** Learned how to design clear and structured prompts to guide an LLM’s behavior.
- **Refinement:** Practiced defining the model’s role, expected output, and level of detail.
- **Integration:** Integrated an LLM (**Gemini**) as a logical “AI brain” that processes retrieved data rather than as a standalone tool.

### End-to-End System Thinking
- **Pipeline Design:** Learned how to build an AI-driven pipeline that:
  - Fetches data from an external API
  - Processes it using an LLM
  - Produces a human-readable, structured output
-  Understood how traditional APIs and AI services can be combined to create intelligent tools.
