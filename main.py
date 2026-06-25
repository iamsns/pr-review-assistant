from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from api.routes import router

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status":"healthy"
    }
    
app.include_router(router=router)