from sklearn.linear_model import LogisticRegression

#hours Studied Input
X=[[1],[2],[3],[4],[5]]
#0=Pass and 1=Fail
y=[0,0,1,1,1]

#Creating Object 
model=LogisticRegression()
model.fit(X,y)

#Taking input for prediction
hours=float(input("Enter How Many Hours You Studied :"))
result=model.predict([[hours]])[0]

if result==1:
    print(f"Based on Hours {hours} you are likely to Pass.")
else:
    print(f"Based on Hours {hours} you are likely to Fail.")
