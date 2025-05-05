# SVM Sigmoid Kernel & C Parameter Analysis  

🔍 **Exploring how the regularization parameter `C` affects SVM performance with a sigmoid kernel.**  

## **📌 Overview**  
This project investigates:  
✅ How `C` (regularization strength) impacts SVM with a **sigmoid kernel**.  
✅ Comparison with **RBF, linear, and polynomial kernels**.  
✅ Best practices for tuning SVM hyperparameters.  

## **🚀 Quick Start**  
1️⃣ Clone the repo:  
```bash

2️⃣ install depencises :
pip install -r requirements.txt

3️⃣ run the jyupter notebook:
jupyter notebook notebooks/SVM_Sigmoid_Kernel_Analysis.ipynb

📊 Key Findings
✔ Small C (< 0.1) → Underfitting (high bias).
✔ Optimal C (1-10) → Best generalization.
✔ Large C (> 100) → Overfitting (high variance).

Accuracy vs. C
Training accuracy across different C values.

🛠 Scripts
train_svm.py → Train SVM with different kernels & C values.

visualize.py → Plot decision boundaries.

