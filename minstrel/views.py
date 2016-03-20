
import os
import yaml
import pickle
from time import time

from django.shortcuts import render

from popgen.composition import DEFAULT_PARAMETERS
from popgen import composition

from .forms import MinstrelForm
from . import utils


def yaml_to_wav(yaml_file):
    composer = composition.Composer.from_yaml(yaml_file)
    composer.compose()

    midi_file = '/tmp/teste.midi'
    wave_path = 'minstrel/static/tmp/'
    if not os.path.exists(wave_path):
        os.makedirs(wave_path)
    wave_file = os.path.join(wave_path, "%d.wav" % time())

    composer.save(midi_file)
    utils.play(midi_file, 'arachno.sf2', wave_file)

    return 'tmp/%s' % os.path.basename(wave_file)


def save_yaml(form, yaml_file):
    data = form.cleaned_data

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
    with open(filename) as file_:
        params.update(yaml.load(file_))
    conv_params = {
        'tempo_lower': params['tempo']['lower'],
        'tempo_upper': params['tempo']['upper'],
        'tempo_fixed': params['tempo']['fixed'],
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


def index(request):
    wav_file = None
    yaml_file = 'lala.yaml'
    if request.method == "POST":
        print 'a'
        form = MinstrelForm(request.POST)
        if form.is_valid():
            save_yaml(form, yaml_file)
            wav_file = yaml_to_wav(yaml_file)
    else:
        form = MinstrelForm(load_yaml(yaml_file))

    return render(request, 'minstrel/index.html', {
        'forms': [form],
        'wav_file': wav_file
    })
