from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove
import io

app = FastAPI()

@app.get("/")
def home():
    return {"status": "BG Remover API is running"}

@app.post("/remove-bg")
async def remove_bg(image: UploadFile = File(...)):

    input_image = await image.read()

    try:
        output = remove(input_image)
        return Response(content=output, media_type="image/png")

    except Exception as e:
        return {"error": str(e)}
