# # # import csv


# # # with open("weather_data.csv") as data_file:
# # #     data = csv.reader(data_file)
# # #     print(data)
# # #     temperatures = []
    
    
# # #     for row in data:
# # #         if row[1] != "temp":
# # #             temperatures.append(row[1])
        
# # #     print(temperatures)

# import pandas 

# # data = pandas.read_csv("weather_data.csv")
# # # # print(type(data))

# # # # print(data)

# # # data_dict = data.to_dict()
# # # # print(data_dict)

# # # temp_list = data["temp"].to_list()


# # # # print(data["temp"].max())

# # # # print(data["condition"])

# # # print(data.condition)

# # # # Get data in row 


# # print(data[data.day == "Monday"])





# # monday = data[data.day == "Monday"]
# # print(monday.temp)

# # fahr = (monday.temp * 9/5 + 32)
# # print(fahr)







# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }


# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# # print(data[data.temp == data.temp.max()])

import pandas


data = pandas.read_csv("squirrel_count.csv")

fur_col = data["Primary Fur Color"]

cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, cinnamon, black]
}

print(data_dict)

data = pandas.DataFrame(data_dict)
data.to_csv("squirrels.csv")