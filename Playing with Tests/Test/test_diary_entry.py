import pytest
from lib.diary_entry import *

"""
Given a title of contents
#format returns a formatted entry e.g.:
'My Title: These are my contents
"""

def test_format_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some Contents")
    result = diary_entry.format()
    assert result == "My Title: Some Contents"

"""
Given a title and contents
#count_words returns number of words in title and cintents
"""
def test_counts_words_in_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some Contents")
    result = diary_entry.count_words()
    assert result == 4

"""
Given empty title
Raise an error
"""
def test_empty_title():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "my contents")
    assert str(err.value) == "Diary entry must have a title and contents"

"""
Given empty contents
Raise an error
"""
def test_empty_content():
    with pytest.raises(Exception) as err:
        DiaryEntry("my title", "")
    assert str(err.value) == "Diary entry must have a title and contents"

"""
Given a words per minute of 2
And a text with 2 words
reading_time returns a minute
"""

def test_reading_time_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My Title", "one two")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given a words per minute of 2
And a text with 4 words
reading_time returns 2 minutes
"""
def test_reading_time_two_wpm_and_four_words():
    diary_entry = DiaryEntry("My Title", "one two three four")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a words per minute of 2
And a text with 3 words
reading_time returns 2 minutes
"""
def test_reading_time_two_wpm_and_three_words():
    diary_entry = DiaryEntry("My Title", "one two three")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a words per minute of 0
reading_time raises an error
"""
def test_reading_time_wpm_at_zero():
    diary_entry = DiaryEntry("My Title", "one two three")
    with pytest.raises(Exception) as err:
        result = diary_entry.reading_time(0)
    assert str(err.value) == "Cannot calclulate reading time with wpm of 0"

"""
Given a contents of six words
And a words per minute of 2
And 2 minutes
reading_chunk returns the first four words
"""
def test_reading_chunk_two_wpm_and_two_minutes():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"

"""
Given a contents of six words
And a words per minute of 2 and 1 minute
First time, reading_chunk returns "one two"
Next time "three four"
Next time "five six"
"""
def test_reading_chunk_two_wpm_and_one_minute_called_mulpiple_times():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(1, 1) == "three"
    assert diary_entry.reading_chunk(2,1) == "four five"

"""
Given a contents of six words
If reading_chunk is called repeatedly
The last chunk is the last words in the text, even if shorter than could be read
The next chunk after that is at the start again
"""
def test_reading_chunk_wraps_around_on_multiple_calls():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 2) == "five six"
    assert diary_entry.reading_chunk(2,2) == "one two three four"

"""
Given a contents of six words
If reading_chunk is called repeatedly with an exact ending
The last chunk is the last words in the text
The next chunk after that is at the start again
"""
def test_reading_chunk_wraps_around_on_multiple_calls_with_exact_ending():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    assert diary_entry.reading_chunk(2,2) == "one two three four"