
import os
import yaml
import pickle
import shutil
from random import randint, randrange, choice, random
from tempfile import NamedTemporaryFile
from time import time

from django.shortcuts import render

from popgen.composition import DEFAULT_PARAMETERS
from popgen import composition, soundfonts
from pydub import AudioSegment

from .forms import MinstrelForm, keys
from .instruments import INSTRUMENTS
from . import utils


def shuffle(x):
    return sorted(x, key=lambda k: random())


def convert_to_mp3(session):
    composition_path = session['composition.path']

    current_path = os.path.join(composition_path, "%d" % time())
    if not os.path.exists(current_path):
        os.makedirs(current_path)
    yaml_file = os.path.join(current_path, 'params.yaml')
    shutil.copy(session['composition.params'], yaml_file)

    composer = composition.Composer.from_yaml(yaml_file)
    composer.compose()
    midi_file = os.path.join(current_path, 'minstrel.midi')
    composer.save(midi_file)

    audio_filename = "minstrel.mp3"
    audio_file = os.path.join(current_path, audio_filename)

    with NamedTemporaryFile(suffix='.wav') as wav_file:
        utils.play(midi_file, soundfonts.DEFAULT_SOUNDFONT, wav_file.name)
        audio_file = audio_file
        with open(audio_file, 'w+') as audio_file_:
            AudioSegment.from_wav(wav_file).export(audio_file_, format="mp3")

    return audio_file.replace('minstrel/static/', '')  # TODO find a better way


def save_yaml(data, yaml_file):

    params = {}
    # Tempo
    params['tempo'] = {
        'lower': data['tempo_lower'],
        'upper': data['tempo_upper'],
        'fixed': data.get('tempo_fixed', None),
    }
    # Key
    params['key'] = data['key']
    # Harmony markov chain
    params['harmony'] = {}
    params['harmony']['markov_chain'] = []
    prog = ['I', 'II', 'III', 'IV', 'V', 'VI']
    for cur in prog:
        key = 'harmony_markov_chain_%s' % cur
        params['harmony']['markov_chain'].append(pickle.loads(data[key]))

    # Melody Harmonic Compilance
    params['melody'] = {}
    params['melody']['harmonic_compilance'] = []
    prog = ['I', 'II', 'III', 'IV', 'V', 'VI']
    for cur in prog:
        key = 'melody_harmonic_compilance_%s' % cur
        params['melody']['harmonic_compilance'].append(pickle.loads(data[key]))

    # Melody Params
    params['melody']['power'] = data['melody_power']
    params['melody']['preferred_range'] = {
        'center': data['melody_preferred_center'],
        'lower_offset': data['melody_preferred_lower'],
        'upper_offset': data['melody_preferred_upper'],
    }
    params['melody']['maximum_range'] = {
        'lower_offset': data['melody_maximum_lower'],
        'upper_offset': data['melody_maximum_upper'],
    }
    params['melody']['inner_drop_off'] = data['melody_inner_drop_off']
    params['melody']['outer_drop_off'] = data['melody_outer_drop_off']
    params['melody']['dynamics'] = pickle.loads(data['melody_dynamics'])

    # Instruments
    params['instruments'] = dict(
        melody=data['instruments_melody'],
        chord=data['instruments_chord'],
        bass=data['instruments_bass']
    )

    with open(yaml_file, 'w') as file_:
        yaml.safe_dump(params, file_, default_flow_style=False)


def load_yaml(filename):
    params = DEFAULT_PARAMETERS.copy()
    with open(filename, 'r') as file_:
        params.update(yaml.load(file_))
    conv_params = {
        'tempo_lower': params['tempo']['lower'],
        'tempo_upper': params['tempo']['upper'],
        'tempo_fixed': params['tempo'].get('fixed', None),
        'key': params['key'],
        'melody_power': params['melody']['power'],
        'melody_preferred_center':
            params['melody']['preferred_range']['center'],
        'melody_preferred_lower':
            params['melody']['preferred_range']['lower_offset'],
        'melody_preferred_upper':
            params['melody']['preferred_range']['upper_offset'],
        'melody_maximum_lower':
            params['melody']['maximum_range']['lower_offset'],
        'melody_maximum_upper':
            params['melody']['maximum_range']['upper_offset'],
        'melody_inner_drop_off': params['melody']['inner_drop_off'],
        'melody_outer_drop_off': params['melody']['outer_drop_off'],
        'instruments_melody': params['instruments']['melody'],
        'instruments_chord': params['instruments']['chord'],
        'instruments_bass': params['instruments']['bass'],
    }
    prog = ['I', 'II', 'III', 'IV', 'V', 'VI']
    for a, p in enumerate(prog):
        for i, value in enumerate(params['harmony']['markov_chain'][a]):
            conv_params['harmony_markov_chain_%s_%s' % (p, i)] = value

    for a, p in enumerate(prog):
        for i, value in enumerate(params['melody']['harmonic_compilance'][a]):
            conv_params['melody_harmonic_compilance_%s_%s' % (p, i)] = value

    for i, value in enumerate(params['melody']['dynamics']):
        conv_params['melody_dynamics_%s' % i] = value

    return conv_params


def get_yaml_file(session):
    session_path = 'minstrel/static/tmp/%d' % time()
    session_path = session.get('composition.path', session_path)
    if not os.path.exists(session_path):
        os.makedirs(session_path)
        session['composition.path'] = session_path

    yaml_file = os.path.join(session_path, 'current_params.yaml')
    if not os.path.exists(session.get('composition.params', yaml_file)):
        with open(yaml_file, 'w+') as file_:
            params = DEFAULT_PARAMETERS.copy()
            yaml.safe_dump(params, file_, default_flow_style=False)
            session['composition.params'] = yaml_file

    return session['composition.params']


