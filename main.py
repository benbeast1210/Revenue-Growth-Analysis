import json
with open('/docs/data.json') as data:
  data = json.loads(data)

def revenue_growth(data):
  age = int(input())
  list = list(data.values())

  def rev(age):
     sal = 0
     for i in list:
         if i < age:
            sal = sal + 5
         else:
            sal = sal+20
     return sal
  
  curr_rev = rev(18)
  pred_rev = rev(age)
  growth = int((pred_rev - curr_rev )*100/ curr_rev )
  
  print(growth)
