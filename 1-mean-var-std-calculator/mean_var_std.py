import numpy as np

def calculate(list):
  if not len(list)==9:
    raise ValueError("List must contain nine numbers.")

  arr = np.array([list[i] for i in range(len(list))])
  newarr = arr.reshape(3, 3)
  newarr = newarr.astype('float64')

  calculations = {
  'mean': [np.mean(newarr, axis = 0).tolist(), np.mean(newarr, axis = 1).tolist(), np.mean(newarr)],
  'variance': [np.var(newarr, axis = 0).tolist(), np.var(newarr, axis = 1).tolist(), np.var(newarr)],
  'standard deviation': [ np.std(newarr, axis = 0).tolist(), np.std(newarr, axis = 1).tolist(), np.std(newarr)],
  'max': [np.max(newarr, axis = 0).tolist(), np.max(newarr, axis = 1).tolist(), np.max(newarr)],
  'min': [np.min(newarr, axis = 0).tolist(), np.min(newarr, axis = 1).tolist(), np.min(newarr)],
  'sum': [np.sum(newarr, axis = 0).tolist(), np.sum(newarr, axis = 1).tolist(),np.sum(newarr)]
  }
  return calculations