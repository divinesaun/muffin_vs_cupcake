from django.shortcuts import render
import joblib
from pathlib import Path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Data
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from rest_framework import status

def index(request):
    return render(request, "base.html", {"prediction": "None"})

def prediction(request):
    model = joblib.load("ml_components/model.joblib")
    flour = request.POST["flour"]
    milk = request.POST["milk"]
    sugar = request.POST["sugar"]
    butter = request.POST["butter"]
    egg = request.POST["egg"]
    baking_powder = request.POST["baking_powder"]
    vanilla = request.POST["vanilla"]
    salt = request.POST["salt"]
    prediction = model.predict([[flour, milk, sugar, butter, egg, baking_powder, vanilla, salt]])
    return render(request, "base.html", {"prediction": prediction[0]})

@api_view(["POST", "GET"])
def prediction_api(request):
    if request.method == "POST":
        serializer = Data(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = joblib.load("ml_components/model.joblib")
        prediction = model.predict(pd.DataFrame([serializer.data]))
        return Response({"Result": "The recipe is for a Cupcake"}, status=status.HTTP_202_ACCEPTED) if prediction == 0 else Response(f"The recipe is for a Muffin")
    elif request.method == "GET":
        return Response(
                            {
                                "Flour": 0,
                                "Milk": 0,
                                "Sugar": 0,
                                "Butter": 0,
                                "Egg":0,
                                "Baking_Powder": 0,
                                "Vanilla": 0,
                                "Salt": 0
                            }
                        )




