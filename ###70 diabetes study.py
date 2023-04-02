import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'

def train_and_evaluate_model(model, X_train, y_train, X_test, y_test):
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)

data = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/diabetes.csv")
y = data["Outcome"]
X = data.drop(columns="Outcome")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Log Reg": LogisticRegression(random_state=0),
    "KNN": KNeighborsClassifier(),
    "SVC": SVC(random_state=0),
    "Bayes": GaussianNB(),
    "Dec Tree": DecisionTreeClassifier(random_state=0)
}

results = pd.DataFrame(columns=["Model", "Accuracy"])

for name, model in models.items():
    score = train_and_evaluate_model(model, X_train, y_train, X_test, y_test)
    results = pd.concat([results, pd.DataFrame({"Model": name, "Accuracy": round(score * 100, 2)}, index=[0])], ignore_index=True)

print(results)
