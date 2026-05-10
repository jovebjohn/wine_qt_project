print("Running Random Forest Project...")

from sklearn.model_selection import train_test_split

from load_data import load_dataset
from preprocess import prepare_data
from train_model import train_random_forest
from evaluate import evaluate_model

# Load dataset
df = load_dataset('data/WineQT.csv')

# Prepare data
X, y = prepare_data(df)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = train_random_forest(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
evaluate_model(y_test, y_pred)