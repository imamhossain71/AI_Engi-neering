import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

#  Dataset Load
df = pd.read_csv("data/train.csv")  
print(df.head())

#  Clean Function
def clean_text(text):
    if isinstance(text, str):   
        text = text.lower()
        text = re.sub(r'\[.*?\]', '', text)
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        text = re.sub(r'<.*?>+', '', text)
        text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub(r'\n', ' ', text)
        text = re.sub(r'\w*\d\w*', '', text)
        return text.strip()
    else:
        return ""   

#  Clean Apply
df['text'] = df['text'].fillna("")  
df['text'] = df['text'].apply(clean_text)

#  Train-Test Split
X = df['text']
y = df['label']   # 0 = Real, 1 = Fake (তোমার dataset অনুযায়ী adjust করো)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

#  Model Training (Logistic Regression)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Prediction
y_pred = model.predict(X_test_tfidf)

# Evaluation
print("\n Accuracy:", accuracy_score(y_test, y_pred))
print("\n Classification Report:\n", classification_report(y_test, y_pred))
