from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO

app = FastAPI()

@app.post("/remover-fundo")
async def remover_fundo(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove(input_image)

    return StreamingResponse(BytesIO(output_image), media_type="image/png")
