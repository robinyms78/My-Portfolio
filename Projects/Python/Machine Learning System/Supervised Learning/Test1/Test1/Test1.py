import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

# Filter warning
warnings.filterwarnings("ignore")

# Input file containing data
input_file = "bank-full.csv"
input_file2 = "bank-additional-full.csv"

# Read the data
X = []
y = []
count_class1 = 0
count_class2 = 0

# Read the data from bank-full.csv
#with open(input_file, "r") as f:
#    for line in f.readlines():
#        data = line[:-1].split(";")

#        if data[-1] == '"yes"':
#            X.append(data)
#            count_class1 += 1

#        if data[-1] == '"no"':
#            X.append(data)
#            count_class2 += 1

# Read the data from bank-additional-full.csv
with open(input_file2, "r") as f:
    for line in f.readlines():
        data = line[:-1].split(";")

        if data[-1] == '"yes"':
            X.append(data)
            del data[10] # Delete data with "unknown" parameters
            count_class1 += 1

        if data[-1] == '"no"':
            X.append(data)
            del data[10] # Delete data with "unknown" parameters
            count_class2 += 1

        # Delete data with "unknown" parameters
        if '"unknown"' in line:
            continue

# Convert to numpy array
X = np.array(X)

# Convert string data to numerical data
label_encoder = []
X_encoded = np.empty(X.shape)
for i, item in enumerate(X[0]):
    if item.isdigit():
        X_encoded[:, i] = X[:, i]
    else:
        label_encoder.append(preprocessing.LabelEncoder())
        X_encoded[:, i] = label_encoder[-1].fit_transform(X[:, i])

X = X_encoded[:, :-1].astype(int)
y = X_encoded[:, -1].astype(int)

# Split data into 80% training data and 20% test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)

# Create the logistic regression classifier
log_classifier = linear_model.LogisticRegression(solver="liblinear", C=1)

# create Naive Bayes classifier
bayes_classifier = GaussianNB() 

# Create SVM classifier
svm_classifier = OneVsOneClassifier(LinearSVC(random_state = 0, dual=False))

# Create the decision tree classifier
params = {"random_state": 0, "max_depth": 8}
tree_classifier = DecisionTreeClassifier(**params)

# Create ensemble learning classifier
params = {"n_estimators": 100, "max_depth": 8, "random_state": 0}
random_classifier = RandomForestClassifier(**params)

# Create neural network classifier
nn_classifier = MLPClassifier(solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(100,2), random_state=1, max_iter=300)

# Train the logistic regression classifier
log_classifier.fit(X_train, y_train)

# Train the Naive Bayes classifier
bayes_classifier.fit(X_train, y_train)

# Train the SVM classifier
svm_classifier.fit(X_train, y_train)

# Train the decision tree classifier
tree_classifier.fit(X_train, y_train)

# Train the ensemble learning classifier
random_classifier.fit(X_train, y_train)

# Train the neural network classifier
nn_classifier.fit(X_train, y_train)

# Compute the accuracy of logistic regression classifier
y_test_pred = log_classifier.predict(X_test)
accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
print("Accuracy of the logistic regression classifier = ", round(accuracy, 2), "%")

# Compute the accuracy of naive Bayes classifier
y_test_pred = bayes_classifier.predict(X_test)
accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
print("Accuracy of the naive Bayes classifier = ", round(accuracy, 2), "%")

# Compute accuracy of SVM classifier
y_test_pred = svm_classifier.predict(X_test)
accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
print("Accuracy of the SVM classifier = ", round(accuracy, 2), "%")

# Compute the accuracy of decision tree classifier
y_test_pred = tree_classifier.predict(X_test)
accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
print("Accuracy of the decision tree classifier = ", round(accuracy, 2), "%")

# Compute the accuracy of ensemble learning classifier
y_test_pred = random_classifier.predict(X_test)
accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
print("Accuracy of the ensemble learning classifier = ", round(accuracy, 2), "%")

# Compute the accuracy of neural network classifier
y_test_pred = nn_classifier.predict(X_test)
accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
print("Accuracy of the neural network classifier = ", round(accuracy, 2), "%")

# Compute the accuracy, precision, recall and F1 score of the logistic regression classifier based on threefold cross validation
num_fold = 3
accuracy_values = cross_val_score(log_classifier, X, y, scoring ="accuracy", cv=num_fold)
print("Accuracy of logistic classifier: " + str(round(100*accuracy_values.mean(), 2)) + "%")

precision_values = cross_val_score(log_classifier, X, y, scoring ="precision_weighted", cv=num_fold)
print("Precision of logistic classifier: " + str(round(100*precision_values.mean(), 2)) + "%")

recall_values = cross_val_score(log_classifier, X, y, scoring ="recall_weighted", cv=num_fold)
print("Recall of logistic classifier: " + str(round(100*recall_values.mean(), 2)) + "%")

f1_values = cross_val_score(log_classifier, X, y, scoring ="f1_weighted", cv=num_fold)
print("F1 score of logistic classifier: " + str(round(100*f1_values.mean(), 2)) + "%")

