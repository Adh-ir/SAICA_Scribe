# SAICA Scribe 🤖

**AI-Powered Competency Documentation Assistant for SAICA Trainees.**

Developed by **[Adhir Singh](https://github.com/Adh-ir)**.

SAICA Scribe helps you map your daily audit activities to the SAICA Competency Framework (2025 Training Plan) using advanced AI (Google Gemini 1.5 Pro/Flash or Groq Llama 3).

## 🚀 Features

*   **Smart Mapping**: Analyzes your input and matches it against the *entire* SAICA 2025 Training Plan.
*   **Multi-Model Support**:
    *   **Google Gemini 2.0 Flash Exp** (Default, High Intelligence).
    *   **GitHub Models (GPT-4o / Mini)** (Strict, Precise).
    *   **Groq (Llama 3)** (Lightning Fast).
*   **Auto-Setup**: Python and dependencies are installed automatically. Just click and run.
*   **Privacy First (BYOK)**: Bring Your Own Key. Your API keys are stored locally on your machine (`.env`) and never shared.
*   **Strict Filtering**: Target a specific competency code (e.g. `COMPETENCY: 1a`) and the system guarantees a single, focused result.

## 🛠️ Quick Start

### Prerequisites
*   None! (The launcher handles everything).

### Installation & Run

1.  **Download** this repository (Code -> Download ZIP) and extract it.
2.  **Double-click the Launcher**:

    *   🍎 **Mac User?**
        Double-click `Run_SAICA_Scribe.command`.
        *(Note: First time might require Right-Click -> Open if MacOS warns about developers)*

    *   🪟 **Windows User?**
        Double-click `Run_SAICA_Scribe.bat`.

    *The launcher will automatically download Python if you don't have it, set up the environment, and launch the app.*

3.  The application will open in your browser at `http://localhost:8000`.

### First Time Setup
The app will guide you through a one-time setup wizard:
1.  Choose your AI provider (Gemini 2.0 or GitHub Models recommended).
2.  Follow the **"Get Key"** links to grab your free API key.
3.  Paste the key into the app, and you are ready to go!

## 💡 Usage Tips
*   **Be Specific**: Mention the *Client*, *Task*, and *Outcome* in your activity.
*   **Targeting**:
    *   **Broad Search**: Just type your activity. The AI finds all relevant matches.
    *   **Specific Target**: Type `COMPETENCY: [Code or Name] EVIDENCE: [Desc]` to force a specific mapping.
    *   *Example*: `COMPETENCY: 1a EVIDENCE: I reconciled the bank statement...` (This guarantees ONLY competency 1a is returned).

---
*Made with ❤️ by [Adhir Singh](https://github.com/Adh-ir)*
