from cProfile import label
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.linear_model import LinearRegression
from tkinter import *


dataset = pd.read_csv('C:\\Users\\datasets\\landprice1.csv')

X = dataset.iloc[0:, 0:3].values
Y = dataset.iloc[0:, -1].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=0)

X_train1 = np.reshape(X_train, (-1,1))
Y_train1 = np.reshape(Y_train, (-1,1))

X_test1 = np.reshape(X_test, (-1,1))
Y_test1 = np.reshape(Y_test, (-1,1))

lin_regressor = LinearRegression()
lin_regressor.fit(X_train,Y_train)

def model_pred():

    area1=entry1.get()
    area = int(area1)

    distance1=entry2.get()
    distance = int(distance1)

    crime1=entry3.get()
    crime = int(crime1)

    tran_variables = np.array([[area,distance,crime]])
    prid_price = lin_regressor.preditct(tran_variables)
    prid_price = str(prid_price)

    label1 = Label(window, text = prid_price, fg='red', font=("Courier",25))
    label1.pack()

    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

window = Tk()
window.geometry("600x700")
window.title("Template Window")
#1
label1 = Label(window,text="Enter the area of the land in thousand Sq Foot")
label1.pack()
area = StringVar()
area.set("")

entry1 = Entry(window, textvariable=area, fg='green', width=10, font=("Courier"))
entry1.pack()

#2
label2 = Label(window,text="Enter the Distance from the City Center")
label2.pack()
distance = StringVar()
distance.set("")

entry2 = Entry(window, textvariable=distance, fg='green', width=10, font=("Courier"))
entry2.pack()

#3
label3 = Label(window,text="Enter the Crime in that Region")
label3.pack()
crime = StringVar()
crime.set("")

entry3 = Entry(window, textvariable=crime, fg='green', width=10, font=("Courier"))
entry3.pack()

pred_button = Button(window, text="Predict", fg="red", command=model_pred)
pred_button.pack()

mainloop()



