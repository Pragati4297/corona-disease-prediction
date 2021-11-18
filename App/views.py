from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np

from App.models import Prediction

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        if password == cpassword:
            print("User Saved")
            user = User.objects.create_user(
                username=name, password=password, email=email
            )
            user.save()

        return redirect("/login")
    else:
        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user_obj = User.objects.get(email=email)
        password = request.POST.get("password")
        user = authenticate(username=user_obj.username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("prediction")
        else:
            messages.info(request, "invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")

def positive(request):
    return render(request, "positive.html")

def negative(request):
    return render(request, "negative.html")

def prediction_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        brearthingproblem = False if request.POST["breathingproblem"] == "No" else True
        fever = False if request.POST["fever"] == "No" else True
        drycough = False if request.POST["drycough"] == "No" else True
        sourthroat = False if request.POST["sourthroat"] == "No" else True
        runningnose = False if request.POST["runningnose"] == "No" else True
        asthma = False if request.POST["asthma"] == "No" else True
        lungdisease = False if request.POST["lungdisease"] == "No" else True
        headache = False if request.POST["headache"] == "No" else True
        heartdisease = False if request.POST["heartdisease"] == "No" else True
        diabetes = False if request.POST["diabetes"] == "No" else True
        hyprtension = False if request.POST["hyprtension"] == "No" else True
        fatigue = False if request.POST["fatigue"] == "No" else True
        gastro = False if request.POST["gastro"] == "No" else True
        abroadtravel = False if request.POST["abroadtravel"] == "No" else True
        contact = False if request.POST["contact"] == "No" else True
        largegathering = False if request.POST["largegathering"] == "No" else True
        publicplaces = False if request.POST["publicplaces"] == "No" else True
        familyworking = False if request.POST["familyworking"] == "No" else True
        wearingmask = False if request.POST["wearingmask"] == "No" else True
        sanitization = False if request.POST["sanitization"] == "No" else True

        df = pd.read_csv(r"static\dataset\Covid Dataset.csv")

        le = LabelEncoder()
        Breathingproblem = le.fit_transform(df["breathingproblem"])
        Fever = le.fit_transform(df["fever"])
        DryCough = le.fit_transform(df["drycough"])
        Sorethroat = le.fit_transform(df["sorethroat"])
        Runningnose = le.fit_transform(df["runningnose"])
        Asthma = le.fit_transform(df["asthma"])
        Lungdisease = le.fit_transform(df["lungdisease"])
        Headache = le.fit_transform(df["headache"])
        Heartdisease = le.fit_transform(df["heartdisease"])
        Diabetes = le.fit_transform(df["diabetes"])
        Hypertension = le.fit_transform(df["hypertension"])
        Fatigue = le.fit_transform(df["fatigue"])
        Gastro = le.fit_transform(df["gastro"])
        Abroadtravel = le.fit_transform(df["abroadtravel"])
        Contact = le.fit_transform(df["contact"])
        Largegathering = le.fit_transform(df["largegathering"])
        Publicplaces = le.fit_transform(df["publicplaces"])
        Familyworking = le.fit_transform(df["familyworking"])
        Wearingmask = le.fit_transform(df["wearingmask"])
        Sanitization = le.fit_transform(df["sanitization"])
        Covid = le.fit_transform(df["COVID-19"])

        a = df.drop(
            [
                "breathingproblem",
                "fever",
                "drycough",
                "sorethroat",
                "runningnose",
                "asthma",
                "lungdisease",
                "headache",
                "heartdisease",
                "diabetes",
                "hypertension",
                "fatigue",
                "gastro",
                "abroadtravel",
                "contact",
                "largegathering",
                "publicplaces",
                "familyworking",
                "wearingmask",
                "sanitization",
                "COVID-19",
            ],
            axis=1,
        )

        a["breathingproblem"] = Breathingproblem
        a["fever"] = Fever
        a["drycough"] = DryCough
        a["sorethroat"] = Sorethroat
        a["runningnose"] = Runningnose
        a["asthma"] = Asthma
        a["lungdisease"] = Lungdisease
        a["headache"] = Headache
        a["heartdisease"] = Heartdisease
        a["diabetes"] = Diabetes
        a["hypertension"] = Hypertension
        a["fatigue"] = Fatigue
        a["gastro"] = Gastro
        a["abroadtravel"] = Abroadtravel
        a["contact"] = Contact
        a["largergathering"] = Largegathering
        a["publicplaces"] = Publicplaces
        a["familyworking"] = Familyworking
        a["wearingmask"] = Wearingmask
        a["sanitization"] = Sanitization
        a["COVID-19"] = Covid

        x = a.drop(["COVID-19"], axis=1)
        y = a[["COVID-19"]]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)

        tree = DecisionTreeClassifier()
        tree.fit(x_train, y_train)
        predict = np.array(
            [
                [
                    brearthingproblem,
                    fever,
                    drycough,
                    sourthroat,
                    runningnose,
                    asthma,
                    lungdisease,
                    headache,
                    heartdisease,
                    diabetes,
                    hyprtension,
                    fatigue,
                    gastro,
                    abroadtravel,
                    contact,
                    largegathering,
                    publicplaces,
                    familyworking,
                    wearingmask,
                    sanitization,
                ]
            ]
        )
        pred = tree.predict(predict)

        target = pred[0]

        hp = Prediction(
            breathingproblem=brearthingproblem,
            fever=fever,
            drycough=drycough,
            sourthroat=sourthroat,
            runningnose=runningnose,
            asthma=asthma,
            lungdisease=lungdisease,
            headache=headache,
            heartdisease=heartdisease,
            diabetes=diabetes,
            hypertension=hyprtension,
            fatigue=fatigue,
            gastro=gastro,
            abroadtravel=abroadtravel,
            contact=contact,
            largergathering=largegathering,
            publicplaces=publicplaces,
            familyworking=familyworking,
            wearingmask=wearingmask,
            sanitization=sanitization,
        )
        hp.save()
        result = ""

        if target == 1:
            return render(request,'positive.html')
        else:
            return render(request,'negative.html')

        return HttpResponse("Result : " + result)

    else:
        return render(request, "prediction.html")


def popup(request):
    return render(request, ".html")
