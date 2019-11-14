import pygame
import random  
import time 


FPS = 30
W = 1800  # ширина экрана
H = 1000  # высота экрана
WHITE =     (255,   255,    255)


BLUE =      (0,     70,     225)
WHITE =     (255,   255,    255)
RED =       (225,   0,      50)
GREEN =     (0,     225,    0)
Aqua =	 	   (0,	 	  128	, 	 128)
Navy_Blue =	(0,	 	  0,	 	   128)
Orange	= 	  (255,	  165,	   0)
Yellow	 =	  (255,	  255, 	  0)

list_of_colors = [BLUE,RED,GREEN,Aqua,Navy_Blue,Orange,Yellow]

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координаты и радиус круга
x = W // 2
y = H // 2
r = 10
 
motion = STOP

list_of_circles = []
for i in range(100):
    list_of_circles.append([random.randrange(0,W,2),random.randrange(0,H,2),random.choice(list_of_colors)])
    

x1 =0 
y1 =0
speed = 4
 
font = pygame.font.Font(pygame.font.get_default_font(), 36)
text_start= font.render('Сьешь все и не попадись ЗЕЛЕНОМУ', True, (0, 0, 0))
text_finish= font.render('ТЫ ПОБЕДИЛ', True, (0, 0, 0))
text_lose= font.render('ТЫ ПРОИГРАЛ', True, (0, 0, 0))


while 1:
    sc.fill(WHITE) # заливаем фон
    sc.blit(text_start, dest=(800,800))
    for i in list_of_circles:
        pygame.draw.circle(sc, i[-1], (i[0:2]), 10)

    pygame.draw.circle(sc, BLUE, (int(x), int(y)), int(r)) # рисуем круг

    pygame.draw.circle(sc, GREEN, (x1, y1), r)


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    # ----------------------for use --------------------------
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
    # ----------------------for use --------------------------
    #let our circle go to the 100,100

    try:
        if x > i.pos[0]:
            x-=speed
        if x < i.pos[0]:
            x+=speed
        if y > i.pos[1]:
            y-=speed
        if y < i.pos[1]:
            y+=speed
    except :
        pass

    if x1 > x:
            x1-=2
    if x1 < x:
            x1+=2
    if y1 > y:
            y1-=2
    if y1 < y:
            y1+=2
    
    

    for i in list_of_circles:
        #i[0:2]
        if (i[0]-x)**2 + (i[1]-y)**2 <= r**2:
            list_of_circles.remove(i)
            r+=1
            speed -= 0.01


    if (x - x1)**2 + (y - y1)**2 <= r**2:
            sc.blit(text_lose, dest=(800,800))
            time.sleep(5)
        
    if len(list_of_circles) == 0:
        sc.blit(text_finish, dest=(800,800))
        time.sleep(5)


            

    pygame.display.update()
 
    clock.tick(FPS)




    

    #    pygame.draw.circle(sc, RED, (int(x+(pos[0]-10)*0.1), int(y + (pos[1]-10)*0.1)), 5)
    #        if i.button == 1:
    #            pygame.draw.circle(sc, RED, i.pos, 20)
    #            pygame.display.update()
    #        elif i.button == 3:
    #            pygame.draw.circle(sc, BLUE, i.pos, 20)
    #            pygame.draw.rect(sc, GREEN, (i.pos[0]-10, i.pos[1]-10, 20, 20))
    #            pygame.display.update()
 
    #pygame.display.update()
 
    #for i in pygame.event.get():
    #    if i.type == pygame.QUIT:
    #        exit()
    #    elif i.type == pygame.KEYDOWN:
    #        if i.key == pygame.K_LEFT:
    #            motion = LEFT
    #        elif i.key == pygame.K_RIGHT:
    #            motion = RIGHT
    #    elif i.type == pygame.KEYUP:
    #        if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
    #            motion = STOP
 
    #if motion == LEFT:
    #    x -= 3
    #elif motion == RIGHT:
    #    x += 3
    #---------------------------------------------------------
    #for i in pygame.event.get():
    #    if i.type == pygame.QUIT:
    #        exit()
 
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_LEFT]:
    #    x -= 3
    #elif keys[pygame.K_RIGHT]:
    #    x += 3
    #elif keys[pygame.K_UP]:
    #    y -=3
    #elif keys[pygame.K_DOWN]:
    #    y +=3
    #else:
    #    if x > 350:
    #        x -=3
    #    elif x < 350:
    #        x+=3
    #    else:
    #        pass
    #---------------------------------------------------------
    
    #for i in pygame.event.get():
    #    if i.type == pygame.QUIT:
    #        exit()
    #    if i.type == pygame.MOUSEBUTTONDOWN:
    #        if i.button == 1:
    #            pygame.draw.circle(sc, RED, i.pos, 20)
    #            pygame.display.update()
    #        elif i.button == 3:
    #            pygame.draw.circle(sc, BLUE, i.pos, 20)
    #            pygame.draw.rect(sc, GREEN, (i.pos[0]-10, i.pos[1]-10, 20, 20))
    #            pygame.display.update()
    #        elif i.button == 2:
    #            sc.fill(WHITE)
    #            pygame.display.update()


    #for i in pygame.event.get():
    #    if i.type == pygame.QUIT:
    #        exit()
 
    #sc.fill(WHITE)

    
 
    #if pygame.mouse.get_focused():
    #    pos = pygame.mouse.get_pos()
    #    #pygame.draw.rect(sc, BLUE, (pos[0]-10, pos[1]-10, 20, 20))
    #    pygame.draw.circle(sc, RED, (int(x+(pos[0]-10)*0.1), int(y + (pos[1]-10)*0.1)), 5)
    #pygame.draw.rect(sc, BLUE, (x, y, 55, 55),7)    
    #pygame.display.update()
 
    #clock.tick(FPS)


