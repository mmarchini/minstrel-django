
from popgen.utils import recursive_update_dict

INSTRUMENTS = {
    'acoustic': {
        'happy': {
            'instruments': {
                'melody': 'Harmonica',
                'chord': 'Acoustic Guitar (nylon)',
                'bass': 'Acoustic Bass',
                'rhythm': 'Acoustic Percussion',
            }
        },
        'sad': {
            'instruments': {
                'melody': 'Tango Accordion',
                'chord': 'Acoustic Guitar (nylon)',
                'bass': 'Acoustic Bass',
                'rhythm': 'Acoustic Percussion',
            },
        },
        'angry': {
            'instruments': {
                'melody': 'Acoustic Guitar (steel)',
                'chord': 'Acoustic Guitar (nylon)',
                'bass': 'Acoustic Bass',
                'rhythm': 'Acoustic Percussion',
            },
        },
        'tender': {
            'instruments': {
                'melody': 'Accordion',
                'chord': 'Acoustic Guitar (nylon)',
                'bass': 'Acoustic Bass',
                'rhythm': 'Acoustic Percussion',
            },
        },
    },
    'jazz': {
        'happy': {
            'instruments': {
                'melody': 'Alto Sax',
                'chord': 'Electric Guitar (jazz)',
                'bass': 'Baritone Sax',
                'rhythm': "Jazz Percussion",
            },
        },
        'sad': {
            'instruments': {
                'melody': 'Tenor Sax',
                'chord': 'Bright Acoustic Piano',
                'bass': 'Cello',
                'rhythm': "Jazz Percussion",
            },
        },
        'tender': {
            'instruments': {
                'melody': 'Trumpet',
                'chord': 'Electric Grand Piano',
                'bass': 'Cello',
                'rhythm': "Jazz Percussion",
            },
        },
        'angry': {
            'instruments': {
                'melody': 'Tenor Sax',
                'chord': 'Electric Guitar (jazz)',
                'bass': 'Soprano Sax',
                'rhythm': "Jazz Percussion",
            },
        },
    },
    'orchestra': {
        'happy': {
            'instruments': {
                'melody': 'Violin',
                'chord': 'Viola',
                'bass': 'Pizzicato Strings',
                'rhythm': "Orchestra Percussion",
            },
        },
        'sad': {
            'instruments': {
                'melody': 'Orchestral Harp',
                'chord': 'Cello',
                'bass': 'Contrabass',
                'rhythm': "Orchestra Percussion",
            },
        },
        'tender': {
            'instruments': {
                'melody': 'Orchestral Harp',
                'chord': 'Viola',
                'bass': 'Contrabass',
                'rhythm': "Orchestra Percussion",
            },
        },
        'angry': {
            'instruments': {
                'melody': 'Violin',
                'chord': 'Cello',
                'bass': 'Pizzicato Strings',
                'rhythm': "Orchestra Percussion",
            },
        },
    },
    'piano': {
        'happy': {
            'instruments': {
                'melody': 'Honky-tonk Piano',
                'chord': 'Electric Piano 1',
                'bass': 'Electric Piano 2',
                'rhythm': "Piano Percussion",
            },
        },
        'sad': {
            'instruments': {
                'melody': 'Acoustic Grand Piano',
                'chord': 'Bright Acoustic Piano',
                'bass': 'Bright Acoustic Piano',
                'rhythm': "Piano Percussion",
            },
        },
        'tender': {
            'instruments': {
                'melody': 'Acoustic Grand Piano',
                'chord': 'Bright Acoustic Piano',
                'bass': 'Bright Acoustic Piano',
                'rhythm': "Piano Percussion",
            },
        },
        'angry': {
            'instruments': {
                'melody': 'Electric Grand Piano',
                'chord': 'Electric Piano 1',
                'bass': 'Electric Piano 2',
                'rhythm': "Piano Percussion",
            },
        },
    },
    'rock': {
        'happy': {
            'instruments': {
                'melody': 'Overdriven Guitar',
                'chord': 'Electric Guitar (jazz)',
                'bass': 'Slap Bass 1',
                'rhythm': "Rock Percussion",
            },
        },
        'sad': {
            'instruments': {
                'melody': 'Overdriven Guitar',
                'chord': 'Electric Guitar (jazz)',
                'bass': 'Electric Bass (finger)',
                'rhythm': "Rock Percussion",
            },
        },
        'tender': {
            'instruments': {
                'melody': 'Overdriven Guitar',
                'chord': 'Electric Guitar (muted)',
                'bass': 'Electric Bass (pick)',
                'rhythm': "Rock Percussion",
            },
        },
        'angry': {
            'instruments': {
                'melody': 'Pad3 (polysynth)',
                'chord': 'Overdriven Guitar',
                'bass': 'Slap Bass 2',
                'rhythm': "Rock Percussion",
            },
        },
    },
    'techno': {
        'happy': {
            'instruments': {
                'melody': 'SynthBrass 1',
                'chord': 'SynthStrings 1',
                'bass': 'Synth Bass 1',
                'rhythm': "Synth Percussion",
            },
        },
        'sad': {
            'instruments': {
                'melody': 'Lead1 (square)',
                'chord': 'Lead6 (voice)',
                'bass': 'Synth Voice',
                'rhythm': "Synth Percussion",
            },
        },
        'tender': {
            'instruments': {
                'melody': 'FX1 (rain)',
                'chord': 'Pad4 (choir)',
                'bass': 'Pad7 (halo)',
                'rhythm': "Synth Percussion",
            },
        },
        'angry': {
            'instruments': {
                'melody': 'Pad3 (polysynth)',
                'chord': 'FX 7 (echoes)',
                'bass': 'Lead3 (calliope)',
                'rhythm': "Synth Percussion",
            },
        },
    },
}


def get_instrument(instrument, mood):
    instruments_data = INSTRUMENTS[instrument][mood]
    return lambda data: recursive_update_dict(data, instruments_data)
