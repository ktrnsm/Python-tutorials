###71 GPT alternative 2nd

import pandas as pd
import os
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def load_diabetes_data(filepath: str) -> pd.DataFrame:
    """
    Load diabetes data from CSV file and return as Pandas DataFrame.
    """
    diabetes_data = pd.read_csv(filepath)
    return diabetes_data


def preprocess_data(data: pd.DataFrame) -> tuple:
    """
    Split data into feature matrix X and target variable y, and perform
    scaling on X using StandardScaler.
    """
    y = data["Outcome"]
    X = data.drop(columns="Outcome")
    sc = StandardScaler()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train_scaled = sc.fit_transform(X_train)
    X_test_scaled = sc.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test


def train_random_forest(X_train: pd.DataFrame, y_train: pd.Series, param_grid: dict) -> RandomForestClassifier:
    """
    Train a random forest classifier on the given feature matrix X_train and
    target variable y_train, and return the trained model.
    """
    model = RandomForestClassifier(random_state=0)
    grid_search = GridSearchCV(model, param_grid=param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    return best_model


def evaluate_model(model: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series) -> float:
    """
    Use the trained model to make predictions on the test set X_test, and
    calculate the accuracy of the predictions using the target variable y_test.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy


def plot_feature_importance(model: RandomForestClassifier, feature_names: list):
    """
    Plot feature importance using the given trained model and feature names.
    """
    importances = model.feature_importances_
    sorted_idx = importances.argsort()
    plt.barh(range(len(sorted_idx)), importances[sorted_idx])
    plt.yticks(range(len(sorted_idx)), [feature_names[i] for i in sorted_idx])
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.show()


if __name__ == "__main__":
    os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
    diabetes_data = load_diabetes_data("C:/Users/Şebnem/Desktop/tutorials/diabetes.csv")
    X_train, X_test, y_train, y_test = preprocess_data(diabetes_data)

    # Define the parameter grid for GridSearchCV
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 10],
        'min_samples_split': [2, 5, 10]
    }

    model = train_random_forest(X_train, y_train, param_grid)
    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Accuracy: {accuracy * 100:.2f}%")

    # Plot feature importance
    feature_names = list(diabetes_data.drop(columns="Outcome").columns)
    plot_feature_importance(model, feature_names)
