import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore")
np.random.seed(42)

train_df = pd.read_csv("ml_components/muffins_vs_cupcakes.csv", index_col=0)


X = train_df.drop("Type", axis=1)
y = train_df["Type"].replace({"Cupcake": 0, "Muffin": 1})

from sklearn.ensemble import RandomForestClassifier


rnd_clf = RandomForestClassifier(n_estimators=10, random_state=42).fit(X, y)

import joblib

joblib.dump(rnd_clf, "ml_components/model.joblib")