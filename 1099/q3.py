"""
Subtract two numbers

500
 99
= 401
  
0->10->4
9->9
^

1->0->4
"""


def subtract(node_x, node_y):



from typing import List

"""
500
 99
"""

 def subtract(a: str, b: str) -> str:                                                                                                                                                                           
      if len(a) < len(b) or (len(a) == len(b) and a < b):                                                                                                                                                        
          return subtract(b, a) 
                                                                                                                                                                                   
      b = b.zfill(len(a))                                                                                                                                                                                        
      res = []                                                                                                                                                                                                   
      borrow = 0  
      for i in range(len(a) - 1, -1, -1):                                                                                                                                                                        
          d = int(a[i]) - int(b[i]) - borrow                                                                                                                                                                     
          borrow = 1 if d < 0 else 0
          res.append(str(d % 10))                                                                                                                                                                                
      return ''.join(reversed(res)).lstrip('0') or '0'
