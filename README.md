# 🧠 Chatbot App with Authentication (Next.js + FastAPI)

This is a full-stack chatbot application powered by a FastAPI backend and a React (Next.js) frontend. It includes user authentication (Signup & Login) using JWT, and a chat interface styled with Tailwind CSS.

---

## ✨ Features

- 🔐 User Signup & Login (JWT-based auth)
- 🤖 Chat interface to talk with a bot
- 🧠 Backend AI response powered by Hugging Face models
- 🎨 Clean UI using Tailwind CSS
- 🚀 Full-stack project using FastAPI (Python) and Next.js (React)

---

## 📁 Project Structure

chatbot-app/ 
├── backend/ 
    # FastAPI App │ 
        ├── main.py 
            # API routes: 
                /signup, 
                /token, 
                /chat │ 
    └── requirements.txt 
        # Python dependencies 
            ├── frontend/ # Next.js App │ 
            ├── app/ │ │ 
                ├── login
                    /page.js │ │ 
                ├── signup
                    /page.js │ │ 
                ├── chat
                    /page.js │ │ 
                └── layout.js │ 
                └── tailwind.config.js 
                # Tailwind CSS Config 
                ├── README.md



---

## 🚀 Getting Started

### 🔧 Prerequisites

- Node.js (v18+)
- Python 3.9+
- pip

---

## 💡 Setup Instructions

### 1️⃣ Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload


📝 backend/requirements.txt
fastapi
uvicorn
python-jose
passlib[bcrypt]

FastAPI will start at: http://127.0.0.1:8000

###2️⃣ Frontend (Next.js + Tailwind CSS)
cd frontend
npm install
npm run dev

Next.js will start at: http://localhost:3000

🔐 Authentication Flow

✅ POST /signup – Create a user with username/password

✅ POST /token – Login to receive a JWT token

✅ Store token in localStorage

✅ Chat API uses Authorization: Bearer <token> header


💬 Chat Flow
User types a message in the chat box

Frontend sends POST /chat with Authorization header

FastAPI responds with generated text from the model

🛡️ Tech Stack
Frontend	Backend	Auth	AI / NLP
Next.js	FastAPI	JWT	HuggingFace + Transformers
React	Python	OAuth2	DistilGPT2 / DialoGPT
Tailwind	Uvicorn	bcrypt	Custom Prompts


🤝 Contributing
Feel free to fork this repo, improve it, and make a PR! You can add:

Chat history with DB

Better prompt tuning

Support for OpenAI API

📜 License
MIT License — Free to use for personal and commercial projects

🙌 Author
Made with 💙 by Shadab Ahmed



---

Let me know if you'd like a full **GitHub repo template** for this or a downloadable ZIP!
