from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json

app = FastAPI(title="AI Image Generator API")

# Enable CORS for Frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

COMFYUI_URL = "http://127.0.0.1:8188"

class GenerationRequest(BaseModel):
    prompt: str
    negative_prompt: str = ""

@app.get("/")
def read_root():
    return {"status": "online", "message": "Backend API is running smoothly!"}

@app.post("/generate")
def generate_image(req: GenerationRequest):
    try:
        # Simple test payload check for ComfyUI
        response = requests.get(f"{COMFYUI_URL}/system_stats")
        if response.status_code == 200:
            return {"status": "success", "message": "Prompt received!", "prompt": req.prompt}
        else:
            raise HTTPException(status_code=500, detail="ComfyUI is not responding.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
