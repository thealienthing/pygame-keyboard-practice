import pygame
import game_settings

vec = pygame.math.Vector2

class Note(pygame.sprite.Sprite):
    def __init__(self, note_val):
        super().__init__()
        self.w = game_settings.NOTE_SPR_W
        self.h = self.w
        self.at_playhead = False
        self.note_val = note_val
        self.surf = pygame.Surface((self.w, self.h))
        self.surf.fill((128,255,40))
        self.font = pygame.font.SysFont("Arial", 12)
        self.textSurf = pygame.font.Font.render(self.font, str(self.note_val), True, pygame.color.Color(0, 0, 0,))
        self.surf.blit(self.textSurf, [self.w/2 - self.textSurf.get_width()/2, self.h/2 - self.textSurf.get_height()/2])
        self.pos = vec(self.w*note_val, self.h)
        self.rect = self.surf.get_rect()

        
    def update(self):
        self.pos += vec(0, 4)
        self.rect.midbottom = self.pos
        
class Deadzone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.w = game_settings.SCREEN_W
        self.h = 40
        self.surf = pygame.Surface((self.w, self.h))
        self.surf.fill((128,255,40))
        self.pos = vec(self.w/2, game_settings.SCREEN_H-self.h)
        self.rect = self.surf.get_rect()
        self.rect.midbottom = self.pos