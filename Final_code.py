# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:43:31 2019

@author: hi
"""

from tkinter import *
import csv
import pandas as pd
import numpy as np
import sklearn as sk
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
tk=Tk()
tk.title("Dengue prediction system")
tk.minsize(500,500)
l1=Label(tk,text="Fill the data",width=15,font=("bold",15))
l1.place(x=180,y=30)
l2=Label(tk,text="Rainfall",width=20,font=("bold",10))
l2.place(x=80,y=90)
s1=DoubleVar()
e1=Entry(tk,textvariable=s1)
e1.place(x=240,y=90)

s2=DoubleVar()
l3=Label(tk,text="Population density",width=20,font=("bold",10))
l3.place(x=80,y=130)
e2=Entry(tk,textvariable=s2)
e2.place(x=240,y=130)

s3=DoubleVar()
l4=Label(tk,text="Minimum Tempearture",width=20,font=("bold",10))
l4.place(x=80,y=170)
e3=Entry(tk,textvariable=s3)
e3.place(x=240,y=170)

s4=DoubleVar()
l5=Label(tk,text="Maxium temperature",width=20,font=("bold",10))
l5.place(x=80,y=210)
e4=Entry(tk,textvariable=s4)
e4.place(x=240,y=210)

s5=DoubleVar()
l6=Label(tk,text="Forest cover",width=20,font=("bold",10))
l6.place(x=80,y=250)
e5=Entry(tk,textvariable=s5)
e5.place(x=240,y=250)

s6=DoubleVar()
l7=Label(tk,text="Stagnant water",width=20,font=("bold",10))
l7.place(x=80,y=290)
e5=Entry(tk,textvariable=s6)
e5.place(x=240,y=290)

s7=DoubleVar()
l8=Label(tk,text="WasteLand Accumulation",width=20,font=("bold",10))
l8.place(x=80,y=330)
e6=Entry(tk,textvariable=s7)
e6.place(x=240,y=330)

s8=StringVar()
l9=Label(tk,text="Result",width=20,font=("bold",10))
l9.place(x=80,y=370)
e7=Entry(tk,textvariable=s8)
e7.place(x=240,y=370)

def normalisemaxtemp(value,k1,k2):
    new_maxa=1
    new_mina=0
    mina=k2
    maxa=k1
    #print("temp",mina,maxa)
    return float((((value-mina)/(maxa-mina))*(new_maxa-new_mina)+new_mina))
def normalisemintemp(value,k1,k2):
    new_maxa=1
    new_mina=0
    mina=k2
    maxa=k1
    #print("min temp",mina,maxa)
    return(((value-mina)/(maxa-mina))*(new_maxa-new_mina)+new_mina)
def normalisedenspop(value,k1,k2):
    new_maxa=1
    new_mina=0
    mina=k2
    maxa=k1
    #print("pop den",mina,maxa)
    return(((value-mina)/(maxa-mina))*(new_maxa-new_mina)+new_mina)
def normalisegeogarea(value,k1,k2):
    new_maxa=1
    new_mina=0
    mina=k2
    maxa=k1
    #print("forest",mina,maxa)
    return(((value-mina)/(maxa-mina))*(new_maxa-new_mina)+new_mina)
def normaliserainfall(value,k1,k2):
    new_maxa=1
    new_mina=0
    mina=k2
    maxa=k1
    #print("rainfall",mina,maxa)
    return float((((value-mina)/(maxa-mina))*(new_maxa-new_mina)+new_mina))
def normalise(value,k1,k2):
    new_maxa=1
    new_mina=0
    mina=k2
    maxa=k1
    #print("rainfall",mina,maxa)
    return float((((value-mina)/(maxa-mina))*(new_maxa-new_mina)+new_mina))
    
dmean=0
def callback():
    
    l=[]
    df=pd.read_excel(r'C:\\Users\\hi\\Desktop\\raw_data.xlsx')
    df.columns=['YEAR','MONTH','MANDAL','PopDensity','Forest','Rainfall','TempMin','TempMax','StagWater','WasteLand','DENGUECASES']
    dmean1=np.mean(df['DENGUECASES'])
    d_max=max(df['DENGUECASES'])
    d_min=min(df['DENGUECASES'])
    #dmean=normalise(dmean1,d_max,d_min)
    dmean=0.0159942
    k1=float(max(df['Rainfall']))
    k2=float(min(df['Rainfall']))
    str1=float(normaliserainfall(s1.get(),k1,k2))
    k1=max(df['PopDensity'])
    k2=min(df['PopDensity'])
    str2=normalisedenspop(s2.get(),k1,k2)
    k1=max(df['TempMax'])
    k2=min(df['TempMin'])
    str3=normalisemintemp(s3.get(),k1,k2)
    k1=max(df['TempMax'])
    k2=min(df['TempMin'])
    str4=normalisemaxtemp(s4.get(),k1,k2)
    k1=max(df['Forest'])
    k2=min(df['Forest'])
    str5=normalisegeogarea(s5.get(),k1,k2)
    l.append(str1)
    l.append(str2)
    l.append(str3)
    l.append(str4)
    l.append(str5)
    l.append(int(s6.get()))
    l.append(int(s7.get()))
    #return l
    #with open(r"C:\\Users\\hi\\Desktop\\final_data.csv",'a') as csvfile:
     #   newfile=csv.writer(csvfile)
     #   newfile.writerow(l)
    return l

def predict1():
    print("ynew",ynew)
    print("dmean",dmean)
    if(ynew>=0.0159942):
        e7.insert(20,"yes")
    else:
        e7.insert(20,"no")
        
        
b1=Button(tk,text="submit",width=20,bg="brown",fg="white",command=callback)
b1.place(x=140,y=400)
b2=Button(tk,text="predict",width=20,bg="brown",fg="white",command=predict1)
b2.place(x=300,y=400)

dataset=pd.read_csv('C:\\Users\\hi\\Desktop\\final_data.csv')
x=dataset.iloc[:,:7].values
y=dataset.iloc[:,7].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
model=Sequential()
model.add(Dense(input_dim=7,init='uniform',output_dim=80,activation='relu'))
model.add(Dense(output_dim=50,init='uniform',activation='relu'))
model.add(Dense(output_dim=20,init='uniform',activation='relu'))
model.add(Dense(output_dim=10,init='uniform',activation='relu'))
model.add(Dense(output_dim=1,init='uniform',activation='sigmoid'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=10)
print('------------------------------------------')
val_loss,val_acc=model.evaluate(x_test,y_test)
print(val_loss,val_acc)   
#algorithm
ynew=model.predict(np.array(np.reshape(callback(),(1,7)))) 
print(ynew) 

tk.mainloop()

