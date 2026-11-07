# InternHelp AI — Chatbot for Intern Queries

A deployable intern-support chatbot demo for assignment #3. It answers common questions about assignment guidelines, submission preparation, GitHub repositories, and troubleshooting.

## Features
- Responsive web chat interface with quick prompts
- FAQ knowledge-base matching and safe fallback responses
- Optional OpenAI-powered natural-language response layer
- Flask API: `POST /api/chat`, `GET /api/health`
- Vercel deployment configuration
- No intentional message persistence
- Clearly identifies itself as a demo, not official platform support

## Tech stack
Python, Flask, OpenAI API (optional), HTML, CSS, JavaScript, Vercel.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m flask --app api.index run --debug
```
Open http://127.0.0.1:5000.

## Environment variables
Copy `.env.example` to `.env` for local development and set your own key if you want AI mode. Never commit real credentials.

- `OPENAI_API_KEY` — optional OpenAI API key
- `OPENAI_MODEL` — optional model name; defaults to `gpt-4.1-mini`

Without a key, the app uses its local FAQ knowledge base. If the OpenAI request fails, it falls back to the FAQ response.

## API
- `GET /api/health` — service health check
- `POST /api/chat` — JSON body: `{"message":"How do I submit an assignment?"}`

## Knowledge-base limitation
The private Internee.pk knowledge base was not provided. Current answers use the assignment brief and general project guidance. Official policy questions (such as stipend, attendance, certificate rules, or deadlines) are explicitly referred to the platform's official portal/support. Add approved FAQ or policy documents before representing this as a complete company knowledge-base integration.

## Deployment
Configured for Vercel Python Functions using `vercel.json`. Set `OPENAI_API_KEY` in the Vercel project environment settings and redeploy to enable the optional OpenAI layer.

## Privacy and safety
Do not submit passwords, API keys, or confidential personal information. This application does not intentionally persist chat messages. It is an educational demo and is not affiliated with or endorsed by Internee.pk.

## License
MIT
