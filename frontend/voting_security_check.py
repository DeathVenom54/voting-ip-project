import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import traceback

from backend.calculate_result import calculate_result
from backend.db.Database import Database


# for easy access cand_entry is in referendum

class VotingSecurityCheckFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        poll = context['poll']
        sec_key = poll['security_key']
        # sec_key = 'password'

        def next_vote():
            ent_password = entry1.get()

            if ent_password == sec_key:
                app.show_frame('voting_window', {'poll': poll})
            else:
                tkinter.messagebox.showerror(title= "error" , message= "Security key is incorrect")

        def terminate_election():
            ent_password = entry1.get()

            if ent_password == sec_key:
                # generate result
                try:
                    db = Database.get_instance()
                    result = calculate_result(poll['id'])
                    print(result)
                    db.mark_as_completed(poll['id'])
                    app.show_frame('result_page', {'poll': poll})
                except Exception as exc:
                    traceback.print_exc()
                    tk.messagebox.showerror(message=str(exc))
            else:
                tkinter.messagebox.showerror(title="error", message="Security key is incorrect")

        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(1):
            self.grid_columnconfigure(i, weight=1)

        self.frame = tk.Frame(self)
        self.frame.grid()



        label1 = tk.Label(self.frame, text="Vote Has been registered" , font= 20)
        label1.grid(row=0, column=0 , pady= 10)

        label2 = tk.Label(self.frame, text="Enter Security Key to Continue")
        label2.grid(row=1, column=0,  pady= 10)
        entry1 = tk.Entry(self.frame, show='*')
        entry1.grid(row=2, column=0)

        def show_and_hide():
            if entry1['show'] == '*':
                entry1['show'] = ''
            else:
                entry1['show'] = '*'

        checkBox_showPassword = tk.Checkbutton(self.frame, text="show password", fg='red',
                                             command=show_and_hide)
        checkBox_showPassword.grid(row=3,column=0)

        start_button = tk.Button(self.frame, text="Next Vote", command = next_vote)
        start_button.grid(row=4, column=0 ,  pady= 10)

        terminate_button = tk.Button(self.frame, text="Terminate", command=terminate_election)
        terminate_button.grid(row=5, column=0, pady=10)

        Button_frame = ttk.LabelFrame(self.frame)
        Button_frame.grid(row=6, column=0, sticky="news")
        for i in range(3):
            Button_frame.grid_columnconfigure(i, weight=1)

        def Help():
            tkinter.messagebox.showinfo(title="Help", message="Take Data from Documentation")

        button1 = ttk.Button(Button_frame, text="Help", command=Help)
        button1.grid(row=0, column=0, sticky='news', padx=10
                     , pady=10)
        button1 = ttk.Button(Button_frame, text="Go Home", command=app.show_frame_factory('elec_navigation'))
        button1.grid(row=0, column=2, sticky='news', padx=10
                     , pady=10)
