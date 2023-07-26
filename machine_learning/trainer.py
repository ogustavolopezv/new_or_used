from joblib import dump
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector as selector
from loader import new_or_used_dataset

def train():
    # Subset
    new_or_used_dataset = new_or_used_dataset()
    X = new_or_used_dataset[["listing_type_id", "base_price", "price", "initial_quantity", "sold_quantity", "available_quantity"]]
    target_name = "condition"
    y = new_or_used_dataset[target_name]

    # Selectors
    numerical_columns_selector = selector(dtype_exclude=object)
    categorical_columns_selector = selector(dtype_include=object)

    numerical_columns = numerical_columns_selector(X)
    categorical_columns = categorical_columns_selector(X)

    # Preprocessors
    categorical_preprocessor = OneHotEncoder(handle_unknown="ignore")
    numerical_preprocessor = StandardScaler()

    preprocessor = ColumnTransformer(
        [
            ("one-hot-encoder", categorical_preprocessor, categorical_columns),
            ("standard_scaler", numerical_preprocessor, numerical_columns),
        ]
    )

    # Pipeline
    model = make_pipeline(preprocessor, GradientBoostingClassifier())

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)

    # Train
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # Metrics
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    print("Classification Report")
    print(classification_report(y_test, predictions))

    # Cross Validation
    cv_results = cross_validate(model, X, y, cv=5)

    scores = cv_results["test_score"]
    print(
        "The mean cross-validation accuracy is: "
        f"{scores.mean():.3f} ± {scores.std():.3f}"
    )

    # Save
    dump(model, 'models/new_or_used_v9.joblib')