from form import make_form


# def main():
#     form = make_form()
#     for settings in form:
#         bars = []
#         harmonies = []
#         for harm_rhythm in settings['harmonic_rhythm']:
#             bar = []
#             for note in harm_rhythm:


class AnimalPlay(object):
    title = 'Animal Play'
    composer = 'Jonathan Marmor'
    def __init__(self):
        self.form = make_form()

        instruments = [
            'violin',
            'clarinet',
            'cello',
            'piano',
            'synthesizer'
        ]


# piece = {
#     'violin': {
#         'full_name': 'vln',
#         'long_name': 'Violin',
#         'measures': [
#             'ending_barline_type': 'single',
#             'time_signature': '4/4',
#             'notes': [
#                 {
#                     'pitches': [61],
#                     'duration': '16.',
#                     'tie': 'start',
#                     'dynamic': 'mf',
#                     'beam': 'start',
#                     'instruction': 'brooding',
#                     'tempo_marking': '4 = 120',
#                     'section_marker': '1a',
#                     'breath': True,
#                     'gliss': 'start',
#                     ''
#                 },

#             ]

#         ]

#     }
#     'clarinet':
#     'cello':
#     'piano':
#     'synthesizer':
# }

