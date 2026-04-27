# Gemini ReAct File Agent

An autonomous AI agent built with Python and Google's Gemini 2.5 Flash. This agent doesn't just chat; it can interact with the local file system, execute code, and perform multi-step reasoning to solve complex tasks.

##  Overview

This project implements the **ReAct (Reasoning + Acting)** pattern. The agent uses **Function Calling** to bridge the gap between Large Language Models (LLMs) and local execution. It can browse directories, read file contents, create/update files, and run Python scripts to verify its work.

##  Key Features

- **Autonomous Tool Use**: The agent decides which tool to use based on the user's prompt.
- **ReAct Loop**: Implements a robust execution loop (up to 20 iterations) allowing the agent to think, act, observe results, and refine its approach.
- **File System Integration**: Custom-built tools for:
  - `get_files_info`: Directory listing and metadata.
  - `get_file_content`: Secure file reading with character limits.
  - `write_file`: Writing or overwriting local files.
  - `run_python_file`: Executing Python logic and capturing stdout/stderr.
- **Error Handling**: Comprehensive validation of API responses and tool execution results.

## 🛠️ Technical Stack

- **Language**: Python 3.12+
- **AI Model**: Google Gemini 2.5 Flash
- **Orchestration**: Google GenAI SDK
- **Environment Management**: `uv` (Fast Python package installer and resolver)
- **Configuration**: `python-dotenv` for secure API key management

## 📦 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [your-repo-link]
   cd first-agent

2. **Set up your environment variables:**
    **Create a `.env` file and add your Gemini API Key:**

    ```bash
    GEMINI_API_KEY=your_api_key_here

3. **Run the agent:**
    **Use the `uv` package manager to run the agent with a prompt:**

    ```bash
    uv run main.py "List the files in the current directory and summarize the content of main.py"

4. **Verbose Mode**
    **To see the agent's internal reasoning and function calls:**

    ```bash
    uv run main.py "your prompt" --verbose
    
--------------------------------------------------------------------------------------------------------------------------------------------

# What I Learned

Building this agent provided deep insights into:

- **API Schema Design**: Defining strict JSON schemas for LLM tool integration.

- **State Management**: Maintaining conversation context and tool results across multiple API calls.

- **Data Routing**: Implementing clean, dictionary-based function mapping for scalable tool integration.

- **Secure Execution**: Managing local file access and execution paths safely.


--------------------------------------------------------------------------------------------------------------------------------------------

*Developers note: This project was developed as part of the Boot.dev curriculum, focusing on AI Agents and advanced Python integration.*
*Developer: Jere Kukkohovi* -
*Date: April 28th, 2026*
