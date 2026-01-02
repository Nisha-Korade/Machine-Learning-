from sklearn.tree import DecisionTreeClassifier

#input Colour and Shade
X=[[7,2],[8,3],[9,8],[10,9]]
#0=Apple and 1=Orange
y=[0,0,1,1]

#Creating Object
model=DecisionTreeClassifier()
model.fit(X,y)

#Taking input for prediction
Colour=float(input("Enter the Colour:"))
Shade=float(input("Enter the Shade:"))
result=model.predict([[Colour,Shade]])[0]

if result==0:
    print("This is likely an Apple.")
else:
    print("This is likely an Orange.")