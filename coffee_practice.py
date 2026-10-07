import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["A","B","C"])

coffee=pd.read_csv('coffee.csv')
cf=coffee.sort_values(["Units Sold","Coffee Type"],ascending=[0,1])
print(cf)