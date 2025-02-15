from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context, Template
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def home(request):
    return render(request, "home.html")

def diet(request):
    return render(request, "diet.html")

def predict(request):
    return render(request, "predict.html", {'form' : True})

def recommend(request):
    return render(request,"recommend.html")
    
def team(request):
    return render(request,"team.html")   
     
def result(request):
    
    data=pd.read_csv("./diabetes.csv")

    x = data.drop("Outcome",axis = 1)
    y = data['Outcome']

    #x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20)

    model =  SVC()
    model.fit(x,y)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])

    result1 = ""
    print(result1)
    if pred == [1]:
        result1 = "Positive"
        
    else:
        result1 = "Negative"

    return render(request, 'predict.html', {
        'result2' : result1,
        'form' : False,
    })

def diet1(request):
    return render(request,'diet.html') 

def below25(request):
    return render(request,"diet25.html")   

def age25(request):
    return render(request,"diet2550.html")

def above50(request):
    return render(request,"diet50.html")    
