import pandas as pd
data = pd.read_csv('data.csv')


print('ex1')
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
#print(data)

print('ex2')
rez = data[data['Age'] > 40].head(10)
(print(rez))

print('ex3')
rez = data[(data['Overall'] >= 85) & (data['Age'] < 25)].head
print(rez)

print('ex4')
rez = data.sort_values(by='Skill Moves' , ascending=False).head
print(rez)

print('ex5')
rez = data[data['Contract Valid Until'] == '2021']
print(rez)

print('ex6')
print(data.shape)
print(data['Name'].nunique())

print('ex7')
print(data['Nationality'].value_counts().head(5))