from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO

app = FastAPI()

# Ativando CORS para permitir acesso do GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Você pode restringir isso para o domínio do GitHub Pages depois
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remover-fundo")
async def remover_fundo(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove(input_image)

    return StreamingResponse(BytesIO(output_image), media_type="image/png")
