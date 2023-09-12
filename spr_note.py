import pygame

vec = pygame.math.Vector2

class Note(pygame.sprite.Sprite):
    def __init__(self, note_name):
        super().__init__()
        print(ord(note_name[0]))
        self.w = 40
        self.h = 40
        self.note_name = note_name
        self.surf = pygame.Surface((self.w, self.h))
        self.surf.fill((128,255,40))
        self.font = pygame.font.SysFont("Arial", 12)
        self.textSurf = pygame.font.Font.render(self.font, self.note_name, True, pygame.color.Color(0, 0, 0,))
        self.surf.blit(self.textSurf, [self.w/2 - self.textSurf.get_width()/2, self.h/2 - self.textSurf.get_height()/2])
        self.pos = vec(1920-self.w, 1080 -  (ord(self.note_name[0])-60)*self.h)
        self.rect = self.surf.get_rect()

        
    def update(self):
        self.pos += vec(-4, 0)
        self.rect.midbottom = self.pos
        
class Deadzone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.w = 40
        self.h = 1080
        self.surf = pygame.Surface((self.w, self.h))
        self.surf.fill((128,255,40))
        self.pos = vec(40, 1080)
        self.rect = self.surf.get_rect()