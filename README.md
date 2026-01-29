# WIDS-25: GitHub Repository Guide Agent

# **Week 1: README Fetcher**

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

# **Week 2: AI Summarizer**

This project implements an AI-powered GitHub README summarizer using a Large Language Model (Google Gemini).  
It extends basic API usage into intelligent understanding and summarization of repository documentation.

The script fetches a repository’s `README.md`, sends it to Large Language Model, and generates a structured, human-readable summary in the terminal.

---

## Features

- **Fetches README.md content** from any public GitHub repository
- **Prepares and truncates text** for LLM input
- **Sends the content to LLM** with a structured prompt
- **Summarizes repository documentation** using the **Gemini 2.5 Flash LLM**
- **Generates concise, structured summaries** highlighting:
  - What the project does
  - Its main purpose
  - Key features or components
  - Intended users or use cases
- **Handles common API and runtime errors gracefully**

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


  
---

# ** Week 3 — GitHub Repository Analysis Agent**

### Overview

In Week 3, we built a Python-based AI agent that analyzes public GitHub repositories and generates a structured developer onboarding guide. The agent processes repository documentation and structure to help new developers quickly understand a codebase.

### What the Agent Does

- Fetches a public GitHub repository using the GitHub API
- Reads and processes the README file
- Analyzes the repository file structure
- Identifies important files in the codebase
- Uses an LLM (Gemini) to generate a structured developer guide

### Generated Developer Guide Includes

- What the project does
- How the codebase is organized
- Important files and their roles
- A logical onboarding path for new developers
---




# Week 4 — Streamlit Web App

## Overview
In Week 4, we turned the Week 3 agent into a polished, demo-ready web application using **Streamlit**. The app allows users to:

* **Input** any public GitHub repository (owner/repo format).
* **Run** the AI agent pipeline on button click.
* **Display** the generated developer guide in a clean, interactive, and responsive UI.

---

## Features
* **Interactive UI:** Sidebar for repository input, buttons for "Generate" and "Reset".
* **Clean Dark Theme:** Styled with custom CSS for a GitHub-inspired look.
* **Guide Display:** Full markdown rendering with code blocks and expandable sections.
* **Session State:** Maintains repository input and generated guide for smooth UX.
* **Error Handling:** Alerts users when repository is invalid or README is missing.
* **Responsive Layout:** Wide layout, fully optimized for demo and portfolio showcasing.

---

## Running the App

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run week4.py
```
## Example Workflow
1. **Open the sidebar** and enter the repository owner and repository name.
2. **Click Generate** to fetch repository data and generate a guided developer tour.
3. **View the generated guide** in the main content area under "View Full Guide".
4. **Use the Reset button** to clear inputs and generate a new guide for a different repository.

## Tech Stack
* **Python 3.x**
* **PyGithub**: For GitHub API interaction
* **Gemini API**: For AI-generated content
* **Streamlit**: For building the interactive web interface
* **Custom CSS**: For styling the dark, clean UI

## Project Structure
```text
.
├── week3.py            # Core GitHub + AI logic
├── week4.py            # Streamlit web app
├── requirements.txt    # Python dependencies
├── .env                # API keys (GitHub, Gemini)
└── README.md           # Project documentation
```
## Future Enhancements

* **Repository Tree Preview:** Add a file tree visualization for quick and easy file browsing.
* **Guide Toggle:** Include an option to switch between a **Short** summary and a **Detailed** comprehensive guide.
* **Polished UI:** Improve overall styling and UX by implementing more advanced UI components.
* **Private Repository Support:** Add functionality for private repositories via GitHub token authentication.

# Overall Outcomes & Learnings

This project successfully transformed an AI concept into a complete, demo-ready application through a structured, multi-week development process.

### Technical Outcomes
- Built an AI agent capable of understanding GitHub repositories using README analysis and repository structure inspection.
- Designed a modular pipeline separating data collection, reasoning, and presentation layers.
- Integrated GitHub APIs and large language models to generate structured developer onboarding guides.
- Developed a clean, interactive Streamlit web application to showcase the AI agent.
- Implemented state management, loading indicators, and graceful error handling for a professional user experience.
- Applied custom CSS to create a polished, developer-friendly UI suitable for demos and portfolios.

### Key Learnings
- How to analyze real-world codebases programmatically using GitHub APIs.
- Effective prompt engineering for technical documentation and onboarding tasks.
- Importance of separating core logic from UI when building AI products.
- Practical experience in productizing AI agents into usable applications.
- UX design principles for developer-focused tools.
- Managing environment variables and API keys securely.
- Turning experimental AI scripts into structured, maintainable software projects.

### Project Impact
- The final system demonstrates how AI can significantly reduce onboarding time for new developers.
- The application is fully demo-ready and suitable for portfolio presentation or further extension.
- The project bridges the gap between AI experimentation and real-world product development.

### Final Reflection
This project strengthened both AI engineering and software development skills, emphasizing not just *building intelligence*, but also *delivering usable, polished AI products*.