# здесь подключаются модули
#str1 = "Модель:RENAULT  CLIO SYMBOLГод "
#print(str1[0:-4])

#import telebot # скачать библиотеку pytelegrambotapi

#bot = telebot.TeleBot('909961745:AAFO9rkaj53K_jHX2kSk0NyTbpxtM-h12UQ') # токен от БОТФазера у каждого свой

#keyboard1 = telebot.types.ReplyKeyboardMarkup()# создание клавиатуры
#keyboard1.row('Показать', 'Записать')


#@bot.message_handler(commands=['start']) # специальний декоратор для получения команды старт 
#def start_message(message): # функция для обработки сообщения 
#    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1) # отправка сообщения и отображение клавиатуры

#@bot.message_handler(content_types=['text'])# специальний декоратор для получения текста от пользователя
#def send_text(message):# функция для обработки сообщения 
#    if message.text.lower() == 'показать пароли': #  message.text гранит наше сообщение - сраавиваем строки 
#          bot.send_message(message.chat.id, 'Докажи что ты это ты')

#    elif message.text.lower() == ".":
#          bot.send_message(message.chat.id, 'Все твои пароли')

#    elif message.text.lower() == 'пока':
#          bot.send_message(message.chat.id, 'Прощай, создатель')
#    elif message.text.lower() == 'записать':
#        bot.send_sticker(message.chat.id, 'запоминаю') # отправляем стикер
#    else:
#        bot.send_message(message.chat.id, 'Шось я тебе не розумію')



#bot.polling()# обязательно шобы работало 




# CAADAgADRwADHSyIEOGw4z6YXcyxFgQ сердючка геть з украини

# CAADAgADjwYAAq1d_Ah8NrauKz8sGBYE мое увожение 


#from tkinter import *
#from tkinter import filedialog


#window = Tk()
#window.title("File")
#window.geometry("500x300")

#def clicked_bt_save():
#    path = entr.get()
#    data = text1.get(1.0,END)
#    with open(path,'w') as f:
#        f.write(data)
    

#def clicked_bt_open():
    
#    file = filedialog.askopenfilename()
#    entr.insert(0, file)

#    with open(file,'r') as f:
#        data1 = f.read()

#    text1.insert(1.0,data1)
    





#entr = Entry(width=40)
#entr.place(x=5,y = 0)

#btn_save = Button(text = "save",fg = "black",command = clicked_bt_save)
#btn_save.place(x=300,y = 0)

#btn_open = Button(text = "open",fg = "black",command = clicked_bt_open)
#btn_open.place(x=250,y = 0)



#text1 = Text(width=60, height=15, bg="white", fg='green')
#text1.place(x=5,y = 27)


#window.mainloop()


#from tkinter import *
#from tkinter import ttk
#from tkinter import filedialog
#gui = Tk()
#gui.geometry("400x400")
#gui.title("FC")

#def getFolderPath():
#    folder_selected = filedialog.askopenfilename() #askdirectory()
#    folderPath.set(folder_selected)

#def doStuff():
#    folder = folderPath.get()
#    with open(folder, 'r') as f:
#        data = f.read() 
#    T.insert(END, data)

#def doWrite():
#    folder = folderPath.get()
#    data =  T.get(1.0, END)
#    with open(folder, 'w') as f:
#        f.write(data)
    

#folderPath =StringVar()
#T = Text(height=20, width=30)
#T.grid(row=1,column = 0)

#a = Label(gui ,text="Enter name")
#a.grid(row=0,column = 0)
#E = Entry(gui,textvariable=folderPath)
#E.grid(row=0,column=1)
#btnFind = ttk.Button(gui, text="Browse Folder",command=getFolderPath)
#btnFind.grid(row=0,column=2)

#c = ttk.Button(gui ,text="find", command=doStuff)



