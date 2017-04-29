from music21 import *

def translate_midi(song, original, x):
    x = str(x)
    if x in original:
        r = note.Note(original[x]["note"])
        r.duration.type = original[x]["duration"]
        if "dots" in original[x]:
            r.dots = original[x]["dots"]

    else:
        r = note.Rest(type='quarter')

    return song.append(r)

note_list = {"1":{"note":"G3", "duration":"64th"},
             "11":{"note":"F3", "duration":"64th"},
             "111":{"note":"G#1", "duration":"32nd", "dots":1},
             "1111":{"note":"A#2", "duration":"32nd", "dots":1},
             "112":{"note":"D4", "duration":"64th"},
             "2":{"note":"C7", "duration":"16th", "dots":1},
             "21":{"note":"D4", "duration":"32nd"},
             "211":{"note":"D5", "duration":"32nd"},
             "2111":{"note":"G#4", "duration":"32nd"},
             "2112":{"note":"A#4", "duration":"32nd"},
             "2113":{"note":"D#4", "duration":"32nd"},
             "2114":{"note":"F#7", "duration":"32nd"},
             "3":{"note":"A#5", "duration":"eighth"},
             "31":{"note":"D4", "duration":"64th"},
             "311":{"note":"C7", "duration":"128th"},
             "312":{"note":"D5", "duration":"128th"},
             "32":{"note":"B#3", "duration":"128th"},
             "321":{"note":"A#2", "duration":"64th"},
             "3211":{"note":"G#2", "duration":"16th"},
             "322":{"note":"C4", "duration":"128th"},
             "33":{"note":"G#1", "duration":"128th"},
             "331":{"note":"G3", "duration":"64th"},
             "3311":{"note":"G3", "duration":"64th"},
             "33111":{"note":"G3", "duration":"32nd"},
             "332":{"note":"F5", "duration":"32nd"},
             "3321":{"note":"A##5", "duration":"32nd"},
             "4":{"note":"G#3", "duration":"32nd"},
             "41":{'note':'A#6', 'duration':'128th'},
             "5":{"note":"G#3", "duration":"64th", "dots":1},
             "511":{'note':'G7', 'duration':'128th'},
             "5111":{'note':'D5', 'duration':'eighth'},
             "5112":{'note':'B#3', 'duration':'64th'},
             "6":{'note':'A##6', 'duration':'64th'},
             "61":{'note':'A#6', 'duration':'32nd', 'dots':1},
             "999":{"note":"G3", "duration":"64th"}}

new_song = stream.Stream()


