# Machine Learning Learning Repository

A comprehensive collection of Machine Learning implementations and projects demonstrating various ML algorithms, techniques, and real-world applications using Python and scikit-learn.

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Topics Covered](#topics-covered)
- [Projects](#projects)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Datasets](#datasets)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository serves as a comprehensive learning resource for Machine Learning enthusiasts and practitioners. It contains Jupyter notebooks covering fundamental to advanced ML concepts, complete with practical implementations using real-world datasets.

## 📁 Repository Structure

```
.
├── 1_Linear Regression/          # Simple & Multiple Linear Regression
├── 2_Encoders/                   # Label, One-Hot, and Ordinal Encoding
├── 3_Scaling/                    # Feature Scaling techniques
├── 4_Polynomial Regression/      # Polynomial feature engineering
├── 5_Regularization/             # Ridge, Lasso, and Elastic Net
├── 6_Logistic Regression/        # Binary & Multi-class Classification
├── 7_Column Transformer/         # Pipeline and preprocessing
├── 8_KNN/                        # K-Nearest Neighbors
├── 9_Decision Tree/              # Decision Tree algorithms
├── 10_Ensemble Methods/          # Random Forest, Boosting
├── 11_SVM/                       # Support Vector Machines
├── 12_Count Vectorizer/          # Text feature extraction
├── 13_Naive Bayes/               # Probabilistic classifiers
├── 14_K Means Clustering/        # Unsupervised learning
├── 15_PCA/                       # Dimensionality reduction
├── Datasets/                     # All datasets used in projects
└── Project/                      # Real-world ML projects
    ├── Crop Yield Prediction/
    └── House Price Prediction/
```

## 📚 Topics Covered

### 1. **Supervised Learning**
   - **Regression**
     - Linear Regression (Simple & Multiple)
     - Polynomial Regression
     - Regularization techniques (Ridge, Lasso, Elastic Net)
   
   - **Classification**
     - Logistic Regression
     - K-Nearest Neighbors (KNN)
     - Decision Trees
     - Random Forest
     - Support Vector Machines (SVM)
     - Naive Bayes

### 2. **Unsupervised Learning**
   - K-Means Clustering
   - Principal Component Analysis (PCA)

### 3. **Data Preprocessing**
   - Feature Encoding (Label, One-Hot, Ordinal)
   - Feature Scaling (Standard Scaler, Min-Max Scaler)
   - Column Transformer
   - Pipeline creation

### 4. **Natural Language Processing**
   - Count Vectorizer
   - Text classification

### 5. **Model Optimization**
   - Hyperparameter tuning with GridSearchCV
   - Cross-validation
   - Model evaluation metrics

## 🚀 Projects

### 1. House Price Prediction
Predict house prices using various regression techniques and feature engineering.

### 2. Crop Yield Prediction
Forecast crop yields based on agricultural and environmental factors.

## 🛠️ Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Jupyter Notebook or JupyterLab
- Git (for version control)
- Git LFS (for large dataset files)

### Requirements

Create a `requirements.txt` file with the following dependencies:

```
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
notebook>=6.4.0
scipy>=1.7.0
```

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pavan953/Machine_Learning.git
   cd Machine_Learning
   ```

2. **Install Git LFS** (required for large datasets)
   ```bash
   # macOS
   brew install git-lfs
   
   # Ubuntu/Debian
   sudo apt-get install git-lfs
   
   # Windows (with Chocolatey)
   choco install git-lfs
   ```

3. **Initialize Git LFS**
   ```bash
   git lfs install
   git lfs pull
   ```

4. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Activate on macOS/Linux
   source venv/bin/activate
   
   # Activate on Windows
   venv\Scripts\activate
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

## 💻 Usage

1. Navigate to the topic folder you want to explore
2. Open the corresponding Jupyter notebook
3. Run the cells sequentially to understand the implementation
4. Modify parameters and experiment with different approaches

### Example: Running Linear Regression

```python
# Navigate to 1_Linear Regression folder
# Open c1_sd.ipynb
# Follow the step-by-step implementation:
# 1. Load and explore data
# 2. Split data into training and testing sets
# 3. Create and train the model
# 4. Evaluate model performance
```

## 📊 Datasets

The `Datasets/` folder contains various datasets used throughout the notebooks:

- **creditcard_cc.csv** - Credit card fraud detection (143.84 MB, tracked with Git LFS)
- **bengaluru_house_prices_bhp.csv** - House price data
- **Salary_dataset_sd.csv** - Experience vs Salary data
- **loan_approval_dataset_lad.csv** - Loan approval data
- **spam_s.csv** - Spam detection dataset
- And many more...

## 📝 Best Practices

- Always explore and preprocess your data before modeling
- Split data into training and testing sets
- Use cross-validation for robust model evaluation
- Apply feature scaling when necessary
- Compare multiple models before selecting the best one
- Document your experiments and findings

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

## 📫 Contact

For questions or suggestions, please open an issue on GitHub.

## 🙏 Acknowledgments

- scikit-learn documentation and community
- Kaggle for datasets
- The open-source ML community

---

**Note**: This repository is for educational purposes. Feel free to use the code and notebooks for learning and experimentation.
