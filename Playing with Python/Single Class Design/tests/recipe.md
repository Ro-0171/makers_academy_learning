## 1. Describe the Problem

>As a user
>So that I can keep track of my music listening
>I want to add tracks I've listened to and see a list of them.


## 2. Design the Class interface

class MusicTracker:

>Firstly there will be the initializer
def __init__(self):
"""
Initialize an empty list here
"""

>Next there would be a method to add tracks

def add_track(self, track_name):
    #Parameters:
        track_name(str) - displays a track name

>Lastly there will be a method to display the tracks

def display_tracks(self):
    #for loop

## 3. Create Examples as Tests

"""
There are no tracks
"""
music_tracker = MusicTracker()
assert len(music_tracker.tracks) == 0

"""
We add a single track
"""
music_tracker = MusicTracker()
music_tracker.add_track("Song 1")
assert "Song 1" in music_tracker.tracks
 
"""
Then a test to add multiple tracks
""""
music_tracker = MusicTracker()
music_tracker.add_track("Song 2")
music_tracker.add_track("Song 3")
music_tracker.add_track("Song 4")
assert len(music_tracker.tracks) == 4

"""
Test if they're in the list
"""
music_tracker = MusicTracker()
music_tracker.add_track("Song 1")
music_tracker.add_track("Song 2")
music_tracker.add_track("Song 3")
music_tracker.add_track("Song 4")

assert music_tracker.tracks == ["Song 1", "Song 2", "Song 3", "Song 4"]



