"""
Breast Cancer Diagnosis using Perceptron
=======================================

This script is the main entry point for the breast cancer diagnosis 
application using the Perceptron model.
"""

import sys
from PyQt5.QtWidgets import QApplication
from sklearn.metrics import accuracy_score, classification_report

from src.load_and_prepare_data import load_and_prepare_data
from src.Perceptron import Perceptron
from src.ResultsWindow import ResultsWindow

def main():
    # Load and prepare data
    X_train, X_test, y_train, y_test, df, breast_cancer = load_and_prepare_data()
    
    # Create and train the model
    perceptron = Perceptron(learning_rate=0.01, n_iterations=1000)
    perceptron.fit(X_train, y_train)
    
    # Make predictions
    y_pred = perceptron.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred,
                                            target_names=['Malignant', 'Benign'])
    
    # Create and display the results window
    app = QApplication(sys.argv)
    window = ResultsWindow(y_test, y_pred, accuracy, classification_rep, breast_cancer)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()