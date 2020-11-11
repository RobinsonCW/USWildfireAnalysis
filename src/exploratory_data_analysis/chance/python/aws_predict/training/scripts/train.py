#!/usr/bin/env python3

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

df = pd.read_csv("../data/ca_fires.csv", low_memory=False)

X = df[["LATITUDE", "LONGITUDE", "DISCOVERY_DATE", "FIRE_SIZE"]]
y = df["STAT_CAUSE_DESCR"]

# print(X[:1])

"""
Train-Test Split
"""
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

"""
Train Naive Bayes Classifier
"""

# fit gaussian naive bayes classifier
clf = OneVsRestClassifier(GaussianNB())
clf.fit(X_train, y_train)

joblib.dump(clf, "../models/gaussian_nb_classifier.pkl")

"""
Test Model
"""
y_pred = clf.predict(X_test)

print(f"The accuracy against the test set is {accuracy_score(y_test, y_pred)}")


"""
Create Pipeline
"""

pipe = make_pipeline(clf)
pipe.fit(X_train, y_train)
joblib.dump(pipe, "../models/pipeline.pkl")

pipeline_predictions = pipe.predict(X_test)
print(
    f"The accuracy against the test set is {accuracy_score(y_test, pipeline_predictions)}"
)


# 'LATITUDE', 'LONGITUDE', 'DISCOVERY_DATE', 'FIRE_SIZE'
pred_test = [[37.093056, -121.573056, 2448787.5, 0.3]]

print(type(pred_test))

print(pipe.predict(pred_test))