import pandas as pd

# Write a program that will load the “football.csv” dataset into a dataframe called “foot_ball”. 

read_dataset=pd.read_csv("C:\\Users\\user\\Downloads\\dataset - 2020-09-24.csv")

foot_ball={(read_dataset)}

foot_ball=pd.DataFrame(read_dataset)

print(foot_ball)

# inspect the dataframe by listing and displaying the last 7 rows of the dataframe using a single python statement.

print(read_dataset.tail(7))

"""3.3 Write python statements to:
3.3.1 Access and display the "Nationality" and "Club" columns for the first all players. (2)
3.3.2 Access and display the data for the tenth player in the dataset using row index. (2)
3.3.3 Access and display the "Goals" and "Appearances" for players with index positions 
100 to 110."""

#3.3.1 Access and display the "Nationality" and "Club" columns for the first all players.
filter=read_dataset[read_dataset["Nationality"],["Club"]]
print(filter)

#3.3.2 Access and display the data for the tenth player in the dataset using row index.

print(foot_ball(10))




