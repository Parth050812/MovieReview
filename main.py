from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image
import io

root = Tk()
root.title('Movie Reccomendation')
root.geometry('3180x1680')

root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.bind("<Insert>", lambda event: root.attributes('-fullscreen', True))
root.bind("<Escape>", lambda event: root.attributes('-fullscreen', False))

#database connection
conn = sqlite3.connect('moviep.db')  

c=conn.cursor()

#main label
MR = Label(root,text='Movie Reccomendation System',font=('Brush Script MT',60,'bold','underline')).place(x=400,y=20)


#exit button

def close_db(connection):
    connection.close()
    root.destroy()
    
exit_b=Button(root,text='Exit',bg='Dark Red',fg='White',borderwidth=5,font=('Times New Roman',20,'bold'),command = lambda: close_db(conn))
exit_b.place(x=1400,y=50)

#entry
m_entry = Entry(root,width=45,borderwidth=5,font=('Times New Roman',20))
m_entry.place(x=450,y=130)

#drop down
menu= StringVar()
menu.set('    Search By => ')
drop= OptionMenu(root, menu,'        Title      => ','Actor/Actress=>','     Director  => ','       Year      => ','     Rating     => ')
drop.config(borderwidth=5,font=('Times New Roman',20,'bold'))
drop.place(x=210,y=125)



#result frame
frame = LabelFrame(root,borderwidth=10)
frame.place(x=30, y=200, width=1060, height=650)

#frame into frame for title
frame_title=LabelFrame(frame,borderwidth=5)
frame_title.place(x=320,y=10,width=600,height=75)
title_label = Label(frame_title,text='#Title#',font=('Times New Roman',24,'bold','underline'))
title_label.pack(expand=True)

#frame into frame for year
frame_year=LabelFrame(frame,borderwidth=5)
frame_year.place(x=930,y=10,width=100,height=75)
year_label = Label(frame_year,text='#Year#',font=('Times New Roman',22,'bold'))
year_label.pack(expand=True)

#frame into frame for Rating
frame_rate=LabelFrame(frame,borderwidth=5)
frame_rate.place(x=800,y=95,width=230,height=200)
rate = Label(frame_rate,text='Rating',font=('Times New Roman',20,'bold')).pack(expand=True)
canvas = Canvas(frame_rate, height=2, bg="black", bd=0, highlightthickness=0)
canvas.pack(fill="x")
rate_label = Label(frame_rate,text="9.9",font=('Times New Roman',40,'bold'))
rate_label.pack(expand=True)

#frame into frame for poster
frame_poster=LabelFrame(frame,borderwidth=5)
frame_poster.place(x=10,y=10,width=300,height=350)
poster_label = Label(frame_poster,text='#Poster#',font=('Times New Roman',20,'bold'))
poster_label.place(x=0,y=0)

