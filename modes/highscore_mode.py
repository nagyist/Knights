"""
Copyright (C) 2012 Mattias Ugelvik

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""


from knights.settings import HIGHSCORE
from knights.scores import get_highscores
from knights.gui_elements import Textbox
import pygame

class Highscore(object):
    def __init__(self,screensize,gametype,title_prefix):
        self.name = "highscore"
        self.hasclicked = False
        self.width = screensize[0]
        self.background = pygame.Surface(screensize).convert()
        self.background.fill(HIGHSCORE['bgcolor'])
        self.changed = True
        highscores = get_highscores(HIGHSCORE['show-n-scores'],gametype=gametype)

        title = Textbox(
            name="highscore_title",
            size=HIGHSCORE['title-size'],
            location=(0,0),
            text_color=HIGHSCORE['title-text-color'],
            surface_color=HIGHSCORE['title-bgcolor'],
            text_size=HIGHSCORE['title-text-size'],
            bold=HIGHSCORE['title-bold'])
        title.update(title_prefix + HIGHSCORE['title-text'])

        score_boxes = []
        placement = 0

        for i in highscores:
            placement += 1
            highscore = Textbox(
                name="highscore_title",
                size=HIGHSCORE['score-size'],
                location=(0,0),
                text_color=HIGHSCORE['score-text-color'],
                surface_color=HIGHSCORE['score-bgcolor'],
                text_size=HIGHSCORE['score-text-size'],
                bold=HIGHSCORE['score-bold'],
                font=HIGHSCORE['score-font'])
            highscore.update(
                '{0:<2}'.format(str(placement))+HIGHSCORE['score-separator']+
                '{0:>15}'.format(str(i))
                )

            self.background.blit(highscore.surface,
                                 highscore.surface.get_rect(
                    centery=75+40*placement,
                    centerx=self.width/2
                    ))
            
        self.background.blit(title.surface,
                             title.surface.get_rect(
                centery=50,
                centerx=self.width/2
                ))


    def update(self):
        if self.changed:
            self.changed = False

    def mousedown(self,pos):
        self.hasclicked = True

    def mouseup(self,pos):
        pass

    def done(self):
        if self.hasclicked:
            return ("selecthighscore",'')
        else:
            return False
