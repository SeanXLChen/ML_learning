import pandas as pd
import streamlit as st
from streamlit_extras import add_vertical_space


def svm_background_what_it_is():
    main, pic = st.columns([5, 3])

    with main:
        what_it_is_context = """
        A support vector machine, SVM, is a supervised machine learning algorithm used for classification 
        and regression tasks. It's particularly effective in dealing with complex, high-dimensional datasets. 
        SVMs are based on the concept of finding an optimal **hyperplane** that separates different classes 
        in the data.

        In SVM, each data point in a training dataset is represented as a multidimensional feature vector. 
        The algorithm aims to find the best hyperplane that maximally separates the data points of different 
        classes. This hyperplane is selected to have the maximum distance or margin from the nearest data points 
        of each class. These nearest data points are called support vectors, hence the name "support vector machine."

        SVM can handle linearly separable data, but it's also capable of applying the "kernel trick," which allows 
        it to handle nonlinear data. The kernel trick involves transforming the original feature space into 
        a higher-dimensional space, where the data may become linearly separable. This allows SVM to find 
        nonlinear decision boundaries and make accurate classifications.

        ## Support Vector Classifier (SVC)
        A support vector classifier is a specific type of SVM used for binary classification tasks. It aims to find 
        the optimal hyperplane that separates the two classes while maximizing the margin. The support vector 
        classifier is often used interchangeably with the term "support vector machine" when referring to binary 
        classification.

        The support vector classifier uses the same principles as an SVM, including finding the support vectors 
        and maximizing the margin. However, SVC focuses specifically on binary classification and does not 
        directly handle multiclass classification problems. For multiclass classification, several binary SVCs 
        can be combined using strategies such as one-vs-one or one-vs-all.
        """
        st.markdown(what_it_is_context)

    with pic:
        st.image("res/SVM_graph.png")


def svm_background_use_cases():
    image_object_recognition_context = """
    ### Image Object Recognition
    SVC can be applied to image object recognition tasks, where the goal is to identify specific objects within 
    images. For example, an SVC model can be trained to detect and classify objects like cars, faces, or animals 
    in images, making it valuable in applications such as autonomous driving, surveillance systems, or image-based 
    search engines.
    """

    sentiment_analysis_context = """
    ### Sentiment Analysis
    SVC can be used for sentiment analysis tasks, such as determining the sentiment expressed in social media posts, 
    customer reviews, or survey responses. By training an SVC model on labeled data, it can classify text inputs 
    into positive, negative, or neutral sentiment categories, providing valuable insights for sentiment monitoring 
    or customer feedback analysis.
    """

    medical_diagnosis_context = """
    ### Medical Diagnosis
    SVC can aid in medical diagnosis tasks, such as detecting diseases or predicting medical conditions. 
    By training an SVC model on relevant patient data and medical records, it can help classify patients into 
    different diagnostic categories based on their symptoms, test results, or other relevant factors.
    """

    credit_risk_assessment_context = """
    ### Credit Risk Assessment
    SVC can assist in credit risk assessment and predicting the likelihood of loan defaults. By analyzing various 
    financial and credit-related factors of borrowers, an SVC model can be trained to classify loan applicants as 
    low or high risk, helping financial institutions make informed lending decisions.
    """

    st.markdown(image_object_recognition_context)
    st.divider()

    st.markdown(sentiment_analysis_context)
    st.divider()

    st.markdown(medical_diagnosis_context)
    st.divider()

    st.markdown(credit_risk_assessment_context)


def svm_background_pros_and_cons():
    SVM_PROS = [
        "Effective in high-dimensional spaces",
        "Works well with a clear margin of separation",
        "Effective even in cases where the number of dimensions is greater than the number of samples",
        "Memory efficient due to the use of a subset of training points (support vectors)",
        "Versatile with different kernel functions for flexibility in modeling complex relationships"
    ]

    SVM_CONS = [
        "Computationally intensive for large datasets",
        "Sensitive to the choice of hyperparameters",
        "Doesn't directly provide probability estimates",
        "Can be affected by outliers in the data",
        "Not suitable for non-linearly separable data without kernel trick"
    ]
    svm_table = {
        "Pros": SVM_PROS,
        "Cons": SVM_CONS
    }
    svm_df = pd.DataFrame(svm_table)
    st.table(svm_df)

