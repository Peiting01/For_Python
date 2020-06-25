import csv
import pandas as pd
import numpy as np

math = "/Users/USER/Desktop/Project_data/student-mat.csv"
por = "/Users/USER/Desktop/Project_data/student-por.csv"

col_name = ["school", "sex", "age", "address", "famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian", "traveltime", "studytime", "failures", "schoolsup",
            "famsup", "paid", "activities", "nursery", "higher", "internet", "romantic", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"]
math_df = pd.read_csv(math)[col_name].dropna()

his = {}
total_data = []

for i in range(len(math_df["school"])):
    temp = []
    for col in col_name:
        temp.append(math_df[col][i])
    temp += [0, 0, 0]
    total_data.append(temp)
# print(total_data)
print(len(total_data))


por_df = pd.read_csv(por)[col_name].dropna()

for i in range(len(por_df["school"])):
    temp = []
    for col in col_name:
        if col == "G1":
            temp += [0, 0, 0]
        temp.append(por_df[col][i])
    total_data.append(temp)
# print(total_data)
print(len(total_data))

# mean
avg_mathG1 = np.mean(math_df["G1"])
avg_mathG2 = np.mean(math_df["G2"])
avg_mathG3 = np.mean(math_df["G3"])
avg_porG1 = np.mean(por_df["G1"])
avg_porG2 = np.mean(por_df["G2"])
avg_porG3 = np.mean(por_df["G3"])

math_avg = [avg_mathG1, avg_mathG2, avg_mathG3]
por_avg = [avg_porG1, avg_porG2, avg_porG3]


for i in total_data[0:395]:
    identified = i[:11]
    identified += [i[19]]
    identified += [i[21]]
    for j in total_data[395:]:
        identified2 = j[:11]
        identified2 += [j[19]]
        identified2 += [j[21]]
        if identified == identified2:
            i[33] = j[33]
            i[34] = j[34]
            i[35] = j[35]
            j[30] = i[30]
            j[31] = i[31]
            j[32] = i[32]

# print(total_data[1043])
A=[]
final_data = []
for i in total_data:
    identified = i[:11]
    identified += [i[19]]
    identified += [i[21]]
    if identified not in A:
        A.append(identified)
        final_data.append(i)
print(len(final_data))

for data in final_data:
    if data[30:33] == [0, 0, 0]:
        data[30:33] = math_avg
    elif data[33:] == [0, 0, 0]:
        data[33:] = por_avg
print(len(final_data))


#write
col_name = ["school", "sex", "age", "address", "famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian", "traveltime", "studytime", "failures", "schoolsup", "famsup",
            "paid", "activities", "nursery", "higher", "internet", "romantic", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences", "matG1", "matG2", "matG3", "porG1", "porG2", "porG3"]

new_file = "/Users/USER/Desktop/output2.csv"
with open(new_file,'a', newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(col_name)

    for data in final_data:
        writer.writerow(data)
