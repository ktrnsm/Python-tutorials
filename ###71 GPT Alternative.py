###71 GPT Alternative
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


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


def train_random_forest(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    """
    Train a random forest classifier on the given feature matrix X_train and
    target variable y_train, and return the trained model.
    """
    model = RandomForestClassifier(random_state=0)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series) -> float:
    """
    Use the trained model to make predictions on the test set X_test, and
    calculate the accuracy of the predictions using the target variable y_test.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy


if __name__ == "__main__":
    os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
    diabetes_data = load_diabetes_data("C:/Users/Şebnem/Desktop/tutorials/diabetes.csv")
    X_train, X_test, y_train, y_test = preprocess_data(diabetes_data)
    model = train_random_forest(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Accuracy: {accuracy * 100:.2f}%")