def svm_background_what_is_kernel():
    main, image = st.columns([5, 3])
    with main:
        kernel_method_context = """
        Kernel methods, a fundamental part of SVM, allow SVMs to efficiently handle non-linear relationships by 
        transforming the input data into a higher-dimensional feature space. This transformation is achieved using 
        kernel functions, which implicitly represent the data in the higher-dimensional space without explicitly 
        calculating it. This technique is known as the "kernel trick."

        ### Classic Kernel Functions
        Here are three classic kernel functions used in SVM. These three classic kernel functions provide 
        flexibility to SVMs in capturing various types of relationships between features and labels. 
        The choice of the kernel function depends on the characteristics of the data and the problem at hand.

        1. Linear Kernel:
        The linear kernel is the simplest kernel function and is used when the data is expected to be linearly 
        separable. It represents the dot product between two vectors in the original feature space. The linear 
        kernel is mathematically defined as:
        
            $ K(x, x') = x · x' $
        
            where x and x' are input feature vectors.

        2. Polynomial Kernel:
        The polynomial kernel allows SVMs to capture non-linear relationships by mapping the input data into 
        a higher-dimensional space using polynomial functions. The polynomial kernel is defined as:
    
            $ K(x, x') = (γ · x · x' + r)^d $
    
            where γ is a scaling factor, r is a coefficient, and d is the degree of the polynomial.

        3. Gaussian Radial Basis Function (RBF) Kernel:
        The RBF kernel is widely used in SVM and is effective in capturing complex non-linear relationships. 
        It measures the similarity between two data points based on the Euclidean distance between them in the 
        original feature space. The RBF kernel is defined as:
    
            $ K(x, x') = exp(-γ · ||x - x'||^2) $
    
            where γ is a parameter that determines the kernel's bandwidth.

        
        """
        st.markdown(kernel_method_context)
    
    with image:
        st.image('https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_001.png')

def svm_background_how_hyperplane_works():
    main, image = st.columns([5, 3])
    
    with main:
        hyperplane_context = """
        The hyperplane is a fundamental concept that plays a crucial role in the classification and regression 
        tasks. A hyperplane can be thought of as a decision boundary that separates different classes or helps 
        in making predictions.

        ### Hyperplane in Linear SVM
        In linear SVM, the hyperplane is a subspace that divides the feature space into two regions corresponding 
        to different classes. For binary classification, the hyperplane can be represented by a linear equation 
        of the form:

            $ w · x + b = 0 $
        where w is the normal vector to the hyperplane, x represents the input feature vector, and b is the 
        bias term.

        The hyperplane's orientation and position are determined by the weights w and the bias b. Points on one 
        side of the hyperplane are classified as one class, while points on the other side belong to the other class.
        
        ### Support Vectors
        Support vectors are the data points that lie closest to the hyperplane and influence its position. 
        These points have a significant impact on the SVM's decision boundary and its generalization performance. 

        ### Margin
        The margin in SVM refers to the region between the hyperplane and the nearest points from each class, 
        which are the support vectors. It measures the separability of the data and can help find the 
        optimal hyperplane. The goal of SVM is to find a hyperplane that maximizes this margin, known as 
        the maximum margin hyperplane.

        ### Soft Margin and C Parameter
        In practice, the data might not always be perfectly separable. To handle such cases, SVM allows for the 
        introduction of a slack variable that permits misclassifications. This approach is known as the soft margin. 
        The parameter C controls the trade-off between maximizing the margin and allowing misclassifications. 
        A smaller C value leads to a wider margin but potentially more misclassifications, while a larger C value 
        allows fewer misclassifications but a narrower margin.
        """
        st.markdown(hyperplane_context)
    with image:
        st.image("https://hands-on.cloud/wp-content/uploads/2021/12/Overview-of-supervised-learning-SVM.png")
