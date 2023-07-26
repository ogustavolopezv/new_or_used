from joblib import dump
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.compose import make_column_selector, make_column_transformer
from loader import new_or_used_dataset, new_or_used_featured_dataset

# new_or_used_v9, Vanilla GradientBoostingClassifier, All features, Categorical One-Hot

# Dataset
dataset = new_or_used_featured_dataset(new_or_used_dataset)

# Features
categorical_columns_subset = [
    "listing_type_id",
    "buying_mode",
    "accepts_mercadopago",
    "automatic_relist",
    "status",
    "sub_status_2",
    "currency_id",
    "has_warranty",
    "has_parent_item",
    "has_official_store",
    "has_video", 
    "has_variations"    
]

numerical_columns_subset = [
    "base_price",
    "price",
    "initial_quantity",
    "sold_quantity",
    "available_quantity"
]

X = dataset[categorical_columns_subset + numerical_columns_subset]
X[categorical_columns_subset] = X[categorical_columns_subset].astype("category")
y = dataset[["condition"]].values.ravel()

categorical_columns = X.select_dtypes(include="category").columns
n_categorical_features = len(categorical_columns)
n_numerical_features = X.select_dtypes(include="number").shape[1]

print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print(f"Number of categorical features: {n_categorical_features}")
print(f"Number of numerical features: {n_numerical_features}")

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# Pipeline
one_hot_encoder = make_column_transformer(
    (
        OneHotEncoder(sparse=False, handle_unknown="ignore"),
        make_column_selector(dtype_include="category"),
    ),
    remainder="passthrough",
)

one_hot = make_pipeline(
    one_hot_encoder, GradientBoostingClassifier()
)

pipeline = one_hot
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)

# Metrics
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("Classification Report")
print(classification_report(y_test, predictions))

dump(pipeline, '.models/new_or_used_v9.joblib')