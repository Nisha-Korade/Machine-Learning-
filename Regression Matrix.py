from sklearn.metrics import mean_absolute_error,mean_squared_error
import numpy as np 

#Real Score
real_score=[90,60,80,100]
#Machine Guess 
predicted_score=[85,70,70,95]

#Creating Object
mae=mean_absolute_error(real_score,predicted_score)
mse=mean_squared_error(real_score,predicted_score)
rmse=np.sqrt(mse)

#Showing Result
print("MAE:On an Average of by:",mae)
print("MSE:Squared Mistake:",mse)
print("RMSE:Final Realistic Error:",rmse)
