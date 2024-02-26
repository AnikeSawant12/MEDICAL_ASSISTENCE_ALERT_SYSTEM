
import os

from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from keras.preprocessing import image
from flask import send_from_directory
import numpy as np
from email_alert import send_email


app = Flask(__name__)

# Get the absolute path of the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
upload_dir = os.path.join(script_dir, 'img')

# Load the trained model
model = load_model('finalmodel.h5')

# Define the classes
classes = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}

# Define a function to preprocess the image
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(48, 48), grayscale=True)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.
    return img

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.files['image-input']
        if uploaded_file.filename != '':
            # Save the file
            image_path = os.path.join(upload_dir, uploaded_file.filename)
            uploaded_file.save(image_path)

            # Preprocess the image
            img = preprocess_image(image_path)

            # Make prediction
            prediction = model.predict(img)
            predicted_class = classes[np.argmax(prediction)]

             # Send email with the prediction result
            send_email(uploaded_file.filename, predicted_class)

            return render_template('result.html', image_name=uploaded_file.filename, text=predicted_class)
        

@app.route('/uploads/<filename>')
def send_image(filename):
    return send_from_directory('img/', filename)

if __name__ == '__main__':
    app.run(debug=True)




