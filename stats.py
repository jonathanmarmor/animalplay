from collections import Counter


pitches = Counter()
pitch_classes = Counter()

chords = Counter()
fifth_roots = Counter()
chord_types = Counter()
harmonic_intervals = Counter()

chord_bigrams = Counter()
chord_type_bigrams = Counter()
melodic_interval_bigrams = Counter()

chord_history = []

previous = []

def harmonies(chord):
    chord_history.append(chord)
    for p in chord:
        pitches[p] += 1
        pc = p % 12
        pitch_classes[pc] += 1



class Chord(object):
    def __init__(self, pitches):
        self.pitches = pitches
        self.pitchclasses = [p % 12 for p in pitches]
