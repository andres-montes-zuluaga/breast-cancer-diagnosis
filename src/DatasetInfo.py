from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTextEdit)

class DatasetInfo(QWidget):
    def __init__(self, breast_cancer):
        super().__init__()
        layout = QVBoxLayout(self)
        
        # Main title
        title = QLabel("Dataset Information")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)
        
        # Dataset information
        info_text = QTextEdit()
        info_text.setReadOnly(True)
        info_text.setStyleSheet("""
            QTextEdit {
                font-family: Arial;
                font-size: 12px;
                background-color: white;
                border: 1px solid #ccc;
                padding: 10px;
            }
        """)

        dataset_info = f"""
WISCONSIN BREAST CANCER DATASET (DIAGNOSTIC)
===========================================

General Information:
------------------
- Total number of samples: {breast_cancer.data.shape[0]}
- Number of features: {breast_cancer.data.shape[1]}
- Classes: {', '.join(breast_cancer.target_names)}

Description:
-----------
This dataset contains features computed from fine needle aspirate (FNA) images 
of breast masses. These features describe the characteristics of the cell nuclei 
present in the images.

Features used in the analysis:
------------------------------
The features are grouped into three main categories, and for each feature, 
the mean, standard error, and "worst" value (mean of the three largest values) are calculated:

1. RADIUS: Mean distance from center to points on the perimeter
2. TEXTURE: Standard deviation of gray-scale values
3. PERIMETER: Size of the core perimeter
4. AREA: Area of the core
5. SMOOTHNESS: Local variation in radius lengths
6. COMPACTNESS: (perimeter² / area - 1.0)
7. CONCAVITY: Severity of concave portions of the contour
8. CONCAVE POINTS: Number of concave portions of the contour
9. SYMMETRY: Symmetry of the core
10. FRACTAL DIMENSION: "Coastline approximation" - 1

Complete list of measured features (30 in total):"""
       
        info_text.setText(dataset_info)
        layout.addWidget(info_text)

        
        # Features table
        features_table = QTextEdit()
        features_table.setReadOnly(True)
        features_table.setStyleSheet("""
            QTextEdit {
                font-family: Courier;
                font-size: 12px;
                background-color: white;
                border: 1px solid #ccc;
                padding: 10px;
            }
        """)
        
        # Organize features into a table
        features_info = "\nIndex  | Feature\n"
        features_info += "-" * 50 + "\n"
        
        for idx, name in enumerate(breast_cancer.feature_names):
            features_info += f"{idx+1:3d}     | {name}\n"
        
        features_table.setText(features_info)
        layout.addWidget(features_table)
        
        # Additional note
        note = QLabel("""Note: Each feature represents a specific measurement 
                     of the cell nucleus and is important for determining 
                     whether a mass is benign or malignant.""")
        note.setWordWrap(True)
        note.setStyleSheet("font-style: italic; color: #666;")
        layout.addWidget(note)