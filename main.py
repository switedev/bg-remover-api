from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove, new_session
from PIL import Image
import io

app = FastAPI()

session = new_session("u2netp")

@app.get("/")
def home():
    return {"status": "API is alive"}

@app.post("/remove-bg")
async def remove_bg(image: UploadFile = File(...)):

    input_image = await image.read()

    # preprocess
    img = Image.open(io.BytesIO(input_image)).convert("RGBA")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    input_image = buffer.getvalue()

    # better removal
    output = remove(
        input_image,
        session=session,
        alpha_matting=True,
        alpha_matting_foreground_threshold=240,
        alpha_matting_background_threshold=10,
        alpha_matting_erode_size=10
    )

    return Response(content=output, media_type="image/png")
