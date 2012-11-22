#! /usr/bin/env python
import pygame
from pygame.locals import *
from gameboard_logic import Gameboard, Field
from settings import board_settings
from settings import pygame_field_settings

class PygameField(pygame.sprite.Sprite):
    def __init__(self,field_size,logicfield,field_representation):
        pygame.sprite.Sprite.__init__(self)
        self.logicfield = logicfield

        self.representation = field_representation

        self.changed = True
        self.image = pygame.Surface((field_size,field_size))

        self.error = 0
        self.errorlength = pygame_field_settings['error-length']

        self.update()
        self.rect = self.image.get_rect()

    def error_update(self):
        if self.error > 0:
            self.error -= 1
            if self.error == self.errorlength+1 or self.error == 0:
                self.changed = True

    def update(self):
        self.changed = False
        if self.error > 0:
            representation = self.representation["error"]
        else:
            representation = self.representation[self.logicfield.type]

        self.image.blit(representation,(0,0))


class Board(Gameboard):
    def __init__(self,width_height,size,field_offset=5):
        super(Board,self).__init__(size)
        self.pygame_fields = []
        self.wh = width_height
        box_size = (float(self.wh) / self.size)

        field_size = int(box_size-field_offset)+0

        load = lambda name: pygame.image.load(name)

        _open   = load(board_settings['open']).convert()
        knight  = load(board_settings['knight']).convert()
        visited = load(board_settings['visited']).convert()
        block   = load(board_settings['block']).convert()
        error   = load(board_settings['error']).convert()
        base    = load(board_settings['base'])

        img_name = [(_open,"open"),
                    (knight,"knight"),
                    (visited,"visited"),
                    (block,"block"),
                    (error,"error")]

        field_representation = {}
        for image, name in img_name:
            image.blit(base,(0,0))
            image = pygame.transform.scale(image,(field_size,field_size))
            field_representation[name] = image


        for field in self.board:
            coords = ((field.x-1)*box_size+field_offset,(field.y-1)*box_size+field_offset)
            tmpf = PygameField(int(box_size-field_offset),field,field_representation)
            tmpf.rect = tmpf.rect.move(coords[0],coords[1])
            self.pygame_fields.append(tmpf)

    def update_fields(self):
        for field in self.pygame_fields:
            field.update()

    def get_current_field(self):
        for field in self.pygame_fields:
            if field.logicfield.get_coords() == self.knight_pos:
                return field
        return False

    def fieldclick(self,coords):
        for field in self.pygame_fields:
            if field.rect.collidepoint(coords):
                old_field = self.get_current_field()
                newfield_type = self.move_knight(field.logicfield.get_coords())
                if not newfield_type: # If unvalid move
                    if field.logicfield.type in ["open","visited"]:
                        field.error = field.errorlength
                        field.changed = True
                    return False
                else:    # <- If it's a valid move and knight has moved
                    old_field.changed = True
                    field.changed = True
                    return newfield_type
