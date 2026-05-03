import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])
print("First five rows:")
print(data.head())
average_age = round(data["Age"].mean(),2)
print(f"Average age: {average_age}")
filtered_students = data[data["Grade"]<="B"]
print("Students with a grade up to B")
print(filtered_students)



# write your code here..