#frame into frame for Actor list
frame_adap=LabelFrame(frame,borderwidth=5)
frame_adap.place(x=320,y=95,width=470,height=200)
canvas = Canvas(frame_adap, width=400, height=200)
scrollbar = Scrollbar(frame_adap, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

c7 = Canvas(scrollable_frame, height=2, bg="black", bd=0, highlightthickness=0,width="470")
c7.pack(pady=10)
dir_label = Label(scrollable_frame,text="Director = ",wraplength=450,justify=LEFT,font=('Times New Roman',17,'bold'))
dir_label.pack()
c8 = Canvas(scrollable_frame, height=2, bg="black", bd=0, highlightthickness=0,width="470")
c8.pack(pady=10)
act_label = Label(scrollable_frame,text="Actors = ",wraplength=430,justify=LEFT,font=('Times New Roman',17,'bold'))
act_label.pack()
c9 = Canvas(scrollable_frame, height=2, bg="black", bd=0, highlightthickness=0,width="470")
c9.pack(pady=10)
mus_label = Label(scrollable_frame,text="Music = ",wraplength=450,justify=LEFT,font=('Times New Roman',17,'bold'))
mus_label.pack()
c10 = Canvas(scrollable_frame, height=2, bg="black", bd=0, highlightthickness=0,width="470")
c10.pack(pady=10)
star1 = Label(scrollable_frame,text="********",font=('Times New Roman',20,'bold')).pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
                 
#frame into frame for Summary
frame_sum=LabelFrame(frame,borderwidth=5)
            
frame_sum.place(x=320,y=305,width=710,height=215)

canvasn = Canvas(frame_sum, width=400, height=200)
scrollbarn = Scrollbar(frame_sum, orient="vertical", command=canvasn.yview)
scrollable_framen = Frame(canvasn)
scrollable_framen.bind(
    "<Configure>",
    lambda e: canvasn.configure(scrollregion=canvasn.bbox("all"))
)
canvasn.create_window((0, 0), window=scrollable_framen, anchor="nw")
canvasn.configure(yscrollcommand=scrollbarn.set)

c3 = Canvas(scrollable_framen, height=2, bg="black", bd=0, highlightthickness=0,width="710")
c3.pack(pady=10)
summ_label = Label(scrollable_framen,text="Summary",font=('Times New Roman',20,'bold')).pack(side=TOP)
c5 = Canvas(scrollable_framen, height=2, bg="black", bd=0, highlightthickness=0,width="710")
c5.pack(pady=10)
sum_label = Label(scrollable_framen,text="#Summary#",wraplength=670,justify=LEFT,font=('Times New Roman',17,'bold'))
sum_label.pack()
c4 = Canvas(scrollable_framen, height=2, bg="black", bd=0, highlightthickness=0,width="710")
c4.pack(pady=10)
genn_label = Label(scrollable_framen,text="Genre",font=('Times New Roman',20,'bold')).pack(side=TOP)
c6 = Canvas(scrollable_framen, height=2, bg="black", bd=0, highlightthickness=0,width="710")
c6.pack(pady=10)
gen_label = Label(scrollable_framen,text="#Genre#",wraplength=690,justify=LEFT,font=('Times New Roman',17,'bold'))
gen_label.pack()
c111 = Canvas(scrollable_framen, height=2, bg="black", bd=0, highlightthickness=0,width="710")
c111.pack(pady=10)

revv_label = Label(scrollable_framen,text="Review",font=('Times New Roman',20,'bold')).pack(side=TOP)
c112 = Canvas(scrollable_framen, height=2, bg="black", bd=0, highlightthickness=0,width="710")
c112.pack(pady=10)
rev_label = Label(scrollable_framen,text="No review Available",wraplength=690,justify=LEFT,font=('Times New Roman',17,'bold'))
rev_label.pack()

c11 = Canvas(scrollable_framen, height=2, bg="black", bd=0, highlightthickness=0,width="710")
c11.pack(pady=10)


canvasn.pack(side="left", fill="both", expand=True)
scrollbarn.pack(side="right", fill="y")



#addwatchlist and not inerested button inside the main frame
def inte():
    global movies_list, current_index
    m= movies_list[current_index]
    res = c.execute("SELECT inte, notinte,markc FROM movie WHERE title = ?", (m[0],))
    s=res.fetchone()

    if s:
        inte_s, notinte_s,markc_s= s
        if inte_s=='yes':
            messagebox.showinfo("Info", "Movie is already in Your Watchlist")
        elif notinte_s == 'yes':
            messagebox.showinfo("Info", "Movie is in the Not Interested List")
        elif markc_s =='yes':
            messagebox.showinfo("Info", "You have already watched this Movie")
        else:
            c.execute("UPDATE movie SET inte = 'yes' WHERE title = ?", (m[0],))
            conn.commit()
            messagebox.showinfo("Success", "Movie added to Your Watchlist")
    else:
        messagebox.showinfo("Error", "Movie not found in the database")

def notinte():
    global movies_list, current_index
    m= movies_list[current_index]
    res = c.execute("SELECT inte, notinte,markc FROM movie WHERE title = ?", (m[0],))
    s = res.fetchone()
    if s:
        inte_s, notinte_s,markc_s = s

        if notinte_s == 'yes':
            messagebox.showinfo("Info", "Movie is already in the Not Interested List")
        elif inte_s == 'yes':
            messagebox.showinfo("Info", "Movie is in Your Watchlist")
        elif markc_s =='yes':
            messagebox.showinfo("Info", "You have already watched this Movie")
        else:
            c.execute("UPDATE movie SET notinte = 'yes' WHERE title = ?", (m[0],))
            conn.commit()
            messagebox.showinfo("Success", "Movie added to Not Interested List")
    else:
        messagebox.showinfo("Error", "Movie not found in the database")    
    

wat_b = Button(frame,text='Add \nto \nWatchlist',command=inte,width=10,height=5,borderwidth=5,fg='White',bg='Green',activeforeground='White',activebackground='Black',font=('Times New Roman',15,'bold'))
wat_b.place(x=12,y=370)
not_i = Button(frame,text='Not \nInterested',command=notinte,width=10,height=5,borderwidth=5,fg='White',bg='Red',activeforeground='White',activebackground='Black',font=('Times New Roman',15,'bold'))
not_i.place(x=165,y=370)

#my watchlist
def watch():
    global b
    wat = Toplevel()
    wat.title('My Watchlist')
    wat.geometry('510x600')
    wat.attributes('-topmost', True)
    wat.lift()
    wat.focus_set()
    
    conn = sqlite3.connect('moviep.db')
    c = conn.cursor()

    #watchlist frame
    frame_wat = LabelFrame(wat, borderwidth=5)
    frame_wat.place(x=10, y=10, width=490, height=250)

    can1 = Canvas(frame_wat, width=460, height=250)
    scrollbarn1 = Scrollbar(frame_wat, orient="vertical", command=can1.yview)
    scr_fr = Frame(can1)
    scr_fr.bind(
        "<Configure>",
        lambda e: can1.configure(scrollregion=can1.bbox("all"))
    )
    can1.create_window((0, 0), window=scr_fr, anchor="nw")
    can1.configure(yscrollcommand=scrollbarn1.set)
    Label(scr_fr, text='My Watchlist', font=('Times New Roman', 16, 'bold')).place(x=170,y=10)
    Label(scr_fr,text='', font=('Times New Roman', 16, 'bold')).grid(row=0, column=0, columnspan=1, pady=10)
    c3 = Canvas(scr_fr, height=2, bg="black", bd=0, highlightthickness=0,width="500")
    c3.place(x=13,y=40)
    Label(scr_fr, text="Title", font=('Times New Roman', 12, 'bold')).grid(row=1, column=0, padx=5, pady=5)
    Label(scr_fr, text="Rating", font=('Times New Roman', 12, 'bold')).grid(row=1, column=1, padx=5, pady=5)
    Label(scr_fr, text="Actions", font=('Times New Roman', 12, 'bold')).grid(row=1, column=2, padx=5, pady=5)
    c4 = Canvas(scr_fr, height=2, bg="black", bd=0, highlightthickness=0,width="500")
    c4.place(x=13,y=80)
    res = c.execute("SELECT title, rate FROM movie WHERE inte = 'yes'")
    movies = res.fetchall()
    index=2
    for movie in movies:
        title, rating = movie
        Label(scr_fr, text=title,wraplength=150, font=('Times New Roman', 12)).grid(row=index, column=0, padx=5, pady=5)
        Label(scr_fr, text=rating, font=('Times New Roman', 12)).grid(row=index, column=1, padx=5, pady=5)

        def mark_c(movie_title=title):
            c.execute("UPDATE movie SET inte = 'no' WHERE title = ?", (movie_title,))
            c.execute("UPDATE movie SET markc = 'yes' WHERE title = ?", (movie_title,))
            conn.commit()
            messagebox.showinfo("Success", f"Marked '{movie_title}' as Completed.")
            wat.destroy()
            watch()
        complete_button = Button(scr_fr, text="Mark Completed", command=mark_c, bg='green', fg='white')
        complete_button.grid(row=index, column=2, padx=5, pady=5, sticky="ew")
        def remove_m(movie_title=title):
            c.execute("UPDATE movie SET inte = 'no' WHERE title = ?", (movie_title,))
            conn.commit()
            messagebox.showinfo("Success", f"Removed '{movie_title}' from Watchlist.")
            wat.destroy()
            watch()
        remove_button = Button(scr_fr, text="Remove", command=remove_m, bg='red', fg='white')
        remove_button.grid(row=index , column=3, padx=5, pady=5, sticky="ew")
        index+=1
    Label(scr_fr, text="\t              ", font=('Times New Roman', 12)).grid(row=index+1, column=0, padx=5, pady=5)
    Label(scr_fr, text="\t              ", font=('Times New Roman', 12)).grid(row=index+1, column=1, padx=5, pady=5)
    can1.pack(side="left", fill="both", expand=True)
    scrollbarn1.pack(side="right", fill="y")

    #completed frame
    frame=LabelFrame(wat,borderwidth=5)
    frame.place(x=10, y=270, width=490, height=250)
    can2 = Canvas(frame, width=460, height=250)
    scrollbarn2 = Scrollbar(frame, orient="vertical", command=can2.yview)
    scr_fr2 = Frame(can2)
    scr_fr2.bind(
        "<Configure>",
        lambda e: can2.configure(scrollregion=can2.bbox("all"))
    )
    can2.create_window((0, 0), window=scr_fr2, anchor="nw")
    can2.configure(yscrollcommand=scrollbarn2.set)
    Label(scr_fr2, text='My Completed List', font=('Times New Roman', 16, 'bold')).place(x=150, y=10)
    Label(scr_fr2, text='', font=('Times New Roman', 16, 'bold')).grid(row=0, column=0, columnspan=1, pady=10)
    c32 = Canvas(scr_fr2, height=2, bg="black", bd=0, highlightthickness=0, width="500")
    c32.place(x=13, y=40)
    Label(scr_fr2, text="Title", font=('Times New Roman', 12, 'bold')).grid(row=1, column=0, padx=5, pady=5)
    Label(scr_fr2, text="Action", font=('Times New Roman', 12, 'bold')).grid(row=1, column=1, padx=5, pady=5)
    c42 = Canvas(scr_fr2, height=2, bg="black", bd=0, highlightthickness=0, width="500")
    c42.place(x=13, y=80)
    r = c.execute("SELECT title FROM movie WHERE markc = 'yes'")
    mov = r.fetchall()
    titles = [m[0] for m in mov]
    y = 2
    for t in titles:
        title = t
        Label(scr_fr2, text=title, wraplength=150, font=('Times New Roman', 12)).grid(row=y, column=0, padx=5, pady=5)
        def rev(title=title):
            rev_window = Toplevel()
            rev_window.title('My Review')
            rev_window.geometry('710x400')
            rev_window.attributes('-topmost', True)
            rev_window.lift()
            rev_window.focus_set()
            r2 = c.execute("SELECT revrate, rev FROM movie WHERE title = ?", (title,))
            reve = r2.fetchone()
            Label(rev_window, text='My Watchlist', font=('Times New Roman', 16, 'bold')).pack(padx=5, pady=5)
            Label(rev_window, text="Title : " + title, font=('Times New Roman', 12, 'bold')).place(x=10, y=40)
            Label(rev_window, text="Your Rating = ", font=('Times New Roman', 13)).place(x=10, y=80)
            y_rate = Entry(rev_window, width=5, borderwidth=5, font=('Times New Roman', 13))
            y_rate.place(x=115, y=80)
            if reve[0] is not None:
                y_rate.insert(0, reve[0])
            Label(rev_window, text="Your Review = ", font=('Times New Roman', 13)).place(x=10, y=120)
            y_rev = Text(rev_window, height=5, borderwidth=5, width=75, font=('Times New Roman', 13))
            y_rev.place(x=10, y=160)
            if reve[1] is not None:
                y_rev.insert(END, reve[1])
            def reved():
                a_rate = y_rate.get()
                b_rev = y_rev.get("1.0", END).strip()
                c.execute("UPDATE movie SET revrate = ?, rev = ? WHERE title = ?", (a_rate, b_rev, title))
                messagebox.showinfo("Success", f"You added your review on '{title}'.")
                conn.commit()
                rev_window.destroy()
            reved_b = Button(rev_window, width=20, height=2, text="Add your review", bg='black',fg='white', command=reved, borderwidth=5, font=('Times New Roman', 15, 'bold'))
            reved_b.place(x=240, y=300)
        review_b = Button(scr_fr2, text="Review", command=lambda t=title: rev(t), bg='blue', fg='white')
        review_b.grid(row=y, column=1, padx=5, pady=5, sticky="ew")
        y += 1
    Label(scr_fr2, text="\t\t\t    ", font=('Times New Roman', 12)).grid(row=y+1,column=0,padx=5,pady=5)
    Label(scr_fr2, text="\t\t\t    ", font=('Times New Roman', 12)).grid(row=y+1,column=1,padx=5, pady=5)
    can2.pack(side="left", fill="both", expand=True)
    scrollbarn2.pack(side="right", fill="y")
    ex_b=Button(wat,text='Exit',bg='Dark Red',fg='White',borderwidth=5,font=('Times New Roman',16,'bold'),command = wat.destroy)
    ex_b.pack(side=BOTTOM,padx=5,pady=7)

my_watch=Button(frame,width=23,borderwidth=5,height=2,text='My Watchlist',command=watch,fg='white',bg='Orange',font=('Times New Roman',15,'bold'))
my_watch.place(x=12,y=520)

#Not inetrested list
def noti():
    global b
    ni = Toplevel()
    ni.title('My Not Interested List')
    ni.geometry('500x490')
    ni.attributes('-topmost', True)
    ni.lift()
    ni.focus_set()

    Label(ni, text='My Not Interested List', font=('Times New Roman', 16, 'bold')).grid(row=0, column=1, columnspan=3, pady=10)
    Label(ni, text="Title", font=('Times New Roman', 12, 'bold')).grid(row=1, column=0, padx=10)
    Label(ni, text="Rating", font=('Times New Roman', 12, 'bold')).grid(row=1, column=1, padx=10)
    Label(ni, text="Actions", font=('Times New Roman', 12, 'bold')).grid(row=1, column=2, padx=10)
    res = c.execute("SELECT title, rate FROM movie WHERE notinte = 'yes'")
    movies = res.fetchall()
    for index, movie in enumerate(movies, start=2):
        title, rating = movie
        
        Label(ni, text=title, font=('Times New Roman', 12)).grid(row=index, column=0, padx=10, pady=5)
        Label(ni, text=rating, font=('Times New Roman', 12)).grid(row=index, column=1, padx=10, pady=5)
        
        def m_remove(movie_title=title):
            c.execute("UPDATE movie SET notinte = 'no' WHERE title = ?", (movie_title,))
            conn.commit()
            messagebox.showinfo("Success", f"'{movie_title}' is removed from not interested list")
            ni.destroy()
            noti() 
        complete_button = Button(ni, text="Remove", command=m_remove, bg='red', fg='white')
        complete_button.grid(row=index, column=2, padx=5, pady=5)
    b = Button(ni, text='Exit', command=ni.destroy)
    b.grid(row=len(movies) + 2, column=1, pady=20)

    
not_int=Button(root,text='My Not Interested List',fg='White',bg='black',command=noti,width=32,height=2,borderwidth=5,font=('Times New Roman',15,'bold'))
not_int.place(x=1100,y=750)




#prev and next buttons inside main frame
def next_movie():
    global current_index
    if current_index < len(movies_list) - 1:
        current_index += 1
        display_movie(current_index)
    else:
        messagebox.showinfo('End', 'No more movies.')

def prev_movie():
    global current_index
    if current_index > 0:
        current_index -= 1
        display_movie(current_index)
    else:
        messagebox.showinfo('End', 'This is the first movie.')


prev = Button(frame,width=10,text="<= Prev",command =prev_movie,borderwidth=5,activeforeground='White',activebackground='Black',font=('Times New Roman',15,'bold'))
prev.place(x=400,y=535)

next = Button(frame,width=10,text="next =>",command =next_movie,borderwidth=5,activeforeground='White',activebackground='Black',font=('Times New Roman',15,'bold'))
next.place(x=550,y=535)

#update button
def upd():
    global movies_list, current_index
    up=Toplevel()
    up.title('Update details')
    up.geometry('710x690')
    up.attributes('-topmost',True)
    up.lift()
    up.focus_set()
    m= movies_list[current_index]
    update_label = Label(up,text='UPDATE DETAILS',font=('Times New Roman',17,'bold','underline')).pack()
    #title update
    up_title = Label(up,text="Update title ",font=('Times New Roman',13)).place(x=10,y=40)
    up_e_title= Entry(up,width=30,borderwidth=5,font=('Times New Roman',13))
    up_e_title.place(x=140,y=40)
    up_e_title.insert(0,m[0])
    #year udpate
    up_year= Label(up,text="Update Year",font=('Times New Roman',13)).place(x=10,y=80)
    up_e_year = Entry(up,width=10,borderwidth=5,font=('Times New Roman',13))
    up_e_year.place(x=140,y=80)
    up_e_year.insert(0,m[1])
    #director update
    up_dir= Label(up,text="Update Director",font=('Times New Roman',13)).place(x=10,y=120)
    up_e_dir = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_dir.place(x=140,y=120)
    up_e_dir.insert(0,m[4])
    #actor 1-5 udpate
    up_act1= Label(up,text="Update Actor 1",font=('Times New Roman',13)).place(x=10,y=160)
    up_e_act1 = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_act1.place(x=140,y=160)
    up_e_act1.insert(0,m[5])
    
    up_act2= Label(up,text="Update Actor 2",font=('Times New Roman',13)).place(x=10,y=200)
    up_e_act2 = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_act2.place(x=140,y=200)
    up_e_act2.insert(0,m[6])
    
    up_act3= Label(up,text="Update Actor 3",font=('Times New Roman',13)).place(x=10,y=240)
    up_e_act3 = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_act3.place(x=140,y=240)
    up_e_act3.insert(0,m[7])
    
    up_act4= Label(up,text="Update Actor 4",font=('Times New Roman',13)).place(x=10,y=280)
    up_e_act4 = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_act4.place(x=140,y=280)
    up_e_act4.insert(0,m[8])
    
    up_act5= Label(up,text="Update Actor 5",font=('Times New Roman',13)).place(x=10,y=320)
    up_e_act5 = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_act5.place(x=140,y=320)
    up_e_act5.insert(0,m[9])
    
    #musician update
    up_music= Label(up,text="Update Musician",font=('Times New Roman',13)).place(x=350,y=120)
    up_e_music = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_music.place(x=490,y=120)
    up_e_music.insert(0,m[10])
    #genre update
    up_gen1= Label(up,text="Update Genre 1",font=('Times New Roman',13)).place(x=350,y=160)
    up_e_gen1 = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_gen1.place(x=490,y=160)
    up_e_gen1.insert(0,m[11])
    
    up_gen2= Label(up,text="Update Genre 2",font=('Times New Roman',13)).place(x=350,y=200)
    up_e_gen2 = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_gen2.place(x=490,y=200)
    up_e_gen2.insert(0,m[12])
    
    up_gen3= Label(up,text="Update Genre 3",font=('Times New Roman',13)).place(x=350,y=240)
    up_e_gen3 = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_gen3.place(x=490,y=240)
    up_e_gen3.insert(0,m[13])
    
    up_gen4= Label(up,text="Update Genre 4",font=('Times New Roman',13)).place(x=350,y=280)
    up_e_gen4 = Entry(up,width=20,borderwidth=5,font=('Times New Roman',13))
    up_e_gen4.place(x=490,y=280)
    up_e_gen4.insert(0,m[14])
    #summary update
    up_sum= Label(up,text="Update Summary",font=('Times New Roman',13)).place(x=10,y=360)
    up_e_sum = Text(up, height=5,borderwidth=5, width=75,font=('Times New Roman',13))
    up_e_sum.place(x=10,y=390)
    up_e_sum.insert(END,m[3])

    def up_d():
        ti=up_e_title.get()
        ye=up_e_year.get()
        di=up_e_dir.get()
        a1=up_e_act1.get()
        a2=up_e_act2.get()
        a3=up_e_act3.get()
        a4=up_e_act4.get()
        a5=up_e_act5.get()
        mu=up_e_music.get()
        g1=up_e_gen1.get()
        g2=up_e_gen2.get()
        g3=up_e_gen3.get()
        g4=up_e_gen4.get()
        su= up_e_sum.get("1.0",END).strip()
        c.execute("UPDATE movie SET title=?,year=?, dec=?,dir=?,act1=?,act2=?,act3=?,act4=?,act5=?, music=?, gen1=?, gen2=?, gen3=?,gen4=? WHERE title=?",
                  (ti,ye,su,di,a1,a2,a3,a4,a5,mu,g1,g2,g3,g4,m[0]))
        conn.commit()  
        movies_list[current_index] = (ti,ye,m[2],su,di,a1,a2,a3,a4,a5,mu,g1,g2,g3,g4,m[-1])
        display_movie(current_index)
        messagebox.showinfo("Success", "Movie details updated successfully!")
    
    upd_b = Button(up,width=20,height=2,text="Update",bg='black',fg='white',command=up_d,borderwidth=5,font=('Times New Roman',15,'bold'))
    upd_b.place(x=220,y=590)
    b=Button(up,text='Exit',bg='Dark Red',fg='White',borderwidth=5,font=('Times New Roman',15,'bold'),command=up.destroy)
    b.place(x=600,y=20)
    
update_b= Button(frame,width=20,height=2,text="Update details of Movie",bg='yellow',command=upd,borderwidth=5,activeforeground='white',activebackground='Black',font=('Times New Roman',15,'bold'))
update_b.place(x=770,y=520)

#status inside the main frame
status = Label(frame, text='RESULT ' + '1 ' + 'OF ' + 'n ', bd=1, relief=SUNKEN, anchor='e', font=('Times New Roman', 15))
status.pack(side='bottom', fill='x', padx=10, pady=10)



#check box frame
    
frame_c = LabelFrame(root, borderwidth=10)
frame_c.place(x=1100, y=200, width=400, height=520)
movies_list=[]
def filt():
    global movies_list, current_index
    ch= [var.get() for var in genre_var if var.get()]
    if(len(ch)>=3):
        messagebox.showinfo("Error", "You can select MAX 2 genres ")
    elif(len(ch)==0):
        messagebox.showinfo("Error", "You need to Select MAX 2 genres max")
    elif(len(ch)==1):
        res = c.execute('''select * from movie where  gen1 like ? or gen2 like ? or gen3 like ? or gen4 like ?''',
                        ('%'+ch[0]+'%','%'+ch[0]+'%','%'+ch[0]+'%','%'+ch[0]+'%'))
        movies_list = res.fetchall()
        if movies_list:
            current_index = 0
            display_movie(current_index)
        else:
            messagebox.showinfo("Error", "Movie like this does not exist in our database")
    else:
        res = c.execute('''select * from movie where  gen1 like ? or gen2 like ? or gen3 like ? or gen4 like ? or
                                                      gen1 like ? or gen2 like ? or gen3 like ? or gen4 like ?''',
                        ('%'+ch[0]+'%','%'+ch[0]+'%','%'+ch[0]+'%','%'+ch[0]+'%','%'+ch[1]+'%','%'+ch[1]+'%','%'+ch[1]+'%','%'+ch[1]+'%'))
        movies_list = res.fetchall()
        if movies_list:
            current_index = 0
            display_movie(current_index)
        else:
            messagebox.showinfo("Error", "Movie like this does not exist in our database")
    

filter_button = Button(frame_c, text='Filter', width=28, height=2, borderwidth=5, fg='White', bg='Dark Blue', 
                       activeforeground='White', activebackground='Black', font=('Times New Roman', 15, 'bold'),
                       command=filt)  
filter_button.pack(padx=5, pady=10)

c1 = Canvas(frame_c, height=2, bg="black", bd=0, highlightthickness=0)
c1.pack(fill="x", padx=5, pady=10)

genre_label = Label(frame_c, text='Genre', font=('Times New Roman', 20, 'bold')).pack()

c2 = Canvas(frame_c, height=2, bg="black", bd=0, highlightthickness=0)
c2.pack(fill="x", padx=5, pady=10)
genre_list = ['Action', 'Adventure', 'Animation', 'Comedy', 'Biography', 'Crime', 'Thriller', 'Drama', 'Family', 
              'Romance', 'War', 'Fantasy', 'Horror', 'Sci-fi', 'Music', 'Kids']
genre_var = [StringVar(value='') for _ in genre_list]  # Default value is empty string, not '0'
left_frame = Frame(frame_c)
right_frame = Frame(frame_c)
half = len(genre_list) // 2
for i, (g, var) in enumerate(zip(genre_list, genre_var)):
    if i < half:
        Checkbutton(left_frame, text=g, variable=var, onvalue=g, offvalue='', font=('Times New Roman', 15, 'bold')).pack(anchor='w')
    else:
        Checkbutton(right_frame, text=g, variable=var, onvalue=g, offvalue='', font=('Times New Roman', 15, 'bold')).pack(anchor='w')

left_frame.pack(side="left", padx=20, pady=20)
right_frame.pack(side="right", padx=20, pady=20)


#search 

def srh():
    global movies_list, current_index

    a = m_entry.get()
    if a == "":
        messagebox.showinfo('Invalid', 'No value entered')
    elif ('    Search By => '==menu.get()) or ('        Title      => '==menu.get()):
        res = c.execute('select * from movie where title like ? order by rate desc', ('%' + a.upper() + '%',))
        movies_list = res.fetchall()

        if movies_list:
            current_index = 0
            display_movie(current_index)  
        else:
            messagebox.showinfo('Error', 'Movie not found.')
    elif ('Actor/Actress=>'==menu.get()):
        query = "Select * from movie where act1 like ? or act2 like ? or act3 like ? or act4 like ? or act5 like ? order by rate desc"
        s = '%' + a.upper() + '%'
        res = c.execute(query, (s,s,s,s,s))
        movies_list = res.fetchall()

        if movies_list:
            current_index = 0
            display_movie(current_index)  
        else:
            messagebox.showinfo('Error', 'Movie not found.')
    elif ('     Director  => '==menu.get()):
        res = c.execute('select * from movie where dir like ? order by rate desc', ('%' + a.upper() + '%',))
        movies_list = res.fetchall()

        if movies_list:
            current_index = 0
            display_movie(current_index)
        else:
            messagebox.showinfo('Error', 'Movie not found.')
    elif ('       Year      => '==menu.get()):
        res = c.execute('select * from movie where year like ? order by rate desc', (int(a),))
        movies_list = res.fetchall()

        if movies_list:
            current_index = 0
            display_movie(current_index)
        else:
            messagebox.showinfo('Error', 'Movie not found.')
    elif('     Rating     => '==menu.get()):
        rating = float(a)  
        res = c.execute('select * from movie where rate<=? order by rate desc', (rating,))
        movies_list = res.fetchall()

        if movies_list:
            current_index = 0
            display_movie(current_index)
        else:
            messagebox.showinfo('Error', 'Movie not found.')
            
def display_movie(index):
    r = movies_list[index]

    words = r[0].split()
    result = [w[0].upper() + w[1:].lower() for w in words]
    b = ' '.join(result)
    title_label.config(text=b)
    
    year_label.config(text=r[1])
    
    rate_label.config(text=r[2])
    
    sum_label.config(text=r[3])
    
    words = r[4].split()
    result = [w[0].upper() + w[1:].lower() for w in words]
    b = ' '.join(result)
    dir_label.config(text="Director = " + b)
    
    act = [r[6], r[7], r[8], r[9]]
    acttxt = r[5] if r[5] != "NULL" else ""
    for i in act:
        if i and i != "NULL":
            acttxt += " , " + i
        else:
            break
    words = acttxt.split()
    result = [w[0].upper() + w[1:].lower() for w in words]
    acttxt = ' '.join(result).rstrip(',') + "."
    act_label.config(text="Actors = " + acttxt)
    if r[10] is not None:
        wor = r[10].split()  # Split the string if it exists
    else:
        wor = []
    result = [w[0].upper() + w[1:].lower() for w in wor]
    b = ' '.join(result)
    mus_label.config(text="Music = " + b)
    gen = [r[12], r[13], r[14]]
    gentxt = r[11] if r[11] != "NULL" else ""
    for j in gen:
        if j and j != "NULL":
            gentxt += " , " + j
        else:
            break
    gentxt = gentxt.strip().rstrip(',') + "."
    gen_label.config(text=gentxt)  
    image_data = r[-1]
    image = Image.open(io.BytesIO(image_data))
    image = image.resize((284, 334), Image.LANCZOS)
    img = ImageTk.PhotoImage(image)
    poster_label.config(image=img)
    poster_label.image = img
    
    review_text = r[-3] if r[-3] not in [None, "NULL"] else "No review available"
    rev_label.config(text=review_text)
    
    original_rating = float(r[2]) if r[2] != "NULL" else 0
    user_rating = float(r[-2]) if r[-2] not in [None, "NULL"] else 0
    if user_rating > 0:
        average_rating = (original_rating + user_rating) / 2
        rate_label.config(text=f"{average_rating:.1f}", fg="red")  
    else:
        rate_label.config(text=f"{original_rating:.1f}", fg="black")

    
    status.config(text=f"RESULT {index + 1} OF {len(movies_list)}")

        

#search button
search = Button(root,text='Search',width=17,borderwidth=5,activeforeground='White',activebackground='Black',command=srh,font=('Times New Roman',15,'bold'))
search.place(x=1100,y=130)

#random movie at first
def start_ran():
    global movies_list, current_index
    res = c.execute('SELECT * FROM movie ORDER BY RANDOM() LIMIT 5')
    movies_list = res.fetchall()
    if movies_list:
        current_index = 0
        display_movie(current_index)  
    else:
        messagebox.showinfo('Error', 'Movie not found.')
start_ran()
star = Label(scrollable_framen,text="********",font=('Times New Roman',20,'bold')).pack()
root.mainloop()