#c.grid(row=4,column=0)
#c1 = ttk.Button(gui ,text="Write", command=doWrite)



#c1.grid(row=5,column=0)


#gui.mainloop()





#from tkinter import *
##import tkinter.ttk as t
#from tkinter import messagebox  
  
#def clicked():
#    res =""
#    try:    
#        res = "{}".format(int(first_param.get()) + int(second_param.get()))
#    except ValueError:
#        messagebox.showwarning('Warning', 'Invalid data')

#    lbl.configure(text=res) 



#window = Tk()  # создаем обьект окна для виндовс 
##fra1 = Frame(width=500,height=100,bg="darkred")
##fra2 = Frame(width=300,height=400,bg="green",bd=20)
##fra3 = Frame(width=500,height=150,bg="darkblue")

##fra1.pack()
##fra2.pack()
##fra3.pack()

##root = Tk()

##disp = Entry(root)
##disp.grid(row=0, columnspan=4, sticky=EW)

##but_lst = ['Cls', 'Back', '', 'Close', '7','8','9','/','4','5','6','8','1','2','3','-','0','.','=','+']

##i=int(0)
##for item in but_lst:
##    but = Button(root, text=item, width=10)
##    but.grid(row=i//4+1, column=i%4)
##    i += 1

##root.mainloop()

#window.title("Добро пожаловать в приложение PythonRu")  # пишем заголовок 
#window.geometry('300x400')  # размер окна 
#first_param= Entry(window,width=10)  
#first_param.place(x=100,y=0)
#second_param= Entry(window,width=10)  
#second_param.place(x=10,y=0)
#btn = Button(window, text="+", bg="black", fg="red",command = clicked)
#btn.place(x=200,y=0)
#lbl = Label(window, text="", font=("Arial Bold", 20))  
#lbl.place(x=200,y=100) # показать поле  


#window.mainloop()

##def clicked():
##    messagebox.showinfo('Заголовок', 'Текст')
##    messagebox.showwarning('Заголовок', 'Текст')  # показывает предупреждающее сообщение
##    messagebox.showerror('Заголовок', 'Текст')  # показывает сообщение об ошибке

##    res = "Привет {}".format(txt.get())

##    lbl.configure(text=res)
    



###def clicked():  
###    lbl.configure(text=selected.get())  
  
  
##window = Tk()  # создаем обьект окна для виндовс 
##window.title("Добро пожаловать в приложение PythonRu")  # пишем заголовок 
##window.geometry('400x250')  # размер окна 


##selected = IntVar()  
##rad4 = t.Radiobutton(window,text='Первый', value=1, variable=selected)  

##lbl = Label(window, text="", font=("Arial Bold", 20))  
##lbl.grid(column=0, row=0) # показать поле   
##btn = Button(window, text="Не нажимать!", bg="black", fg="red",command=clicked)
##btn.grid(column=0, row=2)
##txt = Entry(window,width=10)  
##txt.grid(column=1, row=0)  
##txt.focus()
##combo = t.Combobox(window)  
##combo['values'] = (1, 2, 3, 4, 5, "Текст")  
##combo.current(1)  # установите вариант по умолчанию  
##combo.grid(column=0, row=0)  
###combo.get()
##rad1 = t.Radiobutton(window, text='Первый', value=1)  
##rad2 = t.Radiobutton(window, text='Второй', value=2)  
##rad3 = t.Radiobutton(window, text='Третий', value=3)  
##rad1.grid(column=0, row=0)  
##rad2.grid(column=1, row=0)  
##rad3.grid(column=2, row=0)  
##style = t.Style()  
##style.theme_use('default')  
##style.configure("black.Horizontal.TProgressbar", background='black')  
##bar = t.Progressbar(window, length=200, style='black.Horizontal.TProgressbar')  
##bar['value'] = 70  
##bar.grid(column=0, row=0)  


##from tkinter import *
##root = Tk()

##def colorR():
##    fra.config(bg="Red")
##def colorG():
##    fra.config(bg="Green")
##def colorB():
##    fra.config(bg="Blue")

##def square():
##    fra.config(width=500)
##    fra.config(height=500)
##def rectangle():
##    fra.config(width=700)
##    fra.config(height=400)

##fra = Frame(root,width=300,height=100,bg="Black")
##fra.pack()

##m = Menu(root)
##root.config(menu=m)

##cm = Menu(m)
##m.add_cascade(label="Color",menu=cm)
##cm.add_command(label="Red",command=colorR)
##cm.add_command(label="Green",command=colorG)
##cm.add_command(label="Blue",command=colorB)

##sm = Menu(m)
##m.add_cascade(label="Size",menu=sm)
##sm.add_command(label="500x500",command=square)
##sm.add_command(label="700x400",command=rectangle)

##root.mainloop()



##window.mainloop()

