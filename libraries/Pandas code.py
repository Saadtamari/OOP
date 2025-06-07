# Pandas
import pandas as pd

df = pd.read_excel("C:/Users/user/OneDrive/سطح المكتب/Test.xlsx",
                  # index_col=0, na_values=["NAN","NA"] , 
                   sheet_name = "Sheet1")
print(df)

#NA  NAN
### DataFram Name . ColName
print("....\n")
#print(df.name) 
#print( df[ ["name","age"] ] ) # F name
#print(df["name"])

### min max mean sample describe

#print(df.describe())
#print(df.sample(3))

### sort 

#print(df.sort_values(by="GPA",ascending = True))
print(df.sort_values(by=["name","GPA"],ascending = [True,False] ))
#df.sort_values(by=["name","GPA"],ascending = [True,False] , inplace = True )
print("..........\n")
print(df)

### agg
# m3_GPA = df["GPA"].agg([max,min,sum])
print("..........\n")
# print(m3_GPA)

print(df["name"].agg(sum))
print(df[ ["age","GPA"] ].agg([min,max,sum]) ) 


