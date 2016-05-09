
from popgen.utils import recursive_update_dict


COMPLEXITIES = {
    'simplest': {
        'melody': {
            'power': 1,
            'preferred_range': {
                'lower_offset': 0.4,
                'upper_offset': 0.6,
            },
            'maximum_range': {
                'lower_offset': 0.3,
                'upper_offset': 0.7,
            },
            'inner_drop_off': 0.1,
            'outer_drop_off': 0.3,
        }
    },
    'simple': {
        'melody': {
            'power': 1.2,
            'preferred_range': {
                'lower_offset': 0.35,
                'upper_offset': 0.65,
            },
            'maximum_range': {
                'lower_offset': 0.25,
                'upper_offset': 0.75,
            },
            'inner_drop_off': 0.08,
            'outer_drop_off': 0.25,
        }
    },
    'normal': {
        'melody': {
            'power': 1.5,
            'preferred_range': {
                'lower_offset': 0.3,
                'upper_offset': 0.7,
            },
            'maximum_range': {
                'lower_offset': 0.2,
                'upper_offset': 0.8,
            },
            'inner_drop_off': 0.06,
            'outer_drop_off': 0.2,
        }
    },
    'complex': {
        'melody': {
            'power': 1.9,
            'preferred_range': {
                'lower_offset': 0.25,
                'upper_offset': 0.75,
            },
            'maximum_range': {
                'lower_offset': 0.15,
                'upper_offset': 0.85,
            },
            'inner_drop_off': 0.04,
            'outer_drop_off': 0.15,
        },
    },
    'complexest': {
        'melody': {
            'power': 2.5,
            'preferred_range': {
                'lower_offset': 0.2,
                'upper_offset': 0.8,
            },
            'maximum_range': {
                'lower_offset': 0.1,
                'upper_offset': 0.9,
            },
            'inner_drop_off': 0.02,
            'outer_drop_off': 0.10,
        },
    },
}


def get_complexity(complexity):
    complexity_data = COMPLEXITIES[complexity]
    return lambda data: recursive_update_dict(data, complexity_data)
