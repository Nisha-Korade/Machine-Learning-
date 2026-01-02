from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd
data={
    'Studyhours':[1,2,3,4,5],
    'Testscore':[40,50,60,70,80]
 }
df=pd.DataFrame(data)

#standard scaler
Standard_scaler=StandardScaler()
standardscaled=Standard_scaler.fit_transform(df)

#minmax scaler
minmax_scaler=MinMaxScaler()
minmax_scaled=minmax_scaler.fit_transform(df)

#train test split
X=df[['Studyhours']]
y=df[['Testscore']]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

print('\ntrain data:')
print(X_train)
print('\nTest data:')
print(X_test)

print('\ntrain data:')
print(y_train)
print('\nTest data:')
print(y_test)

print('\nMinMax Scaler Output:')
print(pd.DataFrame(minmax_scaled,columns=['Studyhours','Testscore']))

print("\nStandard Scaler Output:")
print(pd.DataFrame(standardscaled,columns=['Studyhours','Testscore']))
