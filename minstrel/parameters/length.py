
from popgen.utils import recursive_update_dict


LENGTHS = {
    'shortest': {
        # 8
        'simplest': [
            ('phrase', 1),
        ] * 8,
        'simple': [
            ('base', 1),
            ('phrase1', 1),
            ('base', 1),
            ('phrase2', 1),
        ] * 2,
        'normal': [
            ('intro', 1),
            ('pre-chorus', 1),
            ('chorus', 2),
            ('pre-chorus', 1),
            ('chorus', 2),
            ('final', 1),
        ],
        'complex': [
            ('base', 1),
            ('phrase1', 3),
            ('base', 1),
            ('phrase2', 3),
        ],
        'complexest': [
            ('phrase', 8),
        ],
    },
    'short': {
        # 16
        'simplest': [
            ('phrase', 2),
        ] * 8,
        'simple': [
            ('base', 2),
            ('phrase1', 2),
            ('base', 2),
            ('phrase2', 2),
        ] * 2,
        'normal': [
            ('intro', 1),
            ('pre-chorus', 2),
            ('chorus', 3),
            ('bridge', 1),
            ('pre-chorus', 2),
            ('chorus', 3),
            ('solo', 2),
            ('bridge', 1),
            ('final', 1),
        ],
        'complex': [
            ('base', 2),
            ('phrase1', 4),
            ('base', 2),
            ('phrase2', 4),
            ('base', 2),
            ('phrase3', 2),
        ],
        'complexest': [
            ('phrase', 16),
        ],
    },
    'normal': {
        # 24
        'simplest': [
            ('phrase', 2),
        ] * 12,
        'simple': [
            ('base', 2),
            ('phrase1', 2),
            ('base', 2),
            ('phrase2', 2),
        ] * 3,
        'normal': [
            ('intro', 3),
            ('pre-chorus', 2),
            ('chorus', 4),
            ('bridge', 2),
            ('pre-chorus', 2),
            ('chorus', 4),
            ('solo', 3),
            ('bridge', 2),
            ('final', 2),
        ],
        'complex': [
            ('base', 3),
            ('phrase1', 5),
            ('base', 3),
            ('phrase2', 5),
            ('base', 3),
            ('phrase3', 5),
        ],
        'complexest': [
            ('phrase', 24),
        ],
    },
    'long': {
        # 32
        'simplest': [
            ('phrase', 4),
        ] * 8,
        'simple': [
            ('base', 4),
            ('phrase1', 4),
            ('base', 4),
            ('phrase2', 4),
        ] * 2,
        'normal': [
            ('intro', 3),
            ('pre-chorus', 2),
            ('chorus', 4),
            ('bridge', 2),
            ('pre-chorus', 2),
            ('chorus', 4),
            ('solo', 5),
            ('pre-chorus', 2),
            ('chorus', 4),
            ('bridge', 2),
            ('final', 2),
        ],
        'complex': [
            ('base', 3),
            ('phrase1', 5),
            ('base', 3),
            ('phrase2', 5),
            ('base', 3),
            ('phrase3', 5),
            ('base', 3),
            ('phrase4', 5),
        ],
        'complexest': [
            ('base', 32),
        ],
    },
    'longest': {
        # 40
        'simplest': [
            ('phrase', 4),
        ] * 10,
        'simple': [
            ('base', 2),
            ('phrase1', 3),
            ('base', 2),
            ('phrase2', 3),
        ] * 4,
        'normal': [
            ('intro', 4),
            ('pre-chorus', 2),
            ('chorus-1', 4),
            ('chorus-2', 2),
            ('bridge', 3),
            ('pre-chorus', 2),
            ('chorus-1', 4),
            ('solo', 6),
            ('pre-chorus', 2),
            ('chorus-1', 4),
            ('chorus-2', 2),
            ('bridge', 3),
            ('final', 2),
        ],
        'complex': [
            ('base', 4),
            ('phrase1', 6),
            ('base', 4),
            ('phrase2', 6),
            ('base', 4),
            ('phrase3', 6),
            ('base', 4),
            ('phrase4', 6),
        ],
        'complexest': [
            ('phrase', 40),
        ],
    },
}


def get_length(length, complexity):
    length_data = {
        'phrase_structure': LENGTHS[length][complexity]
    }
    return lambda data: recursive_update_dict(data, length_data)
