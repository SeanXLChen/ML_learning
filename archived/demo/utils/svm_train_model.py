import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import streamlit as st
from sklearn import datasets, metrics, svm
from sklearn.datasets import (load_breast_cancer, load_iris, load_wine,
                              make_moons)
from sklearn.model_selection import KFold, train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import RocCurveDisplay, roc_curve, auc, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelBinarizer

@st.cache_data(persist=True)
def load_dataset(dataset_name):
    """
    Loads the selected dataset. **Note: X only contains the first two features.

    Args:
        dataset_name (str): The name of the dataset.

    Returns:
        X: the dataset
        y: the target
    """
    if dataset_name == "Select your dataset":
        return None

    if dataset_name == "Iris":
        dataset = load_iris()
    elif dataset_name == "Wine":
        dataset = load_wine()
    # elif dataset_name == "Breast Cancer":
    else:
        dataset = load_breast_cancer()
    X = dataset.data[:,:2]
    y = dataset.target
    return X, y

#TODO: Fix the train_test_split on both data and target

def perform_train_test_split(data, target, split_method):
    """
    Perform the train-test split based on the specified split method.

    Args:
        dataset (pandas.DataFrame): The dataset to split.
        split_method (str): The selected split method ("Repeated Sub-Sampling" or "K-Fold Cross-Validation").

    Returns:
        tuple: A tuple containing the train and test datasets.
               If the dataset or split method is not provided, it returns (None, None).
    """
    dataset_name = st.session_state.dataset_name

    if data is None or dataset_name == "Select your dataset" or split_method is None:
        return None, None

    if split_method == "Repeated Sub-Sampling":
        train_percentage = st.session_state.train_percentage / 100
        X_train, X_test, y_train, y_test = train_test_split(
                                        data, target,
                                        train_size = train_percentage,
                                        random_state = 1
                                        )

        return X_train, X_test, y_train, y_test

    #NOTE: I(Sean) need to confirm whether split data into train/test set when using K-Fold CV
    # for now, I just split the data into train 70% and test 30%

    # elif split_method == "K-Fold Cross-Validation":
    #     k_value = st.session_state.k_value
    #     kf = KFold(n_splits = k_value)
    #     train_data_list = []
    #     test_data_list = []

    #     for train_index, test_index in kf.split(dataset):
    #         train_data, test_data = dataset.iloc[train_index], dataset.iloc[test_index]
    #         train_data_list.append(train_data)
    #         test_data_list.append(test_data)
        
    #     train = pd.concat(train_data_list)
    #     test = pd.concat(test_data_list)

    #     st.session_state.train_data = train
    #     st.session_state.test_data = test
    #     return train, test
    elif split_method == "K-Fold Cross-Validation":
        X_train, X_test, y_train, y_test = train_test_split(
                                        data, target,
                                        train_size = 0.7,
                                        random_state = 1
                                        )

        return X_train, X_test, y_train, y_test

# This is a helper function for svm_train_main()
# generates a grid of points, can be used to see svm's decision boundary
def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy

# This is a helper function for svm_train_main()
# use svm classifier to predict labels for each point on the grid, and plot the decision boundary
def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out



