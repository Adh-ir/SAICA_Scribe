# CA Scribe 🤖

**AI-Powered Competency Documentation Assistant for SAICA Trainees.**

*Formerly known as SAICA Scribe.*

Developed by **[Adhir Singh](https://github.com/Adh-ir)**.

CA Scribe helps you map your daily audit activities to the SAICA Competency Framework (2025 Training Plan) using advanced AI models. Now featuring a fully immersive, animated interface and cloud accessibility.

## 🌐 Try It Now (No Install Required)

**[Launch CA Scribe →](https://ca-scribe.streamlit.app)**
*(Hosted on Streamlit Cloud)*

> **⚠️ Note:** CA Scribe is a "Bring Your Own Key" application. For your security, keys are only held in your active session. **If you refresh the browser, your session will reset, and you will need to re-enter your API key.**

## 🚀 Features

* **☁️ Instant Access**: No installation needed. Run directly in your browser via Streamlit Cloud.
* **✨ Immersive UI**: A completely redesigned user experience featuring enhanced animations, loading states, and a polished Light Mode interface.
* **🧠 Smart Mapping**: Analyzes your input and matches it against the *entire* SAICA 2025 Training Plan.
* **🤖 Multi-Model Support**:
    * **Google Gemini 2.0 Flash Exp** (Default, High Intelligence).
    * **GitHub Models (GPT-4o / Mini)** (Strict, Precise).
    * **Groq (Llama 3)** (Lightning Fast).
* **🔒 Privacy First**: Your API keys are never stored on a server.
* **🎯 Strict Filtering**: Target a specific competency code (e.g., `COMPETENCY: 1a`) for focused results.

## 🔑 Getting Started

1.  **Open the App**: [Click here to visit CA Scribe](https://ca-scribe.streamlit.app).
2.  **Get an API Key** (free): Follow the in-app guide to get a key from:
    * [Google AI Studio](https://aistudio.google.com/app/apikey) (Recommended)
    * [Groq Console](https://console.groq.com/keys) (Fastest)
    * [GitHub Tokens](https://github.com/settings/tokens) (GPT-4o)
3.  **Paste your key** in the setup wizard and start mapping!

## 💡 Usage Tips

* **Be Specific**: Mention the *Client*, *Task*, and *Outcome* in your activity.
* **Targeting**:
    * **Broad Search**: Just type your activity. The AI finds all relevant matches.
    * **Specific Target**: Click "Target Competency" and fill in the template.
    * *Example*: `COMPETENCY: 1a EVIDENCE: I reconciled the bank statement...` (This guarantees ONLY competency 1a is returned).

## 🛠️ Local Development

If you prefer to run CA Scribe locally:

```bash
# Clone the repository
git clone [https://github.com/Adh-ir/CA_Scribe.git](https://github.com/Adh-ir/CA_Scribe.git)
cd CA_Scribe/code

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# or: .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

The app will open at `http://localhost:8501`.

## 🐳 Docker Deployment

Run CA Scribe in a Docker container for production or isolated development. This ensures cross-platform compatibility (Windows, Mac, Linux).

```bash
# Quick start with Docker Compose
docker compose up -d

# Or build and run manually
docker build -t ca-scribe .
docker run -p 8501:8501 ca-scribe
```

The containerized app runs at `http://localhost:8501`.

### Container Features
- **Multi-stage build** for optimized image size (~400MB)
- **Health checks** for orchestration compatibility
- **Volume mount** for persisting output files
- **Production-ready** configuration

## 📁 Project Structure

```
CA_Scribe/
├── code/
│   ├── streamlit_app.py      # Main Streamlit application
│   ├── config.py             # Configuration settings
│   ├── requirements.txt      # Python dependencies
│   ├── analysis/             # AI mapping logic
│   ├── ingestion/            # Framework data loading
│   ├── reporting/            # Report generation
│   ├── utils/                # Styles and templates
│   └── templates/            # HTML templates (guide)
├── .streamlit/               # Streamlit configuration
├── Dockerfile                # Container build configuration
├── docker-compose.yml        # Docker Compose orchestration
├── .dockerignore             # Files excluded from container
└── README.md
```

---
*Made by [Adhir Singh](https://github.com/Adh-ir)*
