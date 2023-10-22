import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

from backend.db.Database import Database


#Rename file to data_entry
class CreateReferendumFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)


        def enter_data():
            name_institution = name_institution_Entry.get()
            title_referendum = title_referendum_Entry.get()
            description = Description_Entry.get()
            num_candidates = No_Cand_Entry.get() 
            #date_referendum = Date_Entry.get()
            number_voter = No_Voter_Entry.get()
            security_key = Sec_Key_Entry.get()
            tnc = tnc_var.get()
            min_threshold  = Min_thr_Key_Entry.get()
            Alpha = 0
            l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
            try:
                int(num_candidates)
                Alpha += 1
            except ValueError:
                l[0] = 1
            try:
                int(number_voter)
                Alpha += 1
            except ValueError:
                l[1] = 1
            if len(security_key) >= 8:
                Alpha += 1
            else:
                l[2] = 1
            if title_referendum and description :
                Alpha += 1
            else:
                l[3] = 1
            if tnc == 'Checked':
                Alpha += 1
            else:
                l[4] = 1
            try:
                int(min_threshold)
                if int(min_threshold) == 0:
                    min_threshold = None
            except:
                l[5] = 1
            Data_Entry = {"Name": name_institution,
                          "title_elec": title_referendum, "desc": description, "Num_voter": number_voter,
                          "Num_can": num_candidates, "Sec_key": security_key,
                          "tnc": tnc}

            if l[0] == 1:
                tkinter.messagebox.showerror(title="Erroe101", message='Number of Candidataes must be integer')
            elif l[1] == 1:
                tkinter.messagebox.showerror(title="Error102", message='Number of Voters Must be integer')
            elif l[2] == 1:
                tkinter.messagebox.showerror(title="Error103", message='Security Key must be atleast 8 digit long')
            elif l[3] == 1:
                tkinter.messagebox.showerror(title="Error104",
                                             message='Title , Description and Date of referendum Required')
            elif l[5] == 1:
                tkinter.messagebox.showerror(title="Error105", message="You have selected invalid minimum threshold")
            elif l[4] == 1:
                tkinter.messagebox.showerror(title="Error106", message="You have not accepted the Terms and Condition")
            else:
                # save to db
                try:
                    db = Database.get_instance()
                    poll = db.create_poll(name=title_referendum, type='referendum', description=description,
                                          security_key=security_key, secure_mode=True, inst_name=name_institution,
                                          num_candidates=num_candidates, num_voters=number_voter,
                                          min_threshold=min_threshold)
                    app.show_frame('ref_entry', context={'poll': poll})
                except Exception as exc:
                    print(exc)
                    tkinter.messagebox.showerror(title='Error109', message=str(exc))
                finally:
                    return Data_Entry



        self.frame = ttk.Frame(self)
        self.frame.pack()

        User_info_frame = ttk.LabelFrame(self.frame, text="User Informaton")
        User_info_frame.grid(row=0, column=0, sticky="news")

        name_institution = ttk.Label(User_info_frame, text="Name of the institution")
        name_institution.grid(row=0, column=0)
        name_institution_Entry = ttk.Entry(User_info_frame)
        name_institution_Entry.grid(row=0, column=1, padx=50, pady=10)



        referendum_info_frame = ttk.LabelFrame(self.frame, text="Referendum Information")
        referendum_info_frame.grid(row=1, column=0, sticky="news")

        title_referendum = ttk.Label(referendum_info_frame, text="Title of Referendum")
        title_referendum_Entry = ttk.Entry(referendum_info_frame)
        title_referendum.grid(row=0, column=0)
        title_referendum_Entry.grid(row=0, column=1, padx=50, pady=10)


        Description = ttk.Label(referendum_info_frame, text="Description of Referendum")
        Description.grid(row=1, column=0)
        Description_Entry = ttk.Entry(referendum_info_frame)
        Description_Entry.grid(row=1, column=1, padx=50, pady=10)

        No_Cand = ttk.Label(referendum_info_frame, text="Number of Proposals")
        No_Cand.grid(row=2, column=0)
        No_Cand_Entry = ttk.Entry(referendum_info_frame)
        No_Cand_Entry.grid(row=2, column=1, padx=50, pady=10)

        #Date = ttk.Label(referendum_info_frame, text="Date")
        #Date.grid(row=3, column=0)
        #Date_Entry = ttk.Entry(referendum_info_frame)
        #Date_Entry.grid(row=3, column=1, padx=50, pady=10)

        No_Voter = ttk.Label(referendum_info_frame, text="Number of  Voters")
        No_Voter.grid(row=4, column=0)
        No_Voter_Entry = ttk.Entry(referendum_info_frame)
        No_Voter_Entry.grid(row=4, column=1, padx=50, pady=10)

        Sec_Key = ttk.Label(referendum_info_frame, text="Security Key")
        Sec_Key.grid(row=5, column=0)
        Sec_Key_Entry = ttk.Entry(referendum_info_frame)
        Sec_Key_Entry.grid(row=5, column=1, padx=50, pady=10)

        Min_thr_Key = ttk.Label(referendum_info_frame, text="Minimum Approval Threshold(%)")
        Min_thr_Key.grid(row=6, column=0)
        Min_thr_Key_Entry = ttk.Spinbox(referendum_info_frame , from_= 0 , to= 100)
        Min_thr_Key_Entry.grid(row=6, column=1, padx=50, pady=10)



        Dec_frame = ttk.LabelFrame(self.frame, text="Declaration")
        Dec_frame.grid(row=2, column=0, sticky="news")
        terms_and_conditions = ''
        with open('frontend/tos.txt') as file:
            terms_and_conditions = file.read()

        Dec_tnc = ttk.Label(Dec_frame, text="Terms and Condition Declaration")
        tnc_var = tk.StringVar(value="Uncheked")

        def Show_tnc():
            tkinter.messagebox.showinfo(message=terms_and_conditions)

        Dec_tnc_Button = ttk.Button(Dec_frame, text="Show T&C", command=Show_tnc)
        Dec_tnc_Button.grid(row=2, column=0, padx=50)
        Dec_tnc.grid(row=1, column=0)
        Dec_tnc_CB = ttk.Checkbutton(Dec_frame, text="I accept all the T&C", variable=tnc_var,
                                     onvalue="Checked", offvalue="Uncheked")
        Dec_tnc_CB.grid(row=1, column=1, padx=50, pady=10)

        button1 = ttk.Button(self.frame, text="Submit", command=enter_data)
        button1.grid(row=3, column=0, sticky='news', padx=10
                   , pady=10)

        button1 = ttk.Button(self.frame, text="Submit", command=enter_data)
        button1.grid(row=3, column=0, sticky='news', padx=10
                     , pady=10)
        Button_frame = ttk.LabelFrame(self.frame)
        Button_frame.grid(row=4, column=0, sticky="news")
        for i in range(3):
            Button_frame.grid_columnconfigure(i, weight=1)

        def Help():
            tkinter.messagebox.showinfo(title="Help", message="Take Data from Documentation")

        button_1 = ttk.Button(Button_frame, text="Help", command=Help)
        button_1.grid(row=0, column=0, sticky='news', padx=10
                     , pady=10)
        button_2 = ttk.Button(Button_frame, text="Go Back", command=app.show_frame_factory('opening'))
        button_2.grid(row=0, column=2, sticky='news', padx=10
                     , pady=10)