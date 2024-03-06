from lib.music_tracker import *

def test_no_tracks():
    music_tracker = MusicTracker()
    assert len(music_tracker.tracks) == 0

def test_single_track():
    music_tracker = MusicTracker()
    music_tracker.add_track("Song 1")
    assert "Song 1" in music_tracker.tracks

def test_multiple_tracks():
    music_tracker = MusicTracker()
    music_tracker.add_track("Song 2")
    music_tracker.add_track("Song 3")
    music_tracker.add_track("Song 4")
    assert len(music_tracker.tracks) == 3

def test_tracks_in_list():
    music_tracker = MusicTracker()
    music_tracker.add_track("Song 1")
    music_tracker.add_track("Song 2")
    music_tracker.add_track("Song 3")
    music_tracker.add_track("Song 4")
    assert music_tracker.tracks == ["Song 1", "Song 2", "Song 3", "Song 4"]

def test_adding_to_list():
    music_tracker = MusicTracker()
    initial_count = len(music_tracker.tracks)
    music_tracker.add_track("Song 5")
    music_tracker.add_track("Song 6")
    assert len(music_tracker.tracks) == initial_count + 2   