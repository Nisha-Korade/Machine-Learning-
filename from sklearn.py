from sklearn.preprocessing import LabelEncoder
import pandas as pd 

df=pd.read_csv("cleaned_cafe_sales_data.csv")

df_label=df.copy()
le=LabelEncoder()
#Label Encoding
df_label['Location_encoded']=le.fit_transform(df_label['Location'])

#One-Hot Encoding
df_ONE=pd.get_dummies(df_label,columns=["Payment Method"])

print('\nLabel Encoded Data Frame')
print(df_label[['Transaction ID','Item', 'Quantity','Price Per Unit','Total Spent','Payment Method','Location','Location_encoded','Transaction Date']].head(10))

print('\nOne-Hot Encoded Data Frame')
print(df_ONE.head(10))


