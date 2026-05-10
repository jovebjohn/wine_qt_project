from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)

    report = classification_report(y_test, y_pred)

    print("Accuracy:", accuracy)

    print("\nClassification Report:\n")
    print(report)