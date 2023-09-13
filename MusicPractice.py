# import the pygame module, so you can use it
import pygame
from pygame.locals import *
import spr_note
from MIDISpriteGenerator import MIDISpriteGenerator
import random
from threading import Thread
import fluidsynth
import sf2_loader
import pygame



midi_file = "Vampire_Killer_1.mid"
sound_font = "8bitsf.sf2"
 
fs = fluidsynth.Synth()
fs.start()
sfid = fs.sfload(sound_font)

fs.program_select(0, sfid, 0, 56)
fs.program_select(1, sfid, 0, 32)
fs.program_select(2, sfid, 0, 56)
fs.program_select(9, sfid, 128, 0)  
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("ase256.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen_width = 1920
    screen_height = 1080
    displaysurface = pygame.display.set_mode((screen_width,screen_height))
    FPS = 60
    FramePerSec = pygame.time.Clock()
    pygame.display.set_caption("Game")

    
    midi_sprite_gen = MIDISpriteGenerator(midi_file, sound_font)
    midi_sprite_gen.prepare_to_play()
    sprite_gen_thread = Thread(target=midi_sprite_gen.play)
    notes = pygame.sprite.Group()
    dead_zone = spr_note.Deadzone()
     
    # define a variable to control the main loop
    running = True
    tick = 0
    # main loop
    sprite_gen_thread.start()
    while running:
        tick += 1
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.USEREVENT:
                notes.add(spr_note.Note(event.note_val))
                
        displaysurface.fill((0,50,0))
        for spr in notes:
            spr.update()
            displaysurface.blit(spr.surf, spr.rect)
            
        displaysurface.blit(dead_zone.surf, dead_zone.rect)
        
        if pygame.sprite.spritecollideany(dead_zone, notes):
            for spr in notes:
                if pygame.sprite.collide_rect(dead_zone, spr):
                    if not spr.at_playhead:
                        spr.at_playhead = True
                        fs.noteon(0, spr.note_val, 80)
                elif spr.at_playhead:
                    print("Note complete")
                    fs.noteoff(0, spr.note_val)
                    spr.kill()
            

        pygame.display.update()
        
        # if tick % 30 == 0:
        #     if random.choice([True, False]):
        #         notes.add(spr_note.Note(random.randrange(0, 127)))
     
     
# def generate_sprites():
#     midi_sprite_gen = MIDISpriteGenerator(midi_file, sound_font)
#     midi_sprite_gen.prepare_to_play()
#     midi_sprite_gen.play()
    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()