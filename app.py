from flask import Flask, jsonify, request
import joblib
from keras.models import load_model
import base64  
import numpy as np
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Load the Scikit-learn model from model.pkl

# Load the Keras model
model = None
try:
    model = load_model("D:/epics/epicm.h5")
    print("Model loaded successfully")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")

# Dictionary mapping class indices to class names
class_name_dict = {
    0: 'cold and cough',
    1: 'fever',
    2: 'gastric problem',
    3: 'headache',
    4: 'stomach pain',
    5: 'suppress period related pain'
}

# Endpoint to perform image classification
@app.route('/classify_image', methods=['POST'])
def classify_image():
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500

        # Get the image data from the request
        data = request.get_json()
        base64_image = data['image']
        image_data = base64.b64decode(base64_image)
        
        # Create an in-memory binary stream from the image data
        img = Image.open(BytesIO(image_data))
        img = img.resize((224, 224))
        
        # Convert image to numpy array
        img_array = np.array(img)
        
        # Expand dimensions to match model input shape
        img_array = np.expand_dims(img_array, axis=0)
        
        # Normalize pixel values
        img_array = img_array.astype('float32') / 255.0
        
        # Make predictions using the loaded Keras model
        predictions = model.predict(img_array)
        
        # Get the predicted class name from the dictionary
        predicted_class = np.argmax(predictions)
        predicted_class_name = class_name_dict[predicted_class]
        
        # Prepare response with predicted class
        response_data = {
            'predicted_class': predicted_class_name
        }

        return jsonify(response_data)

    except Exception as e:
        print(f"Image classification failed. Error: {e}")
        return jsonify({'error': 'Image classification failed'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
