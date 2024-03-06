class MusicTracker():
    def __init__(self):
        self.tracks = []

    def add_track(self, track_name):
        self.tracks.append(track_name)

    def display_tracks(self):
        for track in self.tracks:
            return track