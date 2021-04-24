


df = pandas.read_csv(r'C:\Users\Aashay\Desktop\check.csv')

print(df)

df = df['Mobile']

print(df)

print(len(df))
str1 = ''
for i in range(0, len(df)):
    str1 += str(df[i]) + ','

print(str1)



