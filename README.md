# InternHelp AI — Chatbot for Intern Queries

An intern-support chatbot demo for assignment #3. It answers common questions about assignment guidelines, submission preparation, GitHub repositories, and technical troubleshooting.

## Features
- Responsive chat interface with quick prompts.
- AI responses grounded in an approved demo FAQ.
- Safe fallback knowledge-base responses when live AI inference is unavailable.
- Explicit handling of unknown official policies; it does not invent stipend, deadline, attendance, eligibility, or certificate rules.
- Flask API and Vercel deployment configuration.

## Stack
Python, Flask, BlockRun Chat Completions API, HTML, CSS, JavaScript, Vercel.

## AI provider
Uses BlockRun's OpenAI-compatible `POST /api/v1/chat/completions` endpoint with free model `nvidia/nemotron-3.5-bolt` and fallback `poolside/laguna-xs-2.1`; no API key, wallet, payment card, or account is needed. Free-model capacity and IP rate limits can change. Fallback answers are labelled as knowledge-base responses.

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
Messages are routed through BlockRun to the selected model provider. BlockRun states that it does not store or train on prompts; upstream provider terms apply. Read [BlockRun Privacy](https://blockrun.ai/privacy) and [Terms](https://blockrun.ai/terms). Do not submit passwords, API keys, sensitive personal data, or confidential information. The app does not intentionally persist chat messages.
