import fertilizer
import time
import SmsSender
from tkinter import *


# =======================================functions==================================================
def FertilizersUpdatesAction():
    global WeatherNotificationWindow
    WeatherNotificationWindow = Toplevel(main_window)
    WeatherNotificationWindow.geometry('1366x768+0+0')
    WeatherNotificationWindow.title('Fertilizers updates')

    data = StringVar()
    label = Label(WeatherNotificationWindow, font=('times', 16, ' roman'), textvariable=data, bg='light green', fg='violet red')
    label.pack(fill=BOTH)

    list_of_fertilizer_updates = fertilizer.Fertilizers_Updates.getListOfFertilizers()
    count = 0
    for i in list_of_fertilizer_updates:
        count += 1
        data.set(data.get() + "\n(" + str(
            count) + ") FERTILIZER: " + i.name + "\nPRICE: " + i.price + "\nWEIGHT: " + i.weight + "\nRATING: " + i.rating + "\nDESCRIPTION: " + i.description + "\n")

    button = Button(WeatherNotificationWindow, font=('arial', 23, 'roman'), text='Back', command=quit1, padx=22, pady=8, bg='light green')
    button.pack(side="bottom", fill=X)
    WeatherNotificationWindow.mainloop()


def FertilizerAlternativesAction():
    global WeatherNotificationWindow
    WeatherNotificationWindow = Toplevel(main_window)
    WeatherNotificationWindow.geometry('1366x768+0+0')
    WeatherNotificationWindow.title('Best alternatives of fertilizers')

    data = StringVar()
    label = Label(WeatherNotificationWindow, font=('times', 18, ' roman'), textvariable=data, bg='light green', fg='violet red')
    label.pack(fill=BOTH)

    list_of_alternative_fertilizers = fertilizer.Alternatives_Of_Fertilizers.getListOfAlternativeFertilizers()
    count = 0
    for i in list_of_alternative_fertilizers:
        count += 1
        data.set(data.get() + "\n(" + str(
            count) + ") FERTILIZER: " + i.name + "\nPRICE: " + i.price + "\nRATING: " + i.rating + "\nDESCRIPTION: " + i.description + "\n\n")

    button = Button(WeatherNotificationWindow, font=('arial', 23, 'roman'), text='Back', command=quit1, padx=22, pady=3, bg='light green')
    button.pack(side="bottom", fill=X)
    WeatherNotificationWindow.mainloop()


def FertilizerSuggestionsAction():
    global WeatherNotificationWindow
    WeatherNotificationWindow = Toplevel(main_window)
    WeatherNotificationWindow.geometry('1366x768+0+0')
    WeatherNotificationWindow.title('Fertilizers suggestions')

    data = StringVar()
    label = Label(WeatherNotificationWindow, font=('times', 18, ' roman'), textvariable=data, bg='light green', fg='violet red')
    label.pack(fill=BOTH)

    list_of_suggested_fertilizers = fertilizer.Suggestions_Of_Fertilizers.getListOfSuggestedFertilizers()
    count = 0
    for i in list_of_suggested_fertilizers:
        count += 1
        data.set(data.get() + "\n(" + str(
            count) + ") FERTILIZER SUGGESTION: " + i.suggestion + "\nUSE FOR: " + i.UseFor + "\n\n")

    button = Button(WeatherNotificationWindow, font=('arial', 23, 'roman'), text='Back', command=quit1, padx=22, pady=3, bg='light green')
    button.pack(side="bottom", fill=X)
    WeatherNotificationWindow.mainloop()


def WeatherNotificationsAction():
    global WeatherNotificationWindow, data, var
    WeatherNotificationWindow = Toplevel(main_window)
    WeatherNotificationWindow.geometry('1366x768+0+0')
    WeatherNotificationWindow.title('Weather notifications')

    frame1 = Frame(WeatherNotificationWindow, bg='light green')
    frame1.pack(fill=BOTH)
    label1 = Label(frame1, text='\n\n\n\nEnter city name for weather forecast\n', font=('times', 25, 'roman'), bg='light green')
    label1.pack(fill=BOTH)
    data = StringVar()
    entry = Entry(frame1, textvariable=data, width=30, font=('times', 20, 'roman'))
    entry.pack(ipady=20)
    button1 = Button(frame1, text='Process', font=('arial', 23, 'roman'), bd=6, command=sendSms)
    button1.pack()
    var=StringVar()
    var.set('\n\n\n\n\n\n')
    label2 = Label(frame1, textvariable=var, font=('times', 25, 'roman'), bg='light green', fg='violet red')
    label2.pack(fill=BOTH)
    button2 = Button(frame1, font=('arial', 23, 'roman'), text='Back', command=quit1, bg='light green', padx=22, pady=4)
    button2.pack(side='bottom', fill=X)
    WeatherNotificationWindow.mainloop()


def quit1():
    global WeatherNotificationWindow
    WeatherNotificationWindow.destroy()


def quit():
    main_window.destroy()


def sendSms():
    global data, var
    city_name = data.get()
    SmsSender.send_sms(city_name)
    temperature=SmsSender.get_weather(city_name)
    var.set("\nToday temperature at " + city_name + " is " + str(temperature) + "'C\n\n\n\n\n")


# =================================main_programme============================================

main_window = Tk()
main_window.geometry('1366x768+0+0')
main_window.title('Farmer Friend')

# =========================frame=============================================
frame = Frame(main_window, bg='light green')
frame.pack(fill=BOTH)

# =========================time===========================
localtime = time.asctime(time.localtime(time.time()))

# =======================labels=============================================
label1 = Label(frame, font=('times', 25, 'roman'), text=localtime, bg='light green', fg='green')
label1.pack()
label2=Label(frame, text='farmer friend', font=('calibri', 65, 'bold italic underline'), fg='green', bg='light green')
label2.pack()
label3 = Label(frame, font=('times', 30, 'bold'), text='MAIN MENU\n', bg='light green')
label3.pack(pady=30)

# ===================buttons=====================
button1 = Button(frame, font=('arial', 20, ' roman'), bd=10, text='Fertilizers updates',
                 command=FertilizersUpdatesAction, pady=3, padx=111)
button1.pack()
button2 = Button(frame, font=('arial', 20, 'roman'), bd=10, text='Best alternatives of fertilizers',
                 command=FertilizerAlternativesAction, pady=3, padx=48)
button2.pack()
button3 = Button(frame, font=('arial', 20, 'roman'), bd=10, text='Fertilizers suggestions',
                 command=FertilizerSuggestionsAction, pady=3, padx=85)
button3.pack()
button4 = Button(frame, font=('arial', 20, 'roman'), bd=10, text='Weather notifications',
                 command=WeatherNotificationsAction, pady=3, padx=90)
button4.pack()
button5 = Button(frame, font=('arial', 20, 'roman'), bd=10, text='Exit', command=quit, padx=30, pady=3)
button5.pack()

main_window.mainloop()
