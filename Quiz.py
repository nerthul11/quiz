import pandas as pd

from flask import Flask, render_template, request
from random import randint

# Global quiz settings
quiz = pd.read_excel("Quiz.xlsx")
df = pd.DataFrame(quiz)

# Set global lists
questions = []
answers = []
chars = []

for i in range(int(pd.DataFrame(df).index.size)-1):
    question = pd.DataFrame(df, index=[i+1]).values[0][0]
    question = {'id': f"question{i}", 'text': question}
    questions.append(question)

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", questions=questions)

@app.route("/results", methods=["POST"])
def results():
    # Store all user's answers in a list.
    answers.clear()
    for i in range(int(pd.DataFrame(df).index.size)-1):
        answer = request.form.get(f"question{i}")
        answers.append(answer)

    # Set all character scores to 0
    chars.clear()
    n = 0
    for column in df.columns:
        if n != 0:
            char = {'name': column, 'score': 0, 'text': pd.DataFrame(quiz, columns=[column]).values[0][0]}
            chars.append(char)
        n += 1

    # Check answers with all characters and submit their score
    for i in range(int(pd.DataFrame(df).index.size)-1):
        n = -1
        for column in df.columns:
            if answers[i] == pd.DataFrame(quiz, columns=[column]).values[i+1][0]:
                chars[n]['score'] += 1
            n += 1

    # Select winning characters
    max_score = 0
    winners = []
    for char in chars:
        current_score = char['score']
        if current_score > max_score:
            winners.clear()
            max_score = current_score
            winners.append({'name': char['name'], 'text': char['text']})
        elif current_score == max_score:
            winners.append({'name': char['name'], 'text': char['text']})
    return render_template("results.html", winners=winners)