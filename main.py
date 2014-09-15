#the last thing I was working on was the thing where I have a dictionary of things and
#I also have a list of things, complementary, may or may ot be necessary, actually maybe unique
from kivy.app import App

from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ListProperty

from sets import settings_json
from random import choice,randint

class Practitioner(FloatLayout):
#have a reference to screen manager .mang

    bucket = ListProperty()

    curr_chord = StringProperty()

    keys = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab']
    modifiers = ['maj7', 'min7', 'susb9', 'maj#4', '7', 'minb6', 'halfdim', 'sus']

    welcome = StringProperty()

    practice_state = NumericProperty()

    state_text = StringProperty()

    lick_text = StringProperty()

    states = ['Play the scale that goes with this chord.', 'Arpeggiate the scale. (1,3,5,7,9)', 'Play a lick using these scale degrees:'] 

    def update_practice_state(self):
        if self.practice_state == 2:
            rtex = ""
            for i in range(5): 
                rtex += str(randint(1,9)) + " "
            rtex += str(choice([1,3,5,8]))
            self.lick_text = rtex
                
        if self.practice_state > 2:
            self.mang.current = 'rate'

        else:
            self.state_text = self.states[self.practice_state]

    def reset_practice_state(self):
        self.practice_state = 0
        self.lick_text = ''
        self.update_practice_state()

    def increment_practice_state(self):
        if self.practice_state < len(self.states):
            self.practice_state += 1
        
        
        


    def get_next(self):
        chord = choice(self.bucket)
        print(chord)
        self.curr_chord = chord
        return chord

    def get_notebooks(self):
        res = ["math", "drugs","science", "history", "CS", "liguistics"]
        return res

    def lame(self):
        print("yeah")

    def list_notebooks(self):
        notes = self.get_notebooks()
        with self.canvas:
            layout = GridLayout(rows = len(notes))
            layout.size = self.size
            for note in notes:
                bot = Button(text=note,pos_hint_x = .7, width=100)
                bot.bind(on_press=self.lame)
                layout.add_widget(bot)


class Interface(App):

    progress = NumericProperty()

    keys = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab']
    modifiers = ['maj7', 'min7', 'susb9', 'maj#4', '7', 'minb6', 'halfdim', 'sus']

    def update_curr_chord(self,chord,value):
        self.config.set('major_harmony',chord,value)
        self.config.write()
        self.update_bucket()

    def update_bucket(self):
        rating_max = 4
        bucket = []
        for key in self.keys:
            for modifier in self.modifiers:
                chord = "{0}_{1}".format(key,modifier)
                rating = int(self.config.get('major_harmony',chord))
                weight = rating_max - rating
                for repetition in range(weight):
                    bucket.append(chord)
        self.Instance.bucket = bucket
        for i in bucket:
            self.progress += 1
            print(i)
        print(self.progress)

    def build(self):
        self.progress = 1
        self.Instance = Practitioner()
        self.update_bucket()
        return self.Instance
    
    def build_config(self,config):
        #this is ether really ugly, or really beautiful
        combinations = ""
        for key in self.keys:
            for modifier in self.modifiers:
                combinations += "'{0}_{1}': 0, ".format(key,modifier)
        exec( "config.setdefaults('major_harmony', {" + combinations + "})" )

if __name__ == '__main__':
    Interface().run()
