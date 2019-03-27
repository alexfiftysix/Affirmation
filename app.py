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
    "Brilliant talk!",
    "Outlandish quality!",
    "Astonishing!",
    "Dreamy, Dynamic, Daring"
    "So Engaging!",
    "You did great!",
    "Euphoric!",
    "Exhilarating!",
    "It is clear that as well as having a gift for presentation, you have worked to achieve such skill"
]


@app.route('/')
def hello_world():
    message = POSITIVE_MESSAGES[random.randint(0, len(POSITIVE_MESSAGES) - 1)]
    message = message.title()
    print(message)
    return render_template('affirmation.html', message=message)
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()
