from sklearn.neighbors import KNeighborsClassifier

#input weight and size
X=[[100,7],[200,7.5],[250,8],[300,8.5],[330,9],[360,9.5]]
#0=Apple and 1=Orange
y=[0,0,0,1,1,1]

#Creating Object
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)

#Taking input for prediction
weight=float(input("Enter Weight in gm :"))
size=float(input("Enter Size in cm :"))
prediction=model.predict([[weight,size]])[0]

if prediction==0:
    print("This is likely an Apple.")
else:
    print("This is likely an Orange.")