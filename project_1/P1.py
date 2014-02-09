# -*- coding: iso-8859-1 -*-

# Name:             Project 1
# Purpose:          CSC 4243
# Author:           Benjamin K Guitreau
# Copyright:
# Licence:          GPL

# OS dev:           Windows 7
# Python dev:       2.7
# Revision:         1.00

# Dependencies:     Python 2.7 32-bit, Kivy 1.5.1

import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.widget import Widget

Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Label:
            text: 'Louisana Heritage\\n   Food and Film'
            font_size: 30
            size_hint: .25, .25
            pos: 288, 822

        Button:
            text: 'Film'
            on_press: root.manager.current = 'filmMain'
            size_hint: .25, .05
            pos: 96, 30

        Button:
            text: 'Food'
            on_press: root.manager.current = 'foodMain'
            size_hint: .25, .05
            pos: 480, 30

        Button:
            text: 'Quit'
            on_press: exit()
            size_hint: .06, .04
            pos: 720, 972

        Button:
            text: 'Map'
            on_press: root.manager.current = 'map'
            size_hint: .06, .04
            pos: 4, 972

        Image:
            source: 'louisiana.png'
            size_hint: 1,1
            pos: 16,48

        Image:
            source: 'text.png'
            size_hint: 1,1
            pos: 16, 48

<FilmMainScreen>:
    FloatLayout:
        Label:
            text: 'Film'
            font_size: 30
            size_hint: .25, .25
            pos: 288, 822

        Button:
            text: 'Food'
            on_press: root.manager.current = 'foodMain'
            size_hint: .25, .05
            pos: 96, 30

        Button:
            text: 'Home'
            on_press: root.manager.current = 'mainMenu'
            size_hint: .25, .05
            pos: 480, 30

        Button:
            text: 'Looper'
            on_press: root.manager.current = 'looper'
            size_hint: .168, .03
            pos: 220, 600

        Button:
            text: 'Fake'
            on_press: root.manager.current = 'looper'
            size_hint: .168, .03
            pos: 420, 600

        Button:
            text: 'Fake'
            on_press: root.manager.current = 'looper'
            size_hint: .168, .03
            pos: 220, 400

        Button:
            text: 'Fake'
            on_press: root.manager.current = 'looper'
            size_hint: .168, .03
            pos: 420, 400

        Button:
            text: 'Quit'
            on_press: exit()
            size_hint: .06, .04
            pos: 720, 972

        Button:
            text: 'Map'
            on_press: root.manager.current = 'map'
            size_hint: .06, .04
            pos: 4, 972

<MovieScreen>:
    FloatLayout:
        Label:
            text: 'Film'
            font_size: 30
            size_hint: .25, .25
            pos: 288, 822

        Button:
            text: 'Food'
            on_press: root.manager.current = 'foodMain'
            size_hint: .25, .05
            pos: 96, 40

        Button:
            text: 'Home'
            on_press: root.manager.current = 'mainMenu'
            size_hint: .25, .05
            pos: 480, 40

        Button:
            text: 'Quit'
            on_press: exit()
            size_hint: .06, .04
            pos: 720, 972

        Button:
            text: 'Map'
            on_press: root.manager.current = 'map'
            size_hint: .06, .04
            pos: 4, 972

        VideoPlayer:
            source: 'looper.mpg'
            size_hint: .75, .75
            pos: 96, 128

<FoodMainScreen>:
    FloatLayout:
        Label:
            text: 'Louisiana\\n    Food'
            font_size: 30
            size_hint: .25, .25
            pos: 288, 822

        Button:
            text: 'Film'
            on_press: root.manager.current = 'filmMain'
            size_hint: .25, .05
            pos: 96, 30

        Button:
            text: 'Home'
            on_press: root.manager.current = 'mainMenu'
            size_hint: .25, .05
            pos: 480, 30

        Button:
            text: 'Gumbo'
            on_press: root.manager.current = 'recipes'
            size_hint: .168, .03
            pos: 320, 680

        Button:
            text: 'Jambalaya'
            on_press: root.manager.current = 'recipes'
            size_hint: .168, .03
            pos: 320, 580

        Button:
            text: 'Dessert'
            on_press: root.manager.current = 'recipes'
            size_hint: .168, .03
            pos: 320, 480

        Button:
            text: 'Quit'
            on_press: exit()
            size_hint: .06, .04
            pos: 720, 972

        Button:
            text: 'Map'
            on_press: root.manager.current = 'map'
            size_hint: .06, .04
            pos: 4, 972

<RecipesScreen>:
    FloatLayout:
        Label:
            text: 'Louisiana\\n    Food'
            font_size: 30
            size_hint: .25, .25
            pos: 288, 822

        Button:
            text: 'Film'
            on_press: root.manager.current = 'filmMain'
            size_hint: .25, .05
            pos: 96, 30

        Button:
            text: 'Home'
            on_press: root.manager.current = 'mainMenu'
            size_hint: .25, .05
            pos: 480, 30

        Image:
            source: 'creole_gumbo.png'
            size_hint: 1, 1
            pos: 4, 60

        Button:
            text: 'Quit'
            on_press: exit()
            size_hint: .06, .04
            pos: 720, 972

        Button:
            text: 'Map'
            on_press: root.manager.current = 'map'
            size_hint: .06, .04
            pos: 4, 972

<MapScreen>:
    FloatLayout:
        Label:
            text: 'Louisiana\\n   Regions'
            font_size: 30
            size_hint: .25, .25
            pos: 288, 822

        Button:
            text: 'Film'
            on_press: root.manager.current = 'filmMain'
            size_hint: .25, .05
            pos: 96, 30

        Button:
            text: 'Food'
            on_press: root.manager.current = 'foodMain'
            size_hint: .25, .05
            pos: 480, 30

        Button:
            text: 'Quit'
            on_press: exit()
            size_hint: .06, .04
            pos: 720, 972

        Button:
            text: 'Home'
            on_press: root.manager.current = 'mainMenu'
            size_hint: .06, .04
            pos: 4, 972

    BoxLayout:
        size_hint: .65, .65
        size: .65, .65
        pos: 112, 192

        ScrollView:
            size_hint: (1,1)

            Image:
                size_hint: (None,None)
                source: 'Louisiana_regions_map.png'
                size: self.texture_size
                bar_color: .8, .8, .3, .9
                bar_width: 36
                bar_margin: 6
                scroll_stoptime: 50
""")

''' For future use
        Slider:
            min: 0
            max: 100
            step: 5
            pos: 96, 96
            size_hint: .75, .05
'''
class MenuScreen(Screen):
    pass

class FilmMainScreen(Screen):
    pass

class FoodMainScreen(Screen):
    pass

class RecipesScreen(Screen):
    pass

class MovieScreen(Screen):
    pass

class MapScreen(Screen):
    print 'in maps'

sm = ScreenManager()
sm.add_widget(MenuScreen(name='mainMenu'))
sm.add_widget(FilmMainScreen(name='filmMain'))
sm.add_widget(FoodMainScreen(name='foodMain'))
sm.add_widget(RecipesScreen(name='recipes'))
sm.add_widget(MovieScreen(name='looper'))
sm.add_widget(MapScreen(name='map'))

class Application(App):
    def build(self):
        return sm

if __name__ == '__main__':
    Application().run()
