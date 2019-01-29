def fun(*ask):
 print(ask)
 for arg in ask:
  print('kwd')

def func(**kwa):
 for a in kwa:
  print('2',a)

q=range(10)
fun(*q)
print(q)
print(list(q))
func(az=1,b=2,c=3)
w=list(range(4))
fun(*w)
