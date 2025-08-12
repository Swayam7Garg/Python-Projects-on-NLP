from tkinter import * 
from mydb import Database
from tkinter import messagebox
from myapi import Api

class NLPapp:

    def __init__(self):

        # create db object
        self.dbo = Database()
        self.api = Api()

        #To load the gui for login
        self.root = Tk()#object of Tk class 
        self.root.title('NLPApp')
        self.root.iconbitmap(r"NLP-gui-tool\resources\fav.ico")
        self.root.configure(bg='#34495E')
        self.root.geometry('350x600')

        self.login_gui()
        self.root.mainloop()#mainloop is used to hold the gui 


    def login_gui(self):

        self.clear()

        heading = Label(self.root,text ='NLPApp',bg= '#34495E' ,fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text = 'Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width = 50)
        self.email_input.pack(pady = (5,10),ipady = 4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width = 50 , show = '*')
        self.password_input.pack(pady = (5,10) ,ipady = 4)

        login_btn = Button(self.root,text = 'Login',command = self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root,text='Not a member?')
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root,text = 'Register Now',command = self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root,text = 'NLPApp',bg= '#34495E' ,fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label0= Label(self.root,text = 'Enter Name')
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root,width = 50)
        self.name_input.pack(pady = (5,10),ipady = 4)

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width = 50)
        self.email_input.pack(pady = (5,10),ipady = 4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width = 50 ,show = '*')
        self.password_input.pack(pady = (5,10) ,ipady = 4)

        register_btn = Button(self.root,text = 'Register',height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3 = Label(self.root,text='Already a member?')
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root,text = 'Login Now',command = self.login_gui)
        redirect_btn.pack(pady=(10,10))


    def clear(self):
        #clear the exisiting gui
        for i in self.root.pack_slaves():
            print(i.destroy())

    def perform_registration(self):
        #fetch data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password= self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration successful , you can login now')
        else:
            messagebox.showerror('Error','Email Already Exist')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email , password)

        if response:
            messagebox.showinfo('success','Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect email/password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root,text = 'NLPApp',bg= '#34495E' ,fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4, command=self.ner_gui) 
        ner_btn.pack(pady=(10, 10))

        lang_deta_btn = Button(self.root, text='Language Detection', width=30, height=4, command=self.ld_gui)  
        lang_deta_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Log Out', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root,text = 'NLPApp',bg= '#34495E' ,fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        heading2 = Label(self.root,text = 'Sentiment Analysis',bg= '#34495E' ,fg='white')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter the text')
        label1.pack(pady=(10,10))

        self.sentiment_input = Entry(self.root,width = 50)
        self.sentiment_input.pack(pady = (5,10),ipady = 4)

        sentiment_btn = Button(self.root , text = 'Analyze Sentiment',width = 30 , height = 4,command = self.do_sentiment_analysis )
        sentiment_btn.pack(pady=(10 , 10))

        self.sentiment_result = Label(self.root,text='',bg= '#34495E' ,fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana',16))


        goback_btn = Button(self.root , text = 'Go Back',width = 30 , height = 4,command = self.home_gui)
        goback_btn.pack(pady=(10 , 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        if not text.strip():
            self.sentiment_result.config(text="Please enter some text")
            return
        result = self.api.sentiment_analysis(text)  # ✅ fixed (self.api instead of self.apio)
        self.sentiment_result.config(text=str(result))

    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text='Named Entity Recognition', bg='#34495E', fg='white')
        heading.pack(pady=(30, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(
            self.root, text='Run NER', width=30, height=2,
            command=self.do_ner
        )
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', width=30, height=2, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))


    def do_ner(self):
        text = self.ner_input.get()
        if not text.strip():
            self.ner_result.config(text="Please enter some text")
            return
        result = self.api.ner(text)  # ✅ fixed (self.api instead of self.apio)
        self.ner_result.config(text=str(result))

    def ld_gui(self):
        self.clear()
        heading = Label(self.root, text='Named Entity Recognition', bg='#34495E', fg='white')
        heading.pack(pady=(30, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.ld_input = Entry(self.root,width = 50)
        self.ld_input.pack(pady = (5,10),ipady = 4)

        ld_btn = Button(
            self.root, text='Run Language Detection', width=30, height=2,
            command=self.do_ld
        )
        ld_btn.pack(pady=(10, 10))
                    
        self.ld_result = Label(self.root,text='',bg= '#34495E' ,fg='white')
        self.ld_result.pack(pady=(10,10))
        self.ld_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='Go Back', width=30, height=2, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_ld(self):
        text = self.ld_input.get()
        if not text.strip():
            self.ld_result.config(text="Please enter some text")
            return
        result = self.api.language_detection(text) 
        self.ld_result.config(text=str(result))

nlp = NLPapp() 