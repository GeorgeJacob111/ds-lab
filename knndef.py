from math import sqrt

def e_dis(r1,r2):
 dist=0.0
 for i in range(len(r1)-1):
  dist+=(r1[i]-r2[i])**2
  return sqrt(dist)

def get_ne(train,test_row,num_neig):
 distances=list()
 for train_row in train:
  dist=e_dis(test_row,train_row)
  distances.append([test_row,train_row])
  distances.sort(key=lambda tup:tup[1])
  neighbors=list()
  for i in range(num_neig):
   neighbors.append(distances[i][0])
   return neighbors

def predict_classif(train,test_row,num_neig):
 neighbors = get_ne(train,test_row,num_neig)
 out_val=[row[-1] for row in neighbors]
 prediction=max(set(out_val),key=out_val.count)
 return prediction

dataset=[[2.734,2.55,0],
 [1.45,3.36,0],
 [2.334, 2.355, 0],
 [1.45, 3.36, 0],
 [2.334, 2.55, 0],
 [1.45, 3.336, 0],
 [3.334, 3.55, 1],
 [1.45, 3.36, 1],
 [3.734, 4.55, 1],
 [3.45, 4.36, 1],
 [4.734, 5.55, 1],
 [3.45, 5.36, 1]]

prediction=predict_classif(dataset,dataset[0],3)
print('Excpected %d,Got %d'%(dataset[0][-1],prediction))