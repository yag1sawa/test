import csv

list = [["吉村", "藤枝", "片桐"],
        ["佐藤", "坂田", "坂上"],
        ["細川", "刑部", "村岡"]]

print(list)

with open("/Users/yagisawayuji/practice/list.cvs", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for i in range(0, 3):
        w.writerow(list[i])