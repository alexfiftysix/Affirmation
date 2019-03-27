from flask import Flask, render_template
import random

app = Flask(__name__)

POSITIVE_MESSAGES = [
    "You're Doing Great!",
    "Nice One!",
    "Fantastic Presentation!",
    "I've never felt more alive!",
    "Ultimate Champion!",
    "Wow!",
    "Oh My Gosh that was crazy good",
    "How fanciful!",
    "Incredible!",
    "Brilliant talk",
    "Outlandish quality!"
]


@app.route('/')
def hello_world():
    index = random.randint(0, len(POSITIVE_MESSAGES) - 1)
    print(POSITIVE_MESSAGES[index])
    return render_template('affirmation.html', message=POSITIVE_MESSAGES[index])
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()
