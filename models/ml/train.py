from joblib import dump
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

X = new_or_used_dataset_pd[["base_price", "price", "initial_quantity", "sold_quantity"]]
y = new_or_used_dataset_pd[["condition"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

clf_pipeline = [('scaling', MinMaxScaler()), ('clf', GradientBoostingClassifier())]
pipeline = Pipeline(clf_pipeline)

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("Classification Report")
print(classification_report(y_test, predictions))

dump(pipeline, './new_or_used_v1.joblib')