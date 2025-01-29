from django.shortcuts import render
import joblib
from pathlib import Path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Data
import warnings
warnings.filterwarnings("ignore")


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

        flour = serializer.data["Flour"]
        milk = serializer.data["Milk"]
        sugar = serializer.data["Sugar"]
        butter = serializer.data["Butter"]
        egg = serializer.data["Egg"]
        baking_powder = serializer.data["Baking_Powder"]
        vanilla = serializer.data["Vanilla"]
        salt = serializer.data["Salt"]

        model = joblib.load("ml_components/model.joblib")
        prediction = model.predict([[flour, milk, sugar, butter, egg, baking_powder, vanilla, salt]])
        return Response("The recipe is for a Cupcake") if prediction == 0 else Response("The recipe is for a Muffin")
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



