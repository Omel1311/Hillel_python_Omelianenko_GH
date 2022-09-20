from Application import *

#инициализация окна
root = Tk()
root.title = "Морскький бій"
root.geometry("800x500+100+100")


#инициализация приложения
app = Application(master=root)
app.mainloop()