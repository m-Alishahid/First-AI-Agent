# 🤖 Agentic AI — Python-Based AI Agent Using Gemini API & UV

This is my first ever Agentic AI project — a foundational step into the world of intelligent automation. Built using Python, the Gemini API from Google, and managed with the ultra-fast UV package manager, this project is a minimal yet functional AI agent that takes your prompt, connects to the Gemini LLM, and returns a meaningful response. While it's not a full conversational agent yet, it lays the groundwork for future intelligent behavior.

## 🧠 What it Does

This is a **single-turn agent**, meaning:

- It does **not** maintain a conversation or memory.
- You give it **one input**.
- It sends that input to **Gemini API** using the `Runner.run_sync()` method.
- It returns **only one response**, and the session ends there.

Great for testing ideas or triggering fast single-responses from LLMs for static instructions.

## ⚙️ How to Set It Up

```bash
# Step 1: Clone the repository
git clone https://github.com/your-username/agentic-ai.git
cd agentic-ai

# Step 2: Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\activate  # For Windows

# Step 3: Install dependencies using uv (if installed)
uv pip install -r requirements.txt

# OR install manually via pip if needed
pip install -r requirements.txt

# Step 4: Set your Gemini API key (required)
set GEMINI_API_KEY=your_api_key_here  # Windows
# export GEMINI_API_KEY=your_api_key_here  # Linux/macOS

# Step 5: Run the agent
uv run main.py
📦 Technologies Used
Python

UVI (Rust-based fast package/dependency manager)

Gemini API (Google Generative AI)

dotenv (optional for storing API key)

📁 Project Structure
main.py – Core logic of the agent

requirements.txt – Python dependencies

.venv/ – Virtual environment (excluded in repo)

README.md – You're reading it :)

📍 Example Output
text
Copy
Edit
Calling
Hello! As a large language model, I don’t experience feelings, but I’m here to assist you!
📌 Notes
This agent is not fully conversational yet, but it provides a base to build upon.

More advanced features like memory, tools, and multiple steps can be added later.

Ideal for those beginning to explore LLMs, API usage, and agent architecture.

📜 License
Open-source under the MIT License

🚀 Built with passion as part of my Agentic AI learning journey.
📸 Instagram: @codecraftali
