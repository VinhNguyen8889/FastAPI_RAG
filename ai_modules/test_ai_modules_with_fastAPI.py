from fastapi import FastAPI, UploadFile
from ai_modules import load_llm, process_pdf, generate_answer
import uvicorn
from pyngrok import ngrok


app = FastAPI()
llm = load_llm()
retriever = None

@app.post("/upload_pdf/")
async def upload(file: UploadFile):
    with open("temp.pdf", "wb") as f:
        f.write(await file.read())
    global retriever
    retriever = process_pdf("temp.pdf")
    query = "YOLOv10 là gì vậy?"
    return {"status": retriever.invoke(query)}

@app.get("/ask/")
def ask(q: str):
    if retriever is None:
        return {"error": "PDF not uploaded yet"}
    answer = generate_answer(retriever, llm, q)
    return {"answer": answer}

if __name__ == "__main__":
    public_url = ngrok.connect(8000)
    print("🌐 Public URL:", public_url)
    uvicorn.run(app, host="0.0.0.0", port=8000)