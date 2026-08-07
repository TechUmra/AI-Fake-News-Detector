# 📰 AI Fake News Detector

An AI-powered Fake News Detection System built using Machine Learning and Streamlit. The application predicts whether a news article is likely **Real** or **Fake** and also displays related news articles using NewsAPI.

---

## 🚀 Features

- 🧠 Machine Learning based Fake News Detection
- 📊 TF-IDF + Logistic Regression Model
- 📈 Confidence Score
- 📰 Latest Related News using NewsAPI
- 🎨 Interactive Streamlit User Interface
- ⚡ Fast and Easy to Use

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib
- NewsAPI
- TF-IDF Vectorizer
- Logistic Regression

---

## 📂 Project Structure

```
AI-Fake-News-Detector/
│
├── app.py
├── train_model.py
├── news_api.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
└── data/
    ├── Fake.csv
    └── True.csv
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/TechUmra/AI-Fake-News-Detector.git
```

Go to the project folder:

```bash
cd AI-Fake-News-Detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
NEWS_API_KEY=YOUR_NEWS_API_KEY
```

Train the model:

```bash
python train_model.py
```

Run the application:

```bash
streamlit run app.py
```

---

## 📊 Dataset

This project uses the **Fake and Real News Dataset** from Kaggle.

Download the dataset and place the following files inside the `data` folder:

- Fake.csv
- True.csv

---

## 📷 Screenshots

(Add screenshots of your application here.)

---

## 📌 Future Improvements

- AI-based News Summarization
- Similarity Matching with Online News
- Advanced Deep Learning Models (BERT)
- Multi-language Support
- News Credibility Score

---

## 👩‍💻 Author

**Umra Waqui**

GitHub: https://github.com/TechUmra
