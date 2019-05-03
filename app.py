from flask import Flask, render_template, redirect, request
import random
import os
import urllib

from affirmation_generator import generate_affirmation, generate_birthday_message

app = Flask(__name__)


# TODO: Sentiment analysis of sentences to decide on appropriate colours. ???
# TODO: add share link button
# TODO: Experiment with Markov Chains
# TODO: Get it to work with '___' instead of specifying adj, verb, etc.


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
    "font-family: 'Comfortaa', cursive;",
    "font-family: 'Poiret One', cursive;",
    "font-family: 'Flamenco', cursive;",
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


@app.route('/home')
def home():
    color = generate_gradient()

    url_split = urllib.parse.urlsplit(request.base_url)
    scheme = url_split.scheme or 'https'
    base_url = scheme + '://' + url_split.netloc

    return render_template('home.html', color=color, base_url=base_url)


@app.route('/seed=<seed_value>')
def positivity_generator(seed_value):
    random.seed(seed_value)
    color = generate_gradient()
    message = generate_affirmation()
    font = random.choice(FONTS)

    url_split = urllib.parse.urlsplit(request.base_url)
    scheme = url_split.scheme or 'https'
    base_url = scheme + '://' + url_split.netloc

    return render_template('affirmation.html', color=color, message=message, font=font, base_url=base_url,
                           seed_value=seed_value)


@app.route('/birthday/to=<birthday_person>/from=<sender>')
def birthday_with_sender_lean(birthday_person, sender):
    random.seed(os.urandom(100))
    seed_value = random.randint(0, 9999999999999)

    return redirect(f'/birthday/to={birthday_person}/from={sender}/seed={seed_value}')


@app.route('/birthday/to=<birthday_person>/')
def birthday_lean(birthday_person):
    random.seed(os.urandom(100))
    seed_value = random.randint(0, 9999999999999)

    return redirect(f'/birthday/to={birthday_person}/seed={seed_value}')


@app.route('/birthday/to=<birthday_person>/seed=<seed_value>')
def birthday(birthday_person, seed_value):
    # TODO: Way too much repeated code right here
    random.seed(seed_value)
    color = generate_gradient()
    message = generate_birthday_message(birthday_person)
    font = random.choice(FONTS)

    url_split = urllib.parse.urlsplit(request.base_url)
    scheme = url_split.scheme or 'https'
    base_url = scheme + '://' + url_split.netloc + '/birthday/to={name}'

    return render_template('affirmation.html', color=color, message=message, font=font, base_url=base_url,
                           seed_value=seed_value, recipient=birthday_person)


@app.route('/birthday/to=<birthday_person>/from=<sender>/seed=<seed_value>')
def birthday_with_sender(birthday_person, sender, seed_value):
    random.seed(seed_value)
    color = generate_gradient()
    message = generate_birthday_message(birthday_person, sender=sender)
    font = random.choice(FONTS)

    url_split = urllib.parse.urlsplit(request.base_url)
    scheme = url_split.scheme or 'https'
    base_url = scheme + '://' + url_split.netloc + '/birthday/to={name}/from={sender}'

    return render_template('affirmation.html', color=color, message=message, font=font, base_url=base_url,
                           seed_value=seed_value, recipient=birthday_person, sender=sender)


if __name__ == '__main__':
    app.run()
