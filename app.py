import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import tkinter as tk

data = pd.read_csv('data.csv')

X = data.drop("RiskLevel", axis=1)
y = data["RiskLevel"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Tkinter GUI
root = tk.Tk()
root.geometry("500x700")

canvas1 = tk.Canvas(root, width=300, height=50)
canvas1.pack()
label1 = tk.Label(root, text='Yaş: ')
canvas1.create_window(100, 25, window=label1)
entry1 = tk.Entry(root)
canvas1.create_window(200, 25, window=entry1)

canvas2 = tk.Canvas(root, width=300, height=50)
canvas2.pack()
label2 = tk.Label(root, text='SystolicBP: ')
canvas2.create_window(100, 25, window=label2)
entry2 = tk.Entry(root)
canvas2.create_window(200, 25, window=entry2)

canvas3 = tk.Canvas(root, width=300, height=50)
canvas3.pack()
label3 = tk.Label(root, text='DiastolicBP: ')
canvas3.create_window(100, 25, window=label3)
entry3 = tk.Entry(root)
canvas3.create_window(200, 25, window=entry3)

canvas4 = tk.Canvas(root, width=300, height=50)
canvas4.pack()
label4 = tk.Label(root, text='BS: ')
canvas4.create_window(100, 25, window=label4)
entry4 = tk.Entry(root)
canvas4.create_window(200, 25, window=entry4)

canvas5 = tk.Canvas(root, width=300, height=50)
canvas5.pack()
label5 = tk.Label(root, text='Vücut Sıcaklığı: ')
canvas5.create_window(100, 25, window=label5)
entry5 = tk.Entry(root)
canvas5.create_window(200, 25, window=entry5)

canvas6 = tk.Canvas(root, width=300, height=50)
canvas6.pack()
label6 = tk.Label(root, text='Kalp Atışı: ')
canvas6.create_window(100, 25, window=label6)
entry6 = tk.Entry(root)
canvas6.create_window(200, 25, window=entry6)

def values():
    global age
    age = int(entry1.get())
    global systolicBP
    systolicBP = int(entry2.get())
    global diastolicBP
    diastolicBP = int(entry3.get())
    global BS
    BS = int(entry4.get())
    global bodyTemp
    bodyTemp = int(entry5.get())
    global heartRate
    heartRate = int(entry6.get())
    
    prediction = model.predict([[age, systolicBP, diastolicBP, BS, bodyTemp, heartRate]])
    label_prediction.configure(text='Risk Level: {}'.format(prediction))
    
button1 = tk.Button(root, text='Hamilelik Riskini Hesapla', command=values, bg='blue', fg='white')
button1.pack()

label_prediction = tk.Label(root, text='Risk Level: ', bg='yellow', fg='black')
label_prediction.pack()    

root.mainloop()