# Compute the accuracy, precision, recall and F1 score of the naive Bayes classifier based on threefold cross validation
num_fold = 3
accuracy_values = cross_val_score(bayes_classifier, X, y, scoring ="accuracy", cv=num_fold)
print("Accuracy of naive Bayes classifier: " + str(round(100*accuracy_values.mean(), 2)) + "%")

precision_values = cross_val_score(log_classifier, X, y, scoring ="precision_weighted", cv=num_fold)
print("Precision of naive Bayes classifier: " + str(round(100*precision_values.mean(), 2)) + "%")

recall_values = cross_val_score(log_classifier, X, y, scoring ="recall_weighted", cv=num_fold)
print("Recall of naive Bayes classifier: " + str(round(100*recall_values.mean(), 2)) + "%")

f1_values = cross_val_score(log_classifier, X, y, scoring ="f1_weighted", cv=num_fold)
print("F1 score of naive Bayes classifier: " + str(round(100*f1_values.mean(), 2)) + "%")

# Compute the accuracy, precision, recall and F1 score of the SVM classifier based on threefold cross validation
num_fold = 3
accuracy_values = cross_val_score(svm_classifier, X, y, scoring ="accuracy", cv=num_fold)
print("Accuracy of SVM classifier: " + str(round(100*accuracy_values.mean(), 2)) + "%")

precision_values = cross_val_score(svm_classifier, X, y, scoring ="precision_weighted", cv=num_fold)
print("Precision of SVM classifier: " + str(round(100*precision_values.mean(), 2)) + "%")

recall_values = cross_val_score(svm_classifier, X, y, scoring ="recall_weighted", cv=num_fold)
print("Recall of SVM classifier: " + str(round(100*recall_values.mean(), 2)) + "%")

f1_values = cross_val_score(svm_classifier, X, y, scoring ="f1_weighted", cv=num_fold)
print("F1 score of SVM classifier: " + str(round(100*f1_values.mean(), 2)) + "%")

# Compute the accuracy, precision, recall and F1 score of the decision classifier based on threefold cross validation
num_fold = 3
accuracy_values = cross_val_score(tree_classifier, X, y, scoring ="accuracy", cv=num_fold)
print("Accuracy of decision tree classifier: " + str(round(100*accuracy_values.mean(), 2)) + "%")

precision_values = cross_val_score(tree_classifier, X, y, scoring ="precision_weighted", cv=num_fold)
print("Precision of decision tree classifier: " + str(round(100*precision_values.mean(), 2)) + "%")

recall_values = cross_val_score(tree_classifier, X, y, scoring ="recall_weighted", cv=num_fold)
print("Recall of decision tree classifier: " + str(round(100*recall_values.mean(), 2)) + "%")

f1_values = cross_val_score(tree_classifier, X, y, scoring ="f1_weighted", cv=num_fold)
print("F1 score of decision tree classifier: " + str(round(100*f1_values.mean(), 2)) + "%")

# Compute the accuracy, precision, recall and F1 score of the ensemble learning classifier based on threefold cross validation
num_fold = 3
accuracy_values = cross_val_score(random_classifier, X, y, scoring ="accuracy", cv=num_fold)
print("Accuracy of ensemble learning classifier: " + str(round(100*accuracy_values.mean(), 2)) + "%")

precision_values = cross_val_score(random_classifier, X, y, scoring ="precision_weighted", cv=num_fold)
print("Precision of ensemble learning classifier: " + str(round(100*precision_values.mean(), 2)) + "%")

recall_values = cross_val_score(random_classifier, X, y, scoring ="recall_weighted", cv=num_fold)
print("Recall of ensemble learning classifier: " + str(round(100*recall_values.mean(), 2)) + "%")

f1_values = cross_val_score(random_classifier, X, y, scoring ="f1_weighted", cv=num_fold)
print("F1 score of ensemble learning classifier: " + str(round(100*f1_values.mean(), 2)) + "%")

# Compute the accuracy, precision, recall and F1 score of the neural network classifier based on threefold cross validation
num_fold = 3
accuracy_values = cross_val_score(nn_classifier, X, y, scoring ="accuracy", cv=num_fold)
print("Accuracy of neural network classifier: " + str(round(100*accuracy_values.mean(), 2)) + "%")

precision_values = cross_val_score(nn_classifier, X, y, scoring ="precision_weighted", cv=num_fold)
print("Precision of neural network classifier: " + str(round(100*precision_values.mean(), 2)) + "%")

recall_values = cross_val_score(nn_classifier, X, y, scoring ="recall_weighted", cv=num_fold)
print("Recall of neural network classifier: " + str(round(100*recall_values.mean(), 2)) + "%")

f1_values = cross_val_score(nn_classifier, X, y, scoring ="f1_weighted", cv=num_fold)
print("F1 score of neural nerwork classifier: " + str(round(100*f1_values.mean(), 2)) + "%")