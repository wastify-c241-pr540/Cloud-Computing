from PIL import Image
import numpy as np

def preprocess_image(image: Image.Image, target_size=(180, 180)) -> np.ndarray:
    image = image.resize(target_size)
    image = np.array(image) / 255.0
    if image.shape[-1] == 4:  # Check for alpha channel and remove it
        image = image[..., :-1]
    return np.expand_dims(image, axis=0)