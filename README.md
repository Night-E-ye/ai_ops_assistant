# AI Operations Assistant 🤖

## Overview
A local, multi-agent AI system built for the GenAI Intern assignment. It accepts natural language tasks, plans execution steps, integrates with real APIs (GitHub & DuckDuckGo), and verifies results using Google Gemini.

## Architecture 🏗️
The system follows a Planner-Executor-Verifier architecture:
1.  **Planner Agent:** Uses LLM to break complex user requests into a structured JSON plan.
2.  **Executor Agent:** Iterates through the plan, dynamically calling the appropriate tools (GitHub Search, Web Search).
3.  **Verifier Agent:** Synthesizes the raw tool outputs into a final, human-readable summary.

## integrated APIs 🔌
1.  **GitHub API:** For searching repositories and code metadata.
2.  **DuckDuckGo Search:** For real-time web information.
3.  **Google Gemini:** As the core LLM reasoning engine.

## Setup Instructions ⚙️

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-link>
    cd ai_ops_assistant
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Setup:**
    - Rename `.env.example` to `.env`
    - Add your API Key: `GEMINI_API_KEY=AIzaSy...`

4.  **Run the application:**
    ```bash
    streamlit run main.py
    ```

## Example Prompts to Test 🧪
1.  "Find top 3 React libraries on GitHub."
2.  "Search for the latest news on 'OpenAI' using web search."
3.  "Find Python libraries for 'Machine Learning' on GitHub."

## Limitations
- The system currently supports sequential execution (not parallel).
- GitHub search is limited to the top 3 results to ensure speed.