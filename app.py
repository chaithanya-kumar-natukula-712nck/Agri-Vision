from flask import Flask, render_template, request
import numpy as np
import pickle
from PIL import Image


from tensorflow.keras.models import load_model


#
app = Flask(__name__)

# ✅ Load Crop Model
model = pickle.load(open('model_cr.pkl', 'rb'))
scaler = pickle.load(open('scaler_crop.pkl', 'rb'))
encoder = pickle.load(open('crop_encoder.pkl', 'rb'))

# ✅ Load Disease Model 
# disease_model = load_model('plant_disease_model.keras')
# disease_model = load_model('plant_disease_model.keras', compile=False)
disease_model = load_model(
    "plant_disease_model.keras",
    compile=False,
    safe_mode=False
)

# ================= ROUTES =================

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')

@app.route('/disease')
def disease():
    return render_template('disease.html')

# ✅ About & Contact (you added)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# ================= CROP PREDICTION =================

@app.route('/crop_result', methods=['POST'])
def crop_result():
    data = [
        float(request.form['nitrogen']),
        float(request.form['phosphorus']),
        float(request.form['potassium']),
        float(request.form['temperature']),
        float(request.form['humidity']),
        float(request.form['ph']),
        float(request.form['rainfall'])
    ]

    data = np.array([data])
    data = scaler.transform(data)

    pred = model.predict(data)
    result = encoder.inverse_transform(pred)[0]

    return f"<h2>🌾 Recommended Crop: {result}</h2>"


# ================= DISEASE DETECTION =================

@app.route('/detect_disease', methods=['POST'])
def detect_disease():
    file = request.files['leaf_image']

    img = Image.open(file).convert('RGB')
    img = img.resize((160,160))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = disease_model.predict(img)
    result = np.argmax(pred)

    return f"<h2>🌿 Disease Class: {result}</h2>"


# ================= RUN =================

if __name__ == '__main__':
    app.run(debug=True)
