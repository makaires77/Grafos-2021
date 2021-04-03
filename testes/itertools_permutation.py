"""
https://www.pythonpool.com/python-permutations/
Exemplos com a função de permutação do Módulo Itertools
"""
from itertools import permutations
a=permutations([1,2,3])
print(list(a),"\n")

from itertools import permutations 
a=permutations([1,2,3]) 
for i in a: 
   print(i) 