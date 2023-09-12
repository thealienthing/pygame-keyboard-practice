import mido
import sf2_loader as sf
import fluidsynth
import threading
import time

midi = mido.MidiFile("Vampire_Killer_1.mid")
fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload("8bitsf.sf2")
fs.program_select(0, sfid, 0, 56)
fs.program_select(1, sfid, 0, 32)
fs.program_select(2, sfid, 0, 56)
fs.program_select(9, sfid, 128, 0)

print(dir(midi))
# fluidsynth_instance.start(driver)  # Replace with the appropriate audio driver

# Load the SoundFont into FluidSynth


def play_file(midi):
    for msg in midi.play():
        if msg.type == "note_on":

            print(f"Note on {msg.note} | channel {msg.channel}")
            fs.noteon(msg.channel, msg.note, msg.velocity)
        elif msg.type == "note_off":
            print(f"Note off {msg.note}")
            fs.noteoff(msg.channel, msg.note)

if __name__ == "__main__":
    player = threading.Thread(target=play_file, args=(midi,))
    sprite_maker = threading.Thread(target=play_file, args=(midi,))
    
    sprite_maker.start()
    time.sleep(1)
    player.start()
    
    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("Break")
            break
    
    print("Done")