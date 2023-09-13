import mido
import sf2_loader as sf
import fluidsynth
import threading
import time
import pygame



class MIDISpriteGenerator():
    def __init__(self, midi_file, sound_font_file):
        self.midi_file = midi_file
        self.sound_font_file = sound_font_file
        self.midi = None
        
    def prepare_to_play(self):
        self.midi = mido.MidiFile(self.midi_file)
        self.fs = fluidsynth.Synth()
        self.fs.start()
        self.sfid = self.fs.sfload(self.sound_font_file)
        
        self.fs.program_select(0, self.sfid, 0, 56)
        self.fs.program_select(1, self.sfid, 0, 32)
        self.fs.program_select(2, self.sfid, 0, 56)
        self.fs.program_select(9, self.sfid, 128, 0)        


    def play(self):
        for msg in self.midi.play():
            if msg.type == "note_on":
                #print(f"Note on {msg.note} | channel {msg.channel}")
                #self.fs.noteon(msg.channel, msg.note, msg.velocity)
                if msg.channel == 0:
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, key='NOTEON', note_val=msg.note))
            elif msg.type == "note_off":
                if msg.channel == 0:
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, key='NOTEOFF', note_val=msg.note))
                #print(f"Note off {msg.note}")
                #self.fs.noteoff(msg.channel, msg.note)