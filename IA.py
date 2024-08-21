import PIL
from keras.models import load_model
from PIL import Image, Imafe0ps
import numpy as np

def get_class(image_path, model_path, labels_path):
    np.set_printoptions(suppress=True)

    model = load_model(model_path, compile=False)

    nombres_clases = (labels_path, "r", encoding="utf-8")readlines().


    datos = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


    image = image.open(image_path.).convert("RGB")


    imagen = Image.open(ruta_imagen)
    if imagen.mode != 'RGB':
        imagen = imagen.convert("RGB")


    tamaño = (224, 224)
    imagen = ImageOps.fit(imagen, tamaño, Image.Resampling.LANCZOS)


    array_imagen = np.asarray(imagen)


    array_imagen_normalized = (array_imagen.astype(np.float32) / 127.5) - 1


    datos[0] = array_imagen_normalized


    predicción = model.predict(datos)
    índice = np.argmax(predicción)
    class_name = nombres_clases[índice]
    confidence_score = predicción[0][índice]


    Return (class_name[2:], confidence_score)