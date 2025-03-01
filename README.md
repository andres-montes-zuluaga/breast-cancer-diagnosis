# breast-cancer-diagnosis
Breast cancer diagnosis with Perceptron

# Breast Cancer Diagnosis with Perceptron

> Classification project using a perceptron model and the dataset [**Breast Cancer Wisconsin (Diagnostic)**](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) from the UCI Machine Learning Repository.

---

## Index

- [Description](#description)
- [Screenshots / Demo](#screenshots--demo)
- [Main Features](#main-features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contribution](#contribution)
- [License](#license)
- [Authors and Credits](#authors-and-credits)
- [Contact](#contact)

---

## Description

This project implements a **perceptron** model for breast cancer diagnosis. The **Breast Cancer Wisconsin (Diagnostic)** dataset is used, and it was developed using Python and libraries such as **NumPy**, **pandas**, **matplotlib**, and **scikit-learn**. The goal is to correctly classify between benign and malignant cases based on features extracted from the data.

---

## Screenshots / Demo

![image](https://github.com/user-attachments/assets/3a9644e2-1afa-45d9-81f7-8276a4449469)


---

## Main Features
- Perceptron Implementation: Binary classification algorithm.
- Data Preprocessing: Exploratory analysis, cleaning, and normalization.
- Model Evaluation: Calculation and visualization of performance metrics such as precision and recall.
- Interactive Visualizations: Graphs and diagrams that facilitate the interpretation of results.
Note: These elements ensure that the project is understandable and reproducible.

---

## Prerequisites
Before installing the project, make sure you have the following tools installed:

Tool	            Minimum Version
- Python	            3.7
- NumPy	              1.18
- pandas	            1.0
- matplotlib	        3.0
- scikit-learn	      0.22

Recommendation: Use a virtual environment to avoid dependency conflicts.

---

## Installation
Follow these steps to set up the project on your machine:

1. **Clone the repository**:
**Open Git bash**
git clone https://github.com/user/diagnosis-cancer-perceptron.git

2. **Access the project directory**:
**Open Git bash**
cd diagnosis-cancer-perceptron

3. **Create and activate a virtual environment** (optional, but recommended):
- Linux/Mac:
Open Git bash
python3 -m venv env
source env/bin/activate

- Windows:
Open Git bash
python -m venv env
env\Scripts\activate

4. **Install dependencies**:
Open Git bash
pip install -r requirements.txt

---

## Usage
To run the analysis and model training...

---

## Configuration
You can customize some aspects of the project:

Perceptron Parameters: Modify the learning rate and the number of iterations in the notebook.
Dataset Path: Change the path if you want to use another dataset.

In Python:
### Example configuration in the file
LEARNING_RATE = 0.01
NUM_ITERATIONS = 1000

---

## Contribution
Contributions are welcome! Follow these steps to collaborate:
1. Fork this repository.
2. Create a branch for your change:
Open Git bash
git checkout -b feature/new-feature
3. Make your changes and commit:
Open Git bash
git commit -am "Added new feature"
4. Send a Pull Request with a detailed description of your changes.

Reminder: Make sure to follow the contribution guidelines to maintain project consistency.

---

## License
This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). To view a copy of this license, visit [this link](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

---

## Authors and Credits
- Andrés MONTES ZULUAGA – Main developer.
- Inspired by the dataset from the UCI Machine Learning Repository.

---

## Contact
For questions or inquiries, you can contact me at:
andres.montes-zuluaga@laplateforme.io
