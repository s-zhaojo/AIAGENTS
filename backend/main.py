from fastapi import FastAPI, Request, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import store
import pytesseract
from PIL import Image
import io
from bs4 import BeautifulSoup
import requests 

app = FastAPI()
# connect to frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return  {"message": "backend is running!"}

@app.get("/tasks")
async def add_task():
    data = await request.json()
    return store.add_task(data)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    return store.delete_task(task_id)

<<<<<<< HEAD
@app.post("/extract"):
=======
@app.post("/extract")
>>>>>>> eccf857be1d18f7320db84bacc435fffdef51ed6
async def extact_file(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return {"text":text.strip()}

@app.post("/extract_link")
async def extract_link(data: dict):
    url = data.get("url")
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        title = soup.title.string if soup.title else ""
        desc = soup.find("meta", attrs={"name": "description"})
        summary = desc["content"] if desc else ""
        return {
            "url": url,
            "title": title,
            "summary": summary
        }
    except Exception as e:
        return {"error": str(e)}
