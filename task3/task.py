from io import StringIO
import csv
import math

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')

    n = 0
    R = []


    for row in reader:
      r1 = int(row[0])
      r2 = int(row[1])
      r3 = int(row[2])
      r4 = int(row[3])
      r5 = int(row[4])

      R.append([r1, r2, r3, r4, r5])
      n += 1

    H = 0.0

    for node in R:
      probabilities = []

      for ri in node:
        probabilities.append(ri * 1.0 / (n - 1))

      node_H = 0.0

      for p in probabilities:
         if (p != 0):
          node_H += p * math.log(p, 2)

      H -= node_H

    return H

print(task("1,0,4,0,0\n2,1,2,0,0\n2,1,0,1,1\n0,1,0,1,1\n0,1,0,2,1\n0,1,0,2,1"))

