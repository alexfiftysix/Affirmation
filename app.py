from flask import Flask, render_template
import random

from affirmation_generator import generate_affirmation

app = Flask(__name__)

COLOURS = [
    (0, 255, 255),  # CYAN
    (0, 255, 0),  # GREEN
    (255, 0, 200),  # PINK
    # (255, 255, 0),  # YELLOW
    # (255, 165, 0),  # ORANGE
    (200, 0, 255),  # PURPLE
    (0, 180, 255),  # BLUE
    (255, 0, 102),  # HOT PINK
    (127, 255, 36),  # ALERT
    (205, 233, 202),  # BRIGHT EYES
    (255, 72, 71),  # CORAL RED
    (181, 255, 206),  # FRESHMINT
    (252, 6, 67),  # ELECTRIC CRIMSON
    (255, 117, 255),  # SOFT PINK
]

GRADIENT_DIRECTIONS = [
    'to bottom right',
    'to bottom left',
    'to top right',
    'to top left',
    'to bottom',
    'to right',
    'to top',
    'to left'
]


# TODO: different fonts
# TODO: Mobile support

@app.route('/')
def hello_world():
    message = generate_affirmation()

    tc = COLOURS[random.randint(0, len(COLOURS) - 1)]
    top_colour = '{}, {}, {}'.format(tc[0], tc[1], tc[2])

    bc = [min(255, x + 150) for x in tc]
    bottom_colour = '{}, {}, {}'.format(bc[0], bc[1], bc[2])

    gradient_direction = GRADIENT_DIRECTIONS[random.randint(0, len(GRADIENT_DIRECTIONS) - 1)]

    return render_template('affirmation.html', message=message, top_colour=top_colour, bottom_colour=bottom_colour,
                           gradient_direction=gradient_direction)
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()
