from sklearn.linear_model import LinearRegression

X=[[1],[2],[3],[4],[5]]
y=[40,50,60,70,90]

#Creating object
model=LinearRegression()
model.fit(X,y)

#Taking input for prediction
hours=float(input("Enter How Many Hours You Studied :"))
predicted_marks=model.predict([[hours]])

#Showing predicted Output
print(f"Based on your Hours {hours} you may score around {predicted_marks}")
