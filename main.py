from fastapi import FastAPI, File, UploadFile
import shutil
import pytesseract

app = FastAPI()

# IMPORTANT: Tesseract executable ka exact path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


@app.post("/ocr")
def ocr(image: UploadFile = File(...)):

    file_path = "uploaded_image.jpg"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    text = pytesseract.image_to_string(
        file_path,
        lang="eng"
    )

    return text