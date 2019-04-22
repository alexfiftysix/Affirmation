from flask import Flask, render_template, redirect, request
import random
import os
import urllib

from affirmation_generator import generate_affirmation

app = Flask(__name__)


# TODO: Sentiment analysis of sentences to decide on appropriate colours. ???
# TODO: different fonts


def generate_gradient_direction():
    """
    returns a randomly chosen gradient direction from those allowed in css
    """
    potential_directions = [
        'to bottom right',
        'to bottom left',
        'to top right',
        'to top left',
        'to bottom',
        'to right',
        'to top',
        'to left'
    ]

    return random.choice(potential_directions)


FONTS = [
    "font-family: 'Nanum Pen Script', cursive;",
    "font-family: 'Open Sans', sans-serif;",
    # "font-family: 'Coming Soon', cursive;",
    "font-family: 'Patrick Hand SC', cursive;",
    "font-family: 'sans-serif';",
]


def generate_gradient():
    """
    returns a gradient which can be dropped into css on an element and will function as a 'background-image'
    Chooses bright colours which should still support white text
    """
    # Yellow-brown range colours can look ugly
    hue_1 = hue_2 = hue_3 = 35
    while 30 <= hue_1 <= 80:
        hue_1 = random.randint(0, 359)
    saturation_1 = 100
    lightness_1 = 50

    gradient_step = random.randint(15, 45)

    # To avoid yellow-browns
    if hue_1 <= 30:
        hue_2 = hue_1 - gradient_step
        hue_3 = hue_2 - gradient_step
    else:
        hue_2 = hue_1 + gradient_step
        hue_3 = hue_2 + gradient_step

    color_1 = f"hsl({hue_1}, {saturation_1}%, {lightness_1}%)"
    color_2 = f"hsl({hue_2}, {saturation_1}%, {lightness_1}%)"
    color_3 = f"hsl({hue_3}, {saturation_1}%, {lightness_1}%)"

    gradient_direction = generate_gradient_direction()

    return f"background-image: linear-gradient({gradient_direction}, {color_1}, {color_2}, {color_3})"


@app.route('/')
def hello_world():
    random.seed(os.urandom(100))
    seed_value = random.randint(0, 9999999999999)
    return redirect(f'/seed={seed_value}')


@app.route('/seed=<seed_value>')
def positivity_generator(seed_value):
    random.seed(seed_value)
    color = generate_gradient()
    message = generate_affirmation(seed_value)
    font = random.choice(FONTS)

    url_split= urllib.parse.urlsplit(request.base_url)
    scheme = url_split.scheme or 'https'
    base_url = scheme + '://' + url_split.netloc
    print(base_url)

    return render_template('affirmation.html', color=color, message=message, font=font, base_url=base_url, seed_value=seed_value)


if __name__ == '__main__':
    app.run()
