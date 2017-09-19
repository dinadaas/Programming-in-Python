import numpy
from classifiers import create_decision_tree, create_random_forest, calculate_model_accuracy, calculate_confusion_matrix
from data import get_minecraft, get_first_n_samples
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

def p0(featuretype='histogram'):
    data_train, data_test, target_train, target_test = get_minecraft(featuretype)
    model = create_decision_tree()

    # TODO: Fit the model to the data using its fit method

    # TODO: Use the model's predict method to predict labels for the training and test sets
    #data_train, data_test, target_train, target_test = train_test_split(features, labels, test_size=0.33, random_state=42)

    #gnb = GaussianNB()
    #model = gnb.fit(data_train, target_train)

    # import some data to play with

    X = data_test
    y = target_test
    #class_names = model.target_names
    # Split the data into a training set and a test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    # Run classifier, using a model that is too regularized (C too low) to see
    # the impact on the results
    #classifier = svm.SVC(kernel='linear', C=0.01)
    #y_pred = classifier.fit(X_train, y_train).predict(X_test)

    # Run classifier, using a model that is too regularized (C too low) to set
    # the impact on the results
    classifier = svm.SVC(kernel='linear', C=0.01)
    y_pred = classifier.fit(X_train, y_train).predict(X_test)


    predict_train = y_test
    predict_test = y_pred

    accuracy_train, accuracy_test = calculate_model_accuracy(predict_train, predict_test, target_train, target_test)
    print('Training accuracy: {0:3f}, Test accuracy: {1:3f}'.format(accuracy_train, accuracy_test))

    cfm = calculate_confusion_matrix(predict_test,target_test)
    print "Confusion matrix"
    print cfm

    for q in range(1,3):
        for p in range(0,q):
            #compute confusion between classes p and q
            index_pq = [i for i,v in enumerate(target_train) if v in [p,q]]
            modelpq = create_decision_tree()
            #TODO: fit model to the data only involving classes p and q
            data_train, data_test, target_train, target_test = train_test_split(features, labels, test_size=0.5, random_state=42)
            testindex_pq = [i for i,v in enumerate(target_test) if v in [p,q]]
            #TODO: calculate and print the accuracy
            gnb = GaussianNB()
            model = gnb.fit(data_train, target_train)
            accuracy_pq = gnb.predict(data_test)
            print "One-vs-one accuracy between classes",p,"and",q,":",accuracy_pq

    return model, predict_train, predict_test, accuracy_train, accuracy_test


def p1():
    #TODO: compare different feature types
    m,ptrain,ptest,atrain,atest = p0('histogram')
    #m,ptrain,ptest,atrain,atest = p0('rgb')
    #m,ptrain,ptest,atrain,atest = p0('gray')

def p2():
    results = []
    model = None

    # TODO: Get the Minecraft dataset using get_minecraft() and create a decision tree
    data_train, data_test, target_train, target_test = get_minecraft('histogram')

    for n in [50, 100, 150, 200, 250]:
        # TODO: Fit the model using a subset of the training data of size n
        # Hint: use the get_first_n_samples function imported from data.py
        samp_data_train, samp_targ_train = get_first_n_samples(data_train, target_train, n)
        samp_data_test, samp_targ_test = get_first_n_samples(data_test, target_test, n)
        model.fit(samp_data_train, samp_targ_train)


        #TODO: use the model to fit the training data and predict labels for the training and test data
        samp_pred_train = model.predict(data_train)
        samp_pred_test = model.predict(data_test)


        # TODO: Calculate the accuracys of the model (use the training data that fit the model in the current iteration)
        accuracy_train_n, accuracy_test = calculate_model_accuracy(samp_pred_train, samp_pred_test, target_train, target_test)


        results.append((n, accuracy_train_n, accuracy_test))

    print(results)
    return model, results


def p3():
    results = []
    model = None

    # TODO: Get the Minecraft dataset
    get_minecraft()

    for n_estimators in [2, 5, 10, 20, 30]:
        # TODO: create a random forest classifier with n_estimators estimators
        model = create_random_forest(n_estimators)


        #TODO: use the model to fit the training data and predict labels for the training and test data
        model.fit(data_train,target_train)
        predict_train = model.predict(data_train)
        predict_test = model.predict(data_test)


        # TODO: calculate the accuracies of the models and add them to the results
        accuracy_train, accuracy_test = calculate_model_accuracy(predict_train,predict_test,target_train,target_test)

        results.append((n_estimators, accuracy_train, accuracy_test))
        print results

    return model, results


def bonus():
    results = []
    model = None

    # OPTIONAL: Repeat p0 using a logistic regression classifier


    return model, results

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", type=str, choices=['p0', 'p1', 'p2', 'p3', 'bonus'], help="The problem to run")
    args = parser.parse_args()

    if args.problem == 'p0':
        p0()
    elif args.problem == 'p1':
        p1()
    elif args.problem == 'p2':
        p2()
    elif args.problem == 'p3':
        p3()
    elif args.problem == 'bonus':
        bonus()
