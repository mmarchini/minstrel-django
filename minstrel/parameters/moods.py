
from random import randint, randrange, choice

from popgen.utils import recursive_update_dict


def happy(conv_params):
    # +10 bpm
    # Major
    # +5dB
    # +4 semitons
    tempo_lower = randint(90, 120)
    recursive_update_dict(conv_params, {
        'tempo': {
            'lower': tempo_lower,
            'upper': tempo_lower + randint(30, 60),
        },
        'key': choice(['E', 'F', 'G', 'A', 'B'])[0],
    })
    conv_params['melody']['preferred_range']['lower_offset'] += 0.1
    conv_params['melody']['preferred_range']['upper_offset'] += 0.1
    conv_params['melody']['maximum_range']['lower_offset'] += 0.1
    conv_params['melody']['maximum_range']['upper_offset'] += 0.1
    for i in range(16):
        value = randrange(5, 14)
        conv_params['melody']['dynamics'][i] = value

    return conv_params


def angry(conv_params):
    # 10+ bpm
    # Minor
    # +7dB
    # +0 semitons
    tempo_lower = randint(90, 120)
    recursive_update_dict(conv_params, {
        'tempo': {
            'lower': tempo_lower,
            'upper': tempo_lower + randint(30, 60),
        },
        'key': choice(['c', 'c#', 'd', 'd#', 'e'])[0],
    })
    for i in range(16):
        value = randrange(8, 17)
        conv_params['melody']['dynamics'][i] = value

    return conv_params


def sad(conv_params):
    # -15 bpm
    # Minor
    # -5dB
    # -4 semitons
    tempo_lower = randint(60, 90)
    recursive_update_dict(conv_params, {
        'tempo': {
            'lower': tempo_lower,
            'upper': tempo_lower + randint(10, 30),
        },
        'key': choice(['e', 'f', 'g', 'a', 'b'])[0],
    })
    conv_params['melody']['preferred_range']['lower_offset'] -= 0.1
    conv_params['melody']['preferred_range']['upper_offset'] -= 0.1
    conv_params['melody']['maximum_range']['lower_offset'] -= 0.1
    conv_params['melody']['maximum_range']['upper_offset'] -= 0.1
    for i in range(16):
        value = randrange(4, 9)
        conv_params['melody']['dynamics'][i] = value

    return conv_params


def tender(conv_params):
    # +10 bpm
    # Major
    # +5dB
    # +4 semitons
    tempo_lower = randint(60, 80)
    recursive_update_dict(conv_params, {
        'tempo': {
            'lower': tempo_lower,
            'upper': tempo_lower + randint(10, 20),
        },
        'key': choice(['E', 'F', 'G', 'A', 'B'])[0],
    })
    conv_params['melody']['preferred_range']['lower_offset'] += 0.1
    conv_params['melody']['preferred_range']['upper_offset'] += 0.1
    conv_params['melody']['maximum_range']['lower_offset'] += 0.1
    conv_params['melody']['maximum_range']['upper_offset'] += 0.1
    for i in range(16):
        value = randrange(1, 7)
        conv_params['melody']['dynamics'][i] = value

    return conv_params


def get_mood(mood):
    return {
        'happy': happy,
        'sad': sad,
        'tender': tender,
        'angry': angry,
    }[mood]
