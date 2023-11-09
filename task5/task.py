import json
import numpy as np

def step_1(str):
    reviews = json.loads(str)

    keys_indexes = dict()
    keys = []

    for ind in range(len(reviews)):
        r = reviews[ind]

        if type(r) is list:
            for el in r:
                keys_indexes[el] = ind
                keys.append(el)
        else:
            keys_indexes[r] = ind
            keys.append(r)

    sorted_keys = keys.copy()
    sorted_keys.sort()
    relations_matrix = []

    for key_i in sorted_keys:
        row = []
        
        for key_j in sorted_keys:
            row.append(1 if (keys_indexes[key_j] >= keys_indexes[key_i]) else 0)
        
        relations_matrix.append(row)

    relations_matrix = np.matrix(relations_matrix)
    return relations_matrix, keys_indexes, keys, sorted_keys

def step_2(matrix_1, matrix_2):
  matrix_12 = np.multiply(matrix_1, matrix_2)

  tr_matrix_12 = np.multiply(np.transpose(matrix_1), np.transpose(matrix_2))

  res_matrix = np.logical_or(matrix_12, tr_matrix_12)
  
  return res_matrix
  
def step_3(keys_1, sorted_keys, keys_indexes_1, keys_indexes_2, matrix_contradictions):
  res = []

  if (len(keys_1) > 0):
    res.append(keys_1[0])

  used_contradictions = set()
  prev = keys_1[0]

  for i in range(1, len(keys_1)):
    cur_val = cur = keys_1[i]
    prev_val = prev[0] if type(prev) == list else prev

    if (cur_val in used_contradictions):
      continue

    cur_contradictions = []
    for j in range(len(keys_1)):
      if (not matrix_contradictions[sorted_keys.index(cur_val), j]):
        val = sorted_keys[j]
        cur_contradictions.append(val)
        used_contradictions.add(val)
    if (len(cur_contradictions) > 0):
      cur = [cur] + cur_contradictions

    if (keys_indexes_1[cur_val] > keys_indexes_1[prev_val] or keys_indexes_2[cur_val] > keys_indexes_2[prev_val]):
      res.append(cur)
    else:
      if (type(cur) != list):
        cur = [cur]

      if (type(prev) != list):
        prev = [prev]
      
      res[len(res) - 1] = prev + cur
    
    prev = cur

  return res

def task(A, B):
    matrix_A, keys_indexes_A, keys_A, sorted_keys_A = step_1(A)
    matrix_B, keys_indexes_B, _, _ = step_1(B)
    
    matrix_contradictions = step_2(matrix_A, matrix_B)

    res = step_3(keys_A, sorted_keys_A, keys_indexes_A, keys_indexes_B, matrix_contradictions)

    return res


print(task(
    '["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]',
    '[["1", "2"], ["3", "4", "5"], "6", "7", "9", ["8", "10"]]'
))