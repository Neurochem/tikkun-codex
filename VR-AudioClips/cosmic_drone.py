from midiutil import MIDIFile

midi = MIDIFile(1)
track = 0
channel = 0
time = 0
tempo = 60
midi.addTempo(track, time, tempo)

# Drone notes: C2 (36) and G2 (43)
drone_notes = [36, 43]

# Single 60-second sustained chord
for pitch in drone_notes:
    midi.addNote(track, channel, pitch, 0, 60, 80)

with open("cosmic_drone.mid", "wb") as f:
    midi.writeFile(f)
