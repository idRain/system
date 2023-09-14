import csv

filename = input()
row = int(input())
col = int(input())

with open(filename) as f:
  data = list(csv.reader(f, delimiter=","))
  print(data[row][col])
      