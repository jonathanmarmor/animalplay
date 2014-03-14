from collections import Counter


class Part(object):
    """Parent class for tracking state of a musical part."""
    def __init__(self):
        self.pc_count = Counter()
        self.pitch_count = Counter()
        self.melody_ngram_count = Counter()
        self.register_counter = Counter()


class Drone(Part):
    """Current state of the drone part"""
    def __init__(self):
        pass


class Piano(Part):
    """Current state of the Piano part"""
    def __init__(self):
        self.simultaneous_notes_count = Counter()
        self.simultaneous_notes_right_count = Counter()
        self.simultaneous_notes_left_count = Counter()
        self.harmonic_interval_count = Counter()


class Violin(Part):
    """Current state of the Violin part"""
    def __init__(self):
        pass


class Clarinet(Part):
    """Current state of the Violin part"""
    def __init__(self):
        pass


class Cello(Part):
    """Current state of the Violin part"""
    def __init__(self):
        pass


class Crawler(object):
    """Crawl through the piece, making choices note-by-note, for all instruments"""
    def __init__(self):
        pass
