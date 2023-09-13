# import the pygame module, so you can use it
import pygame
from pygame.locals import *
import spr_note
from MIDISpriteGenerator import MIDISpriteGenerator
import random
from threading import Thread

midi_file = "Vampire_Killer_1.mid"
sound_font = "8bitsf.sf2"
 
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
                
        displaysurface.fill((0,50,0))
        for spr in notes:
            spr.update()
            displaysurface.blit(spr.surf, spr.rect)
            
        displaysurface.blit(dead_zone.surf, dead_zone.rect)
        
        if pygame.sprite.spritecollideany(dead_zone, notes):
            for spr in notes:
                if pygame.sprite.spritecollide(dead_zone, notes, True):
                    print("Note end: ", len(notes))
            

        pygame.display.update()
        
        if tick % 30 == 0:
            if random.choice([True, False]):
                notes.add(spr_note.Note(random.choice(['C4', 'D4', 'E4', 'F4', 'G5', 'A5'])))
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()