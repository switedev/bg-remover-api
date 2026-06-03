from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API is alive"}

@app.post("/remove-bg")
async def remove_bg(image: UploadFile = File(...)):

    from rembg import remove  # safe now

    input_image = await image.read()
    output = remove(input_image)

    return Response(content=output, media_type="image/png")
