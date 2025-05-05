# Create SVM classifier with linear kernel
svm_model = SVC(kernel='linear', C=1.0)
svm_model.fit(X_train, y_train)