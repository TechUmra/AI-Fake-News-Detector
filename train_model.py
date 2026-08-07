import pandas as pd
import re
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------
# Load datasets
# -------------------------------

fake = pd.read_csv("data/Fake.csv")
true = pd.read_csv("data/True.csv")

# Add labels
fake["label"] = 0
true["label"] = 1

# Merge datasets
df = pd.concat([fake, true], ignore_index=True)

print("Dataset Loaded Successfully")
print(df.shape)

# -------------------------------
# Combine title + text
# -------------------------------

df["content"] = df["title"].fillna("") + " " + df["text"].fillna("")

# -------------------------------
# Clean text
# -------------------------------

def clean_text(text):
    text = str(text).lower()

    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"www\S+", " ", text)

    text = re.sub(r"[^a-zA-Z ]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()

df["content"] = df["content"].apply(clean_text)

# -------------------------------
# Features
# -------------------------------

X = df["content"]

y = df["label"]

# -------------------------------
# Train Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -------------------------------
# Model
# -------------------------------

model = Pipeline([

    (
        "tfidf",

        TfidfVectorizer(
            stop_words="english",
            max_df=0.7
        )
    ),

    (
        "classifier",

        LogisticRegression(
            max_iter=2000
        )
    )

])

# -------------------------------
# Train
# -------------------------------

print("\nTraining Model...\n")

model.fit(X_train, y_train)

# -------------------------------
# Test
# -------------------------------

pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)

print(f"\nAccuracy : {acc*100:.2f}%\n")

print(classification_report(y_test, pred))

# -------------------------------
# Save Model
# -------------------------------

joblib.dump(model, "fake_news_model.pkl")

print("\nModel Saved Successfully!")