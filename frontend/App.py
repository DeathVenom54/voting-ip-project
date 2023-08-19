import tkinter as tk
import tkinter.ttk as ttk
from .opening_page import OpeningPageFrame
from .credits import CreditsFrame
from .help import Helpframe
from .ftpt_de import ele_de_frame

class App(tk.Tk):
    frames_data = {
        'opening': {'title': 'Main Page', 'frame': OpeningPageFrame},
        'credits': {'title': 'Credits', 'frame': CreditsFrame},
        'help' : {'title' : 'Help??', 'frame' : Helpframe},
        'cre_elec': {'title' : 'Create election' , 'frame' : ele_de_frame}
    }

    def __init__(self):
        super().__init__()
        print('App created')
        self.title('Poll Pilot')
        self.geometry('500x450')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.loaded_frames = {}

        # instantiate all frames
        for (name, frame) in App.frames_data.items():
            self.loaded_frames[name] = frame['frame'](self)
            self.loaded_frames[name].grid(row=0, column=0, sticky='news')

        # show main page
        self.show_frame('opening')

    def show_frame(self, frame_name):
        print(f'Showing {frame_name}...')
        self.title('Poll Pilot - ' + App.frames_data[frame_name]['title'])
        frame = self.loaded_frames[frame_name]
        frame.tkraise()

    def show_frame_factory(self, frame_name):
        def show():
            print(f'Showing {frame_name}...')
            self.title('Poll Pilot - ' + App.frames_data[frame_name]['title'])
            frame = self.loaded_frames[frame_name]
            frame.tkraise()
        return show

def start_application():
    app = App()
    app.mainloop()