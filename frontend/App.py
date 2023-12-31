import os.path
import platform
import tkinter as tk
import tkinter.ttk as ttk
from .opening_page import OpeningPageFrame
from .credits import CreditsFrame
from .help import Helpframe
from .create_election import CreateElectionFrame
from .candidate_entry import CandidateEntryFrame
from .start_election import StartElectionFrame
from .election_navigation_page import TreeViewNavigationFrame
from .voting_window import VotingWindow
from .voting_security_check import VotingSecurityCheckFrame
from .result_page import ResultFrame
from .create_referendum import CreateReferendumFrame
from .referendum_entry_frame import ReferendumEntryFrame
class App(tk.Tk):
    frames_data = {
        'opening': {'title': 'Main Page', 'frame': OpeningPageFrame},
        'credits': {'title': 'Credits', 'frame': CreditsFrame},
        'help' : {'title' : 'Help??', 'frame' : Helpframe},
        'cre_elec': {'title' : 'Create election' , 'frame' : CreateElectionFrame},
        'cand_entry' : {'title' : 'Enter Candidates' , 'frame' : CandidateEntryFrame},
        'start_election': {'title': 'Start Election', 'frame': StartElectionFrame},
        'voting_window' : {'title': 'Voting Window', 'frame': VotingWindow},
        'voting_security_check' : {'title': 'Security check', 'frame': VotingSecurityCheckFrame},
        'result_page': {'title': 'Result', 'frame': ResultFrame},
        'create_ref': {'title': 'Create Referendum', 'frame': CreateReferendumFrame},
        'elec_navigation': {'title': 'Election Navigation Frame', 'frame': TreeViewNavigationFrame},
        'ref_entry': {'title': 'Referendum Entry Frame', 'frame': ReferendumEntryFrame}

    }

    def __init__(self):
        super().__init__()
        print('App created')
        self.title('Poll Pilot')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.current_frame_name = 'opening'
        self.current_frame = None

        # set theme
        style = ttk.Style()
        if platform.system() == 'Linux':
            print('applying clam')
            style.theme_use('clam')

        # set icon
        photo = tk.PhotoImage(file='icon.png')
        self.wm_iconphoto(False, photo)
        # show main page
        self.show_frame('opening')

    def show_frame(self, frame_name, context = None):
        function = self.show_frame_factory(frame_name, context)
        function()

    def show_frame_factory(self, frame_name, context=None):
        def show_function():
            print(f'Showing {frame_name}...')
            # Remove current frame
            self.current_frame = None

            frame = App.frames_data[frame_name]['frame'](self, context)
            frame.grid(row=0, column=0, sticky='news')
            self.current_frame = frame

            self.title('Poll Pilot - ' + App.frames_data[frame_name]['title'])
            self.current_frame_name = frame_name
        return show_function

def start_application():
    app = App()
    app.mainloop()