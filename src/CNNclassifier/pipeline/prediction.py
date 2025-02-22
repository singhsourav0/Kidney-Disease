import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model safely
        model_path = os.path.join("model", "model.h5")
        model = load_model(model_path, compile=False)

        # Load and preprocess image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image) / 255.0  # Normalize
        test_image = np.expand_dims(test_image, axis=0)

        # Predict and find class index
        prediction_probs = model.predict(test_image)
        result = np.argmax(prediction_probs, axis=1)

        # Debugging: Print probabilities
        print("Prediction probabilities:", prediction_probs)
        print("Predicted class index:", result[0])

        # Class label mapping
        class_labels = {0: 'Normal', 1: 'Tumor'}
        prediction = class_labels.get(result[0], "Unknown")

        return [{"image": prediction}]
