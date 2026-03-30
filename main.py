# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from llm import ask_llm

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/ask")
# async def ask_question(data: dict):
#     question = data.get("question")
#     answer = ask_llm(question)

#     return {"answer": answer}


# upgrade

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from llm import ask_llm
# from database import SessionLocal, Chat

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/ask")
# async def ask_question(data: dict):
#     question = data.get("question")

#     # Get previous context (all chats)
#     db = SessionLocal()
#     previous_chats = db.query(Chat).all()
#     context = "\n".join([f"Q: {c.question}\nA: {c.answer}" for c in previous_chats])

#     # Combine context + new question
#     prompt = f"{context}\nQ: {question}"

#     answer = ask_llm(prompt)

#     # Save to DB
#     chat = Chat(question=question, answer=answer)
#     db.add(chat)
#     db.commit()
#     db.close()

#     return {"answer": answer}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from llm import ask_llm
from database import SessionLocal, Chat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5501", "http://localhost:5501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_question(data: dict):
    question = data.get("question")

    db = SessionLocal()
    previous_chats = db.query(Chat).all()
    context = "\n".join([f"Q: {c.question}\nA: {c.answer}" for c in previous_chats])

    prompt = f"{context}\nQ: {question}"

    answer = ask_llm(prompt)

    chat = Chat(question=question, answer=answer)
    db.add(chat)
    db.commit()
    db.close()

    return {"answer": answer}


# 🔥 ADD THIS PART
@app.get("/history")
def get_history():
    db = SessionLocal()
    chats = db.query(Chat).all()
    db.close()

    return [
        {"question": c.question, "answer": c.answer}
        for c in chats
    ]    