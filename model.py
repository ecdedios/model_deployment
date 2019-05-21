import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv('./spam_clean.csv')
df.head()

tfidf = TfidfVectorizer()

X = tfidf.fit_transform(df.text)
y = df.label

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.2)

lm = LogisticRegression(solver='saga').fit(X_train, y_train)

def predict(msg):
    return lm.predict(tfidf.transform([msg]))[0]