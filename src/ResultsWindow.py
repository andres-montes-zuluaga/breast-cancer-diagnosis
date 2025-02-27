from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QLabel, QTextEdit, QTabWidget)
from .HelpButton import HelpButton
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sklearn.metrics import confusion_matrix
from .DatasetInfo import DatasetInfo
import seaborn as sns

class ResultsWindow(QMainWindow):
    def __init__(self, y_test, y_pred, accuracy, classification_rep, breast_cancer):
        super().__init__()
        self.setup_ui(y_test, y_pred, accuracy, classification_rep, breast_cancer)
        
    def setup_ui(self, y_test, y_pred, accuracy, classification_rep, breast_cancer):
        """Set up the user interface"""
        self.setWindowTitle("Breast Cancer Analysis")
        self.setGeometry(100, 100, 1250, 600)
        
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Create tabs
        tabs = QTabWidget()
        
        # Results tab
        results_tab = QWidget()
        results_layout = QHBoxLayout(results_tab)
        
        # Left panel for text
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        # Title with help button
        title_layout = QHBoxLayout()
        title = QLabel("Analysis Results")
        title.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }
        """)
        title_layout.addWidget(title)
        
        help_btn = HelpButton(
            "This panel shows the analysis results:\n"
            "- Accuracy: Percentage of correct predictions\n"
            "- Classification report: Detailed metrics by class"
        )
        title_layout.addWidget(help_btn)
        title_layout.addStretch()
        
        left_layout.addLayout(title_layout)

        # Text area for results
        text_results = QTextEdit()
        text_results.setReadOnly(True)
        text_results.setStyleSheet("""
            QTextEdit {
                font-family: Courier;
                font-size: 12px;
                background-color: white;
                border: 1px solid #ccc;
                padding: 10px;
            }
        """)
        
        # Format and display results
        results_text = f"""Model results:
Accuracy: {accuracy:.2%}

Classification report:
{classification_rep}
"""
        text_results.setText(results_text)
        left_layout.addWidget(text_results)

        # Right panel for confusion matrix
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        # Title for the matrix
        matrix_title = QLabel("Confusion Matrix")
        matrix_title.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }
        """)
        right_layout.addWidget(matrix_title)

        # Create and display the confusion matrix
        fig = Figure(figsize=(8, 6))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=['Malignant', 'Benign'],
                    yticklabels=['Malignant', 'Benign'],
                    ax=ax)
        ax.set_title('Confusion Matrix')
        ax.set_ylabel('True')
        ax.set_xlabel('Predicted')
        
        right_layout.addWidget(canvas)

        # Add panels to results layout
        results_layout.addWidget(left_panel, 40)  # 40% of the space
        results_layout.addWidget(right_panel, 60)  # 60% of the space

        # Add tabs
        tabs.addTab(results_tab, "Results")
        tabs.addTab(DatasetInfo(breast_cancer), "Dataset Information")
        
        # Add tabs to main layout
        main_layout.addWidget(tabs)

        # Status bar
        self.statusBar().showMessage("Analysis successfully completed")

        # Set global style
        self.setStyleSheet("""
            QMainWindow {background: #f0f0f0;}
        """)