def svm_train_main():
    '''
    Method -- svm_train_main
        Triggered by clicking on the "Train" button. Will train the SVM model using the parameters in the
        st.session_state, and plot the graphs.
        Parameters:
            No parameters.
        Return None.
    '''
    #TODO:Right now can only plot the first two features of each dataset, AND the train_test split is set to 70%.
    #TODO: I(Jackie) will add more comments to this one, give me some time to fix it.
    X, y = load_dataset(st.session_state['dataset_name'])
    #TODO: For now, only support "Repeated Sub-Sampling" method
    # train test split
    X_train, X_test, y_train, y_test = perform_train_test_split(X, y, st.session_state['split_method'])

    # create svm model with user selected parameters
    model = svm.SVC(C=st.session_state['margin_value'], kernel=st.session_state['kernel_type'],
                    gamma=st.session_state['gamma_value'], coef0=st.session_state['coefficient_value'],
                    degree=st.session_state['degree_value'], probability=True)
    
    # train the modeln (svm model is a classifier)
    clf = model.fit(X_train, y_train)

    if st.session_state['split_method'] == "Repeated Sub-Sampling":
        
        fig, ax = plt.subplots()
        # title for the plots
        title = ('Decision surface of linear SVC ')
        # Set-up grid for plotting.
        # We only use the first two features of the X to do the plotting
        # TODO: can let user to decide which two features to plot
        X0, X1 = X_test[:, 0], X_test[:, 1]
        xx, yy = make_meshgrid(X0, X1)

        plot_contours(ax, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
        ax.scatter(X0, X1, c=y_test, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
        ax.set_ylabel('y label here')
        ax.set_xlabel('x label here')
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(title)
        ax.legend()
        st.pyplot(fig, use_container_width=300)

        # plot the confusion matrix

        #y_pred = clf.predict(X_test)
        #cm = confusion_matrix(y_test, y_pred, normalize=None) #NOTE: need to confirm whether to normalize the confusion matrix (over the true (rows), predicted (columns) conditions or all the population.)
        #TODO need to change the color of the confusion matrix to make it look better
        confusion_matrix = ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test, cmap=plt.cm.Blues)

        fig2, ax2 = plt.subplots()
        ax2.set_title('Confusion Matrix')
        confusion_matrix.plot(ax=ax2)
        st.pyplot(fig2, use_container_width=300)

        # plot the micro ROC AUC curve
        y_score = clf.predict_proba(X_test)
        label_binarizer = LabelBinarizer().fit(y_train)
        y_onehot_test = label_binarizer.transform(y_test)

        fig3, ax3 = plt.subplots()
        ax3.set_title('ROC Curve')

        roc = RocCurveDisplay.from_predictions(
            y_onehot_test.ravel(),
            y_score.ravel(),
            name="micro-average OvR ROC curve",
            color="blue"
        )

        roc.plot(ax=ax3)

        #TODO plot the macro precision-recall curve

        # store the fpr, tpr, and roc_auc for all averaging strategies
        fpr, tpr, roc_auc = dict(), dict(), dict()
        
        n_classes = len(np.unique(y))
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_onehot_test[:, i], y_score[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])

        fpr_grid = np.linspace(0.0, 1.0, 1000)

        # Interpolate all ROC curves at these points
        mean_tpr = np.zeros_like(fpr_grid)

        for i in range(n_classes):
            mean_tpr += np.interp(fpr_grid, fpr[i], tpr[i])  # linear interpolation

        # Average it and compute AUC
        mean_tpr /= n_classes

        fpr["macro"] = fpr_grid
        tpr["macro"] = mean_tpr
        roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

        ax3.plot(
            fpr["macro"], 
            tpr["macro"], 
            label=f"macro-average OvR ROC curve (AUC = {roc_auc['macro']:.2f})",
            color="navy",
            linestyle=":",
            linewidth=3,
        )

        ax3.legend()
        ax3.legend(loc="lower right")

        st.pyplot(fig3, use_container_width=300)

    elif st.session_state['split_method'] == "K-Fold Cross-Validation":
        #TODO: need to add Confusion Matrix & ROC curve for the K-Fold Cross-Validation
        #NOTE: I(Sean) don't know why but when i generate roc curve for k-fold, it always return null
        scores = cross_val_score(clf, X, y, cv=st.session_state['k_value'], scoring='f1_macro')
        #scores = cross_val_score(clf, X, y, cv=st.session_state['k_value'], scoring='roc_auc')
        st.write("The average F1 score is: ", scores.mean())
        fig, ax = plt.subplots()
        ax.set_title('F1 Macro Score')
        ax.plot(scores)
        st.pyplot(fig, use_container_width=300)


    