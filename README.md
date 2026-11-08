# InternHelp AI — Chatbot for Intern Queries

An intern-support chatbot demo for assignment #3. It answers common questions about assignment guidelines, submission preparation, GitHub repositories, and technical troubleshooting.

## Features
- Responsive chat interface with quick prompts.
- Context-aware AI responses grounded in an approved demo FAQ.
- Safe fallback knowledge-base responses when the AI provider is unavailable.
- Explicit handling of unknown official policies; it does not invent stipend, deadline, attendance, eligibility, or certificate rules.
- Flask API and Vercel deployment configuration.

## Stack
Python, Flask, Vireonix Chat Completions API, HTML, CSS, JavaScript, Vercel.

## AI provider
Uses Vireonix's OpenAI-compatible `POST /v1/chat/completions` endpoint with `model: "auto"`, no API key or Authorization header. The free public API is subject to per-IP hourly budgets and may return HTTP 429 or become temporarily unavailable. Fallback answers are labelled as knowledge-base responses.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python -m flask --app api.index run --debug
```
Open http://127.0.0.1:5000.

No provider API key is required.

## API
- `GET /api/health` — health metadata.
- `POST /api/chat` — JSON body: `{"message":"How do I prepare a strong README?"}`.

## Knowledge-base limitation
The private Internee.pk knowledge base was not supplied. The demo uses the assignment brief and general project guidance. Questions about official policies or account-specific matters are directed to the portal/support. It is not official Internee.pk support and cannot submit work to an account.

## Privacy and safety
Chat messages are sent to Vireonix and may be retained and used for model training and improvement. The interface discloses this and links to https://vireonix.ai/terms. Do not submit passwords, API keys, sensitive personal data, or confidential information. The app does not intentionally persist chat messages.
