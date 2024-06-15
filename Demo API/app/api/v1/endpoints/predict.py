from fastapi import APIRouter, File, UploadFile
from tensorflow.keras.models import load_model
from app.utilities.preprocess import preprocess_image
import numpy as np
from PIL import Image
import io

router = APIRouter()

model = load_model("app/db/model/trash.h5")

classes = {'cardboard': 0, 'glass': 1, 'metal': 2, 'paper': 3, 'plastic': 4, 'trash': 5}
class_names = {v: k for k, v in classes.items()}

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    img_array = preprocess_image(image)

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    return {"predicted_class": predicted_class}