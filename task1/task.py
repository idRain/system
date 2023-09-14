import sys
import csv

def main():
  file = sys.argv[1]
  print(file)
  row = sys.argv[2]
  col = sys.argv[3]

  with open(file) as f:
    data = list(csv.reader(f, delimiter=","))
    print(data[row][col])
      
