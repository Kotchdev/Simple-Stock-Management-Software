
import customtkinter
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title('Login')
app.attributes('-fullscreen',True)
app.config(bg='#001220')

font1 = ('Helvetica',25,'bold')
font2 = ('Arial',17,'bold')
font3 = ('Arial',13,'bold')
font4 = ('Arial',13,'bold','underline')

# Will annotate later
global frame1, username_entry2, password_entry2
frame1, username_entry2, password_entry2 = None, None, None
global frame2

conn = sqlite3.connect('tree_crm.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
               username VARCHAR(20) NOT NULL PRIMARY KEY,
               password VARCHAR(20) NOT NULL)''')

def signup():
    username = username_entry2.get()
    password = password_entry2.get()
    if username != '' and password != '':
        cursor.execute('SELECT username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', 'Username already exists.')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            
            cursor.execute('INSERT INTO users VALUES (?, ?)', [username,hashed_password])
            conn.commit()
            messagebox.showinfo('Success', 'Account has been created.')
    else:
        messagebox.showerror('Error','Enter all data')
    
def login_account():
    global username
    username = username_entry1.get()
    password = password_entry1.get()
    if username != '' and password != '':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                messagebox.showinfo('Success', 'Logged in successfully.')
                
                app.destroy()

                from Stocks_Page import main
                main(username)
            else:
                messagebox.showerror('Error', 'Invalid password.')
        else:  
            messagebox.showerror('Error', 'Invalid username.')
    else:
        messagebox.showerror('Error', 'Invalid Enter all data.')

def login():
    
    if frame1:
        frame1.destroy()
    global frame2
    frame2 = customtkinter.CTkFrame(app,bg_color='#001220',fg_color='#001220',width=1920,height=1080)
    frame2.place(x=0,y=0)

    login_label1 = customtkinter.CTkLabel(frame2, font=font1, text='Welcome to Emrex SMS',text_color='#fff', bg_color='#001220')
    login_label1.place(x=580,y=200)

    global username_entry1
    global password_entry1

    username_entry1 = customtkinter.CTkEntry(frame2, font=font2, text_color='#fff',fg_color='#001a2e',bg_color='#121111',border_color='#004780', border_width=3,placeholder_text='Username',placeholder_text_color='#a3a3a3', width=250, height=60)
    username_entry1.place(x=600,y=290)

    password_entry1 = customtkinter.CTkEntry(frame2, font=font2, show="*", text_color='#fff',fg_color='#001a2e',bg_color='#121111',border_color='#004780',border_width=3,placeholder_text='Password',placeholder_text_color='#a3a3a3',width=250,height=60)
    password_entry1.place(x=600, y=370)

    login_button1 = customtkinter.CTkButton(frame2, command = login_account ,font = font2,text_color='#fff',text='Log in',fg_color = '#00965d',hover_color='#006e44', bg_color='#121111',cursor = 'hand2', corner_radius=5,height = 35, width=120)
    login_button1.place(x=665,y=450)

    signup_label = customtkinter.CTkLabel(frame2, font=font3,text="Don't have an account?", text_color='#fff',bg_color='#001220')
    signup_label.place(x=620,y=500)

    signup_button = customtkinter.CTkButton(frame2, command = sign_up   ,font=font4, text_color='#00bf77',text='Signup',fg_color='#001220', hover_color='#001220',cursor='hand2',width=40)
    signup_button.place(x=770,y=500)

def sign_up():
    global frame1, username_entry2, password_entry2
    if 'frame2' in globals() and frame2:
        frame2.destroy()

    frame1 = customtkinter.CTkFrame(app,bg_color='#001220',fg_color='#001220',width=1920,height=1080)
    frame1.place(x=0,y=0)

    signup_label = customtkinter.CTkLabel(frame1, font=font1, text='Sign Up', text_color='#fff',bg_color='#001220')
    signup_label.place(x=580,y=200)

    username_entry2 = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#001a2e',bg_color='#121111',border_color='#004780',border_width=3,placeholder_text='Username',placeholder_text_color = '#a3a3a3',width=250,height=60)
    username_entry2.place(x=600,y=290)

    password_entry2 = customtkinter.CTkEntry(frame1, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111',border_color='#004780',border_width=3,placeholder_text='Password',placeholder_text_color='#a3a3a3',width=250,height=60)
    password_entry2.place(x=600,y=370)

    signup_button = customtkinter.CTkButton(frame1,command=signup,font=font2, text_color='#fff', text='Sign up', fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,height=35,width=120)
    signup_button.place(x=665,y=450)

    login_label2 = customtkinter.CTkLabel(frame1, font=font3, text='Already have an account?', text_color='#fff',bg_color='#001220')
    login_label2.place(x=620,y=500)

    login_button = customtkinter.CTkButton(frame1, command = login,font=font4, text_color='#00bf77',text='Login',fg_color='#001220', hover_color='#001220',cursor='hand2',width=40)
    login_button.place(x=780,y=500)

    app.update()    

login()
app.mainloop()
conn.close()

