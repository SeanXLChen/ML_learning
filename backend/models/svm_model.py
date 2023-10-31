'''
This is the SVMModel class, which utilize sklearn.svm.SVC model. This class provide useful method
to train, evaluate, and plot SVM model.
'''
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc, precision_recall_curve, average_precision_score
import numpy as np
import plotly.graph_objs as go

class SVMModel:
    """
    A class used to represent a Support Vector Machine model.

    Attributes
    ----------
    model : sklearn.svm.SVC
        The Support Vector Machine model.

    Methods
    -------
    train(X_train, y_train):
        Trains the model.
    predict(X):
        Makes a prediction using the model.
    evaluate(X_test, y_test):
        Evaluates the model.
    plot_confusion_matrix(confusion_mat):
        Plots a confusion matrix.
    plot_roc_curve(X_test, y_test):
        Plots a Receiver Operating Characteristic (ROC) curve.
    """


    def __init__(self, params=None):
        """
        Constructs all the necessary attributes for the SVMModel object.

        Parameters
        ----------
            params : dict, optional
                Parameters to be passed to the SVM model.
        """
        self.model = svm.SVC(**params, probability=True) if params is not None else svm.SVC(probability=True)


    def train(self, X_train, y_train):
        """
        Trains the SVMModel model.

        Parameters
        ----------
            X_train : numpy.ndarray
                Training data.
            y_train : numpy.ndarray
                Labels for the training data.
        """
        self.model.fit(X_train, y_train)


    def predict(self, X):
        """
        Makes a prediction using the SVMModel model.

        Parameters
        ----------
            X : numpy.ndarray
                Data for which to make a prediction.

        Returns
        -------
            numpy.ndarray
                Prediction made by the model.
        """
        return self.model.predict(X)


    def evaluate(self, X_test, y_test):
        """
        Evaluates the SVMModel model.

        Parameters
        ----------
            X_test : numpy.ndarray
                Testing data.
            y_test : numpy.ndarray
                Labels for the testing data.

        Returns
        -------
            dict
                Classification statistics.
            numpy.ndarray
                Confusion matrix.
        """
        y_pred = self.predict(X_test)
        classification_stats = classification_report(y_test, y_pred, output_dict=True)
        confusion_mat = confusion_matrix(y_test, y_pred).tolist()
        return classification_stats, confusion_mat


    def plot_confusion_matrix(self, confusion_mat, font_size=14):
        """
        Plots a confusion matrix.

        Parameters
        ----------
            confusion_mat : numpy.ndarray
                The confusion matrix to plot.
            font_size : int, optional
                Font size for the annotation text, default is 14.
        """
        annotations = []
        for i in range(confusion_mat.shape[0]):
            for j in range(confusion_mat.shape[1]):
                annotations.append(
                    go.layout.Annotation(
                        x=j,
                        y=i,
                        text=str(confusion_mat[i, j]),
                        showarrow=False,
                        font=dict(size=font_size, color="white" if abs(confusion_mat[i, j]) > (confusion_mat.max() / 2) else "black")
                    )
                )

        fig = go.Figure(data=go.Heatmap(
            z=confusion_mat, 
            x=['Predicted Positive', 'Predicted Negative'], 
            y=['Actual Positive', 'Actual Negative'],     
            colorscale='Blues',
            showscale=False),
            layout=go.Layout(
                annotations=annotations
            )
        )
        fig.layout.template = None
        return fig


    def plot_roc_curve(self, X_test, y_test):
        """
        Plots a Receiver Operating Characteristic (ROC) curve.

        Parameters
        ----------
            X_test : numpy.ndarray
                Testing data.
            y_test : numpy.ndarray
                Labels for the testing data.
        """
        y_pred_prob = self.model.predict_proba(X_test)[:, 1]

        fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
        roc_auc = auc(fpr, tpr)

        fig = go.Figure(data=[
            go.Scatter(x=fpr, y=tpr, mode='lines', name='ROC curve (area = %0.2f)' % roc_auc)
        ]
        )
        fig.update_layout(
            title='Receiver Operating Characteristic',
            xaxis=dict(title='False Positive Rate'),
            yaxis=dict(title='True Positive Rate'),
            autosize=False,
            width=500,
            height=500,
            margin=dict(
                l=50,
                r=50,
                b=100,
                t=100,
                pad=4
            )
        )
        fig.layout.template = None
        return fig
    

    def plot_precision_recall_curve(self, X_test, y_test):
        """
        Plots the precision-recall curve.

        Parameters
        ----------
            X_test : numpy.ndarray
                Test data.
            y_test : numpy.ndarray
                Labels for the test data.
        """
        y_score = self.model.predict_proba(X_test)[:, 1]
        precision, recall, _ = precision_recall_curve(y_test, y_score)
        average_precision = average_precision_score(y_test, y_score)

        fig = go.Figure(data=[
            go.Scatter(x=recall, y=precision, mode='lines', name=f'AP={average_precision:0.2f}')
        ])
        
        fig.update_layout(
            title='Precision-Recall Curve',
            xaxis=dict(title='Recall'),
            yaxis=dict(title='Precision'),
            autosize=False,
            width=500,
            height=500,
            margin=dict(
                l=50,
                r=50,
                b=100,
                t=100,
                pad=4
            )
        )
        
        fig.layout.template = None
        return fig
    

    def apply_pca_2d(self, X):
        """
        Applies PCA to reduce data to 2D.

        Parameters
        ----------
            X : numpy.ndarray
                Data to be reduced to 2D.

        Returns
        -------
            numpy.ndarray
                Data projected onto 2D using PCA.
        """
        pca = PCA(n_components=2)
        X_2d = pca.fit_transform(X)
        return X_2d
    

    def plot_decision_boundary(self, X_train, y_train, X_test, y_test):
        """
        Plots the decision boundary in 2D using Plotly.

        Parameters
        ----------
            X_train : numpy.ndarray
                Training data.
            y_train : numpy.ndarray
                Labels for the training data.
            X_test : numpy.ndarray
                Test data.
            y_test : numpy.ndarray
                Labels for the test data.
        """
        X_train_2d = self.apply_pca_2d(X_train)
        self.model.fit(X_train_2d, y_train)

        h = 0.5  # step size in the mesh
        
        # Define range with 10% expansion
        x_min = X_train_2d[:, 0].min() - 0.05 * (X_train_2d[:, 0].max() - X_train_2d[:, 0].min())
        x_max = X_train_2d[:, 0].max() + 0.05 * (X_train_2d[:, 0].max() - X_train_2d[:, 0].min())
        y_min = X_train_2d[:, 1].min() - 0.05 * (X_train_2d[:, 1].max() - X_train_2d[:, 1].min())
        y_max = X_train_2d[:, 1].max() + 0.05 * (X_train_2d[:, 1].max() - X_train_2d[:, 1].min())
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

        Z = self.model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        fig = go.Figure()

        # Get the custom colorscale
        bright_cscale = [[0, "#ff3700"], [1, "#0b8bff"]]
        custom_cscale = [
            [0.0000000, "#ff744c"],
            [0.1428571, "#ff916d"],
            [0.2857143, "#ffc0a8"],
            [0.4285714, "#ffe7dc"],
            [0.5714286, "#e5fcff"],
            [0.7142857, "#c8feff"],
            [0.8571429, "#9af8ff"],
            [1.0000000, "#20e6ff"],
        ]

        # Plot contour
        fig.add_trace(go.Contour(x=xx[0], y=yy[:, 0], z=Z, hoverinfo="none", showscale=False,
                                contours=dict(showlines=False), colorscale=custom_cscale, opacity=0.9))

        # Plot the threshold
        threshold_value = 0.5
        fig.add_trace(go.Contour(x=xx[0], y=yy[:, 0], z=Z, hoverinfo="none", showscale=False,
                                contours=dict(showlines=False, type="constraint", operation="=",
                                              value=threshold_value), line=dict(color="#708090")))

        # Plot training points
        fig.add_trace(go.Scatter(x=X_train_2d[:, 0], y=X_train_2d[:, 1], hoverinfo="none", mode='markers',
                                marker=dict(color=y_train, size=12, colorscale=bright_cscale, opacity=0.8),
                                showlegend=False, name='Training Data'))

        # Plot test points
        X_test_2d = self.apply_pca_2d(X_test)
        fig.add_trace(go.Scatter(x=X_test_2d[:, 0], y=X_test_2d[:, 1], hoverinfo="none", mode='markers',
                                marker=dict(color=y_test, size=12, symbol="triangle-up", 
                                            colorscale=bright_cscale, opacity=0.8),
                                showlegend=False, name='Test Data'))

        fig.layout.template = None
        return fig


