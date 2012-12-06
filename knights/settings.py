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

import sys

if sys.version_info[0] < 3:
    from yaml.lib import yaml
else:
    from yaml.lib3 import yaml

settings_file = open("settings.yaml","r").read()
settings = yaml.load(settings_file)

GAME            = settings['game']
FREEMODE        = settings['freemode']
CLICKTOCONTINUE = settings['clickToContinue']
SCOREMODE       = settings['scoremode']
TIMESAVEMODE    = settings['timesavemode']
BOARD           = settings['board']
SIDEBAR         = settings['sidebar']
BUTTON          = settings['button']
PYGAME_FIELD    = settings['pygame-field']
GAMEBOARD_LOGIC = settings['gameboard-logic']
SCOREBOX        = settings['scorebox']
TIMEBOX         = settings['timebox']
LEVELBOX        = settings['levelbox']
TEXTBOX         = settings['textbox']
MAINMENU        = settings['mainmenu']
SELECTHIGHSCORE = settings['selecthighscore']
HIGHSCORE       = settings['highscore']
