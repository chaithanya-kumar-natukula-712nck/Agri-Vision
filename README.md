# 🌱 Agri-Vision

Agri-Vision is an intelligent agriculture-based system designed to assist farmers using Machine Learning and Deep Learning techniques. It consists of two main modules:

* 🌾 Crop Recommendation System
* 🍃 Leaf Disease Classification System

---

## 🚀 Features

### 🌾 Crop Recommendation

* Suggests the best crop based on:

  * Soil nutrients (N, P, K)
  * Temperature
  * Humidity
  * pH level
  * Rainfall
* Built using Machine Learning models

### 🍃 Leaf Disease Detection

* Classifies plant leaves as **Healthy or Diseased**
* Uses **CNN (Convolutional Neural Networks)**
* Trained on image datasets (fruits & vegetables)

---

## 🧠 Tech Stack

* **Programming Language:** Python 🐍
* **Libraries:** NumPy, Pandas, Scikit-learn, TensorFlow/Keras
* **Frontend:** HTML, CSS
* **Backend:** Flask / FastAPI
* **Tools:** Google Colab, Jupyter Notebook

---

## 📂 Project Structure

```
Agri-Vision/
│── crop_recommendation/
│   ├── model.pkl
│   ├── app.py
│
│── disease_classification/
│   ├── model.keras
│   ├── train.py
│   ├── predict.py
│
│── static/
│── templates/
|── notebooks/
│
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/chaithanya-kumar-natukula-712nck/Agri-Vision.git
cd agri-vision
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python app.py
```

---

## 📊 Model Details

### Crop Recommendation

* Algorithm: Random Forest / XGBoost
* Accuracy: ~70–75%

### Disease Classification

* Model: CNN / MobileNetV2
* Accuracy: ~87–90%
* Loss: ~0.38

---

## 🧪 Challenges Faced

* Large dataset → high training time
* Class imbalance
* Overfitting

### 🔧 Solutions

* Used **Dropout layers**
* Applied **Early Stopping (patience tuning)**
* Reduced dataset size for faster training

---

## 📈 Future Improvements

* Add real-time disease detection via mobile camera
* Improve accuracy using larger datasets
* Deploy as a mobile/web application
* Integrate weather API

---

## 🤝 Contribution

Feel free to fork this repo and contribute!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Chaithanya**
B.Tech CSE | Aspiring AI/ML Engineer
