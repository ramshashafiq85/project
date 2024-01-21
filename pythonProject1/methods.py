a = {}
b = set()
print(a, type(a))
print(b, type(b))
dict1 = {"good": "something pleasant",  "fetch": "to bring" , "1": "the number 1"}
print(dict1["good"])
marks = {"ramsha": 50 , "mirha": 45 , "shaheer": 56 , "zayyan": 46 , "shafiq": 34
         }
print(marks["ramsha"])
print(marks["ramsha" or "mirha"])
marks["cucumber"] = 34
print(marks)
print(marks.get("ramsha"))
print(marks.get("ahmed"))
print(marks.values())
print(marks.items())
print(marks.items())
