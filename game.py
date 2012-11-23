import pygame

from settings import GAME
from common import nice_print

from mainmenu_mode import Mainmenu
from score_mode import Scoremode
from clicktocontinue_mode import ClickToContinue
from highscore_mode import Highscore

class Game(object):
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode(GAME['resolution'])
        pygame.display.set_caption(GAME['caption'])
        self.clock = pygame.time.Clock()
        self.timeinterval = GAME['fps-limit']

        self.mode = Mainmenu(self.screen.get_size())

    def loop(self):
        while 1:
            self.handle_button_clicks()

            self.modeswitch(self.mode.done())
            self.events()

            self.blit()
            self.update()

            pygame.display.flip()
            self.clock.tick(self.timeinterval)

    def handle_button_clicks(self):
        if self.mode.name == "Scoremode":
            buttons = self.mode.button_clicked()
            for name in buttons:
                if name == "quit":
                    nice_print(["Game.handle_button_clicks:",
                                "'quit' clicked: exiting"])
                    exit()
                elif name == "restart":
                    self.mode = Scoremode(1,self.screen.get_size())

                elif name == "pause":
                    self.mode.set_pause()

                elif name == "main_menu":
                    self.mode = Mainmenu(self.screen.get_size())

        elif self.mode.name == "Mainmenu":
            buttons = self.mode.button_clicked()
            for name in buttons:
                if name == "scoremode":
                    self.mode = Scoremode(1,self.screen.get_size())
                elif name == "exit":
                    nice_print(["Game.handle_button_clicks:",
                                "'quit' clicked: exiting"])
                    exit()
                elif name == "highscore":
                    self.mode = Highscore(self.screen.get_size())

    def blit(self):
        if self.mode.changed:
            nice_print(["Mode {!r} changed:".format(self.mode.name),
                        "Blitting on screen\n"])
            self.screen.blit(self.mode.background,(0,0))


    def update(self):
        self.mode.update()

    def events(self):
        for i in pygame.event.get():
            if i.type==pygame.QUIT or i.type==pygame.KEYDOWN and i.key==pygame.K_ESCAPE:
                exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                self.mode.mousedown(i.pos)

    def modeswitch(self,done): # done is tuple with necessary information
        if done:
            self.blit()
            self.mode.update()
            self.blit()
            newmode = done[0]
            if newmode == "freemode":
                self.mode = Freemode(done[1],self.screen.get_size())
            elif newmode == "scoremode":
                self.mode = Scoremode(done[1],self.screen.get_size(),done[2])
            elif newmode == "clicktocontinue":
                self.mode = ClickToContinue(done[1],
                                            self.screen.get_size(),
                                            done[2])
            elif newmode == "clicktocontinue_scoremode_loss":
                self.mode = ClickToContinue(done[1],
                                            self.screen.get_size(),
                                            done[2],
                                            wait=700)
            elif newmode == "mainmenu":
                self.mode = Mainmenu(self.screen.get_size())
            else:
                print newmode
                print "No matching mode"



if __name__ == "__main__":
    g = Game()
    g.loop()
