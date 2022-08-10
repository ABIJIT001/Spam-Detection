import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Spam Classifier")

input_message = st.text_input("Enter the message")

if st.button('Predict'):
    # 1 preprocess
    transform_message = transform_text(input_message)

    # 2 vectorized
    vector_input = tfidf.transform([transform_message])

    # 3 predict
    result = model.predict(vector_input)

    # 4. Display

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