def random_params():
    params = DEFAULT_PARAMETERS.copy()
    tempo_lower = randint(40, 120)
    instruments = choice(INSTRUMENTS)
    conv_params = {
        'tempo_lower': tempo_lower,
        'tempo_upper': tempo_lower + randint(1, 120),
        'key': choice(keys)[0],
        'melody_power': randrange(50, 500, 25) / 100.,
        'melody_preferred_center': randint(2, 4),
        'melody_preferred_lower': randint(2, 8),
        'melody_preferred_upper': randint(2, 8),
        'melody_maximum_lower': randint(1, 6),
        'melody_maximum_upper': randint(1, 6),
        'melody_inner_drop_off': randrange(1, 200, 1) / 100.,
        'melody_outer_drop_off': randrange(1, 200, 1) / 100.,
        'instruments_melody': instruments['melody'],
        'instruments_chord': instruments['chord'],
        'instruments_bass': instruments['bass'],
    }
    prog = ['I', 'II', 'III', 'IV', 'V', 'VI']
    for a, p in enumerate(prog):
        for i in range(len(params['harmony']['markov_chain'][a])):
            value = randrange(1, 60, 1)
            conv_params['harmony_markov_chain_%s_%s' % (p, i)] = value

    for a, p in enumerate(prog):
        for i in range(len(params['melody']['harmonic_compilance'][a])):
            value = randrange(1, 99, 7) / 100.
            conv_params['melody_harmonic_compilance_%s_%s' % (p, i)] = value

    for i in range(len(params['melody']['dynamics'])):
        value = randrange(1, 12)
        conv_params['melody_dynamics_%s' % i] = value

    return conv_params


def happy_params():
    # +10 bpm
    # Major
    # +5dB
    # +4 semitons
    tempo_lower = randint(90, 120)
    conv_params = random_params()
    conv_params.update({
        'tempo_lower': tempo_lower,
        'tempo_upper': tempo_lower + randint(30, 60),
        'key': choice(['E', 'F', 'G', 'A', 'B'])[0],
        'melody_preferred_center': 4,
        'melody_preferred_lower': randint(2, 4),
        'melody_preferred_upper': randint(4, 8),
        'melody_maximum_lower': randint(1, 3),
        'melody_maximum_upper': randint(2, 4),
    })
    for i in range(16):
        value = randrange(5, 14)
        conv_params['melody_dynamics_%s' % i] = value

    return conv_params


def angry_params():
    # 10+ bpm
    # Minor
    # +7dB
    # +0 semitons
    tempo_lower = randint(90, 120)
    conv_params = random_params()
    conv_params.update({
        'tempo_lower': tempo_lower,
        'tempo_upper': tempo_lower + randint(30, 60),
        'key': choice(['c', 'c#', 'd', 'd#', 'e'])[0],
        'melody_preferred_center': 4,
        'melody_preferred_lower': randint(2, 5),
        'melody_preferred_upper': randint(2, 5),
        'melody_maximum_lower': randint(1, 3),
        'melody_maximum_upper': randint(1, 3),
    })
    for i in range(16):
        value = randrange(8, 17)
        conv_params['melody_dynamics_%s' % i] = value

    return conv_params


def sad_params():
    # -15 bpm
    # Minor
    # -5dB
    # -4 semitons
    tempo_lower = randint(60, 90)
    conv_params = random_params()
    conv_params.update({
        'tempo_lower': tempo_lower,
        'tempo_upper': tempo_lower + randint(10, 30),
        'key': choice(['e', 'f', 'g', 'a', 'b'])[0],
        'melody_preferred_center': 3,
        'melody_preferred_lower': randint(4, 8),
        'melody_preferred_upper': randint(2, 4),
        'melody_maximum_lower': randint(2, 4),
        'melody_maximum_upper': randint(1, 3),
    })
    for i in range(16):
        value = randrange(4, 9)
        conv_params['melody_dynamics_%s' % i] = value

    return conv_params


def tender_params():
    # +10 bpm
    # Major
    # +5dB
    # +4 semitons
    tempo_lower = randint(60, 80)
    conv_params = random_params()
    conv_params.update({
        'tempo_lower': tempo_lower,
        'tempo_upper': tempo_lower + randint(10, 20),
        'key': choice(['E', 'F', 'G', 'A', 'B'])[0],
        'melody_preferred_center': 4,
        'melody_preferred_lower': randint(2, 4),
        'melody_preferred_upper': randint(4, 8),
        'melody_maximum_lower': randint(1, 3),
        'melody_maximum_upper': randint(2, 4),
    })
    for i in range(16):
        value = randrange(1, 7)
        conv_params['melody_dynamics_%s' % i] = value

    return conv_params


def index(request):
    audio_file = None
    yaml_file = get_yaml_file(request.session)
    if request.method == "POST":
        if 'play' in request.POST:
            form = MinstrelForm(request.POST)
        elif 'random' in request.POST:
            form = MinstrelForm(random_params())
        elif 'happy' in request.POST:
            form = MinstrelForm(happy_params())
        elif 'angry' in request.POST:
            form = MinstrelForm(angry_params())
        elif 'sad' in request.POST:
            form = MinstrelForm(sad_params())
        elif 'tender' in request.POST:
            form = MinstrelForm(tender_params())

        if form.is_valid():
            save_yaml(form.cleaned_data, yaml_file)
            audio_file = convert_to_mp3(request.session)
    else:
        form = MinstrelForm(load_yaml(yaml_file))

    return render(request, 'minstrel/index.html', {
        'forms': [form],
        'audio_file': audio_file
    })
