#simple webapp in flask
from flask import Flask, render_template
import random

app = Flask(__name__)

# Sample anime quotes
quotes = [
    "What are you so hesitant about? It’s your dream, isn’t it? It’s right in front of you, and you’re wavering? You gotta be reckless and take whatever you can!”,
    "Throughout heaven and earth, I alone am the honored one",
    #use an api to get quotes
]

@app.route('/')
def index():
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True)
