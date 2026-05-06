# 🌍 Linguistic Analysis & Translation System

A sophisticated, enterprise-grade translation tool built with **Python** and **Gradio**. This system leverages neural machine translation and high-fidelity speech synthesis to provide a seamless multilingual experience.

## 🚀 Live Demo
**[View the Live Application on Hugging Face Spaces](https://huggingface.co/spaces/mubashrawaqar123/languageTranslator)**

## 🛠️ Tech Stack
*   **Interface:** Gradio
*   **Translation Engine:** Google Neural Machine Translation (via deep-translator)
*   **Primary Audio Synthesis:** Google Text-to-Speech (gTTS)
*   **Failover Audio Synthesis:** Microsoft Edge Neural TTS

## 🧠 Technical Highlight: Invisible Failover Logic
To ensure 100% uptime and bypass common rate-limiting issues associated with public API endpoints (such as `HTTP 429: Too Many Requests`), this system implements a **Redundant Failover Architecture**.

### How it works:
1.  The system first attempts to synthesize audio using the primary **gTTS** engine.
2.  If the primary engine fails due to network congestion or API throttling, the backend silently catches the exception.
3.  The system immediately triggers the secondary **Microsoft Edge Neural TTS** engine.
4.  The user receives their translated audio without ever seeing an error message or experiencing a service interruption.

## 📂 Project Structure
*   `app.py`: Core logic including the asynchronous processing and failover handling.
*   `requirements.txt`: Necessary dependencies for local and cloud deployment.

## 🔧 Local Setup
1. Clone the repository: `git clone https://github.com/YOUR_USERNAME/Linguistic-Processor-Pro.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`

---
*Developed as a demonstration of robust API integration and resilient backend architecture.*
