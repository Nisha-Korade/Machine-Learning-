from sklearn.metrics import confusion_matrix
#Actual Result
y_true=[1,0,1,1,0,1,0,0,1,0]
#Predict Value
y_predict=[1,0,1,0,0,0,1,1,0,1]
#Creating Object
cm=confusion_matrix(y_true,y_predict)
print("Confusion Matrix :")
print(cm)



