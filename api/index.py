import os
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024

FAQ = [
    (["submit", "submission", "turn in", "upload"], "To submit an assignment, open the relevant task in your internship Task Portal, read its guidelines, choose Submit Task, and follow the portal's submission flow. Include the requested project links and verify that the portal displays a submitted status. This demo cannot submit work to your account."),
    (["chatbot assignment", "assignment 3", "intern queries"], "Assignment #3 asks you to create a 24/7 GenAI chatbot for intern questions about tasks and policies. Required capabilities: natural-language understanding, FAQs, task guidelines, and connection to Internee.pk's knowledge base. Suggested tools include Rasa, Dialogflow, OpenAI API, and Flask. The private company knowledge base was not supplied for this demo."),
    (["deliverable", "project requirements", "what should", "features"], "A strong submission should include a working web chat UI; FAQ and task-guideline coverage; clear fallback for unknown questions; source/knowledge-base grounding; safe handling of secrets; setup instructions; and a public demo plus GitHub repository. Explain any limits honestly."),
    (["technical issue", "error", "bug", "not working"], "For a technical issue: capture the exact error, note the steps that reproduce it, check browser console and server logs, verify environment variables are configured on the hosting platform, and test the health endpoint. Never share passwords or API keys in chat."),
    (["github", "readme", "repository", "repo"], "A good GitHub repository should contain a clear README (purpose, features, stack, setup, environment variables, API endpoints, limitations), dependency files, an example environment file with placeholders only, and a license. Never commit real secrets."),
    (["policy", "attendance", "stipend", "certificate", "deadline", "duration"], "I don't have access to Internee.pk's private policy documents, so I can't confirm official rules about attendance, stipends, certificates, deadlines, or eligibility. Check the current portal guidelines or contact the platform's official support team."),
    (["task", "guideline", "assignment"], "Open the assignment's Guidelines section and translate each requirement into a checklist. Build and test the smallest working version first, document the stack and limitations, deploy it, then submit the repository and live-demo links if requested."),
    (["hello", "hi", "hey"], "Hello! Ask me about assignment requirements, project structure, GitHub, deployment, or troubleshooting.")
]

def local_answer(message):
    q = message.lower()
    for terms, answer in FAQ:
        if any(term in q for term in terms):
            return answer
    return ("I don't have a verified answer for that yet. I can help with assignment instructions, project deliverables, GitHub preparation, and general troubleshooting. For official Internee.pk policies or account-specific issues, check the portal or official support. Try asking one focused question.")

@app.get("/")
def home():
    return send_from_directory(os.path.dirname(__file__), "index.html")

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "internhelp-ai"})

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()[:1200]
    if not message:
        return jsonify({"error": "Please enter a question."}), 400

    answer = local_answer(message)
    mode = "knowledge_base"
    key = os.getenv("OPENAI_API_KEY")
    if key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=key)
            response = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                temperature=0.2,
                messages=[
                    {"role": "system", "content": "You are InternHelp AI, an assistant for interns. Answer only from the supplied knowledge. The supplied knowledge is: " + "\n".join(a for _, a in FAQ) + "\nThe assignment brief: create a 24/7 intern FAQ chatbot with natural-language understanding, Internee.pk knowledge-base connection, FAQs and task guidelines; suggested tools Rasa, Dialogflow, OpenAI API, Flask. Never invent private company policies. If unknown, say so and direct the user to official portal/support. Never ask for secrets."},
                    {"role": "user", "content": message}
                ]
            )
            answer = response.choices[0].message.content or answer
            mode = "ai"
        except Exception:
            pass
    return jsonify({"answer": answer, "mode": mode})

@app.errorhandler(413)
def too_large(_):
    return jsonify({"error": "Request too large."}), 413
