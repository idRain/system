import sys
import csv

def main():
  file = sys.argv[1]

  with open(file) as f:
    data = list(csv.reader(f, delimiter=","))
    
    answer_list = solve(data)

    for key, value in answer_list.items():
      print(key, " ".join(value)) 


def solve(edges_list):
  answer = dict()

  for a, b in edges_list:
    if a in answer:
      answer[a].append(b)
    else:
      answer[a] = [b]

    if b in answer:
      answer[b].append(a)
    else:
      answer[b] = [a]
    
  return answer

main()
