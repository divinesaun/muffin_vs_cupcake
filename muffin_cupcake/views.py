from django.shortcuts import render
import joblib
from pathlib import Path


def index(request):
    return render(request, "base.html", {"prediction": "None"})

def prediction(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    model = joblib.load(BASE_DIR / "ml_components/model.joblib")
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