from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
import os
from werkzeug.utils import secure_filename
from src.CNNclassifier.pipeline.prediction import PredictionPipeline  # Ensure correct import

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Directory to save uploaded images
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

class ClientApp:
    def __init__(self):
        self.filename = None  # Will store the uploaded image dynamically
        self.classifier = None  # Create PredictionPipeline instance when needed

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("dvc repro")  # Ensure DVC is set up properly
    return "Training done successfully!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image_file = request.files["image"]
    if image_file.filename == "":
        return jsonify({"error": "No selected file"}), 400



    filename = secure_filename(image_file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    image_file.save(filepath)

    # Run prediction
    clApp.filename = filepath  # Update filename dynamically
    clApp.classifier = PredictionPipeline(clApp.filename)
    result = clApp.classifier.predict()

    return jsonify({"prediction": result[0]["image"]})  # Format response properly

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=8080, debug=True)
