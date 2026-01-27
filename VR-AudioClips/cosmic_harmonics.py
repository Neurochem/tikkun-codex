from midiutil import MIDIFile

midi = MIDIFile(1)
track = 0
channel = 0
time = 0
tempo = 60
midi.addTempo(track, time, tempo)

# C major arpeggio: C4, E4, G4, C5
notes = [60, 64, 67, 72]

# 60 seconds total, arpeggio every 8 seconds
duration = 1.5  # each note length
interval = 8    # seconds between arpeggio starts
total_time = 60

t = 0
while t < total_time:
    for i, pitch in enumerate(notes):
        midi.addNote(track, channel, pitch, t + i * 0.5, duration, 90)
    t += interval

with open("cosmic_arpeggio.mid", "wb") as f:
    midi.writeFile(f)
