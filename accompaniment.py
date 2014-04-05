import random


def next_accompaniment_notes(name_a, name_b, previous_a, previous_b, harmony, unused_harmony):


    pitch_a = random.choice(unused_harmony)
    # unused_harmony.remove(pitch_a % 12)
    pitch_b = random.choice(unused_harmony)
    # unused_harmony.remove(pitch_b % 12)
    return pitch_a, pitch_b
