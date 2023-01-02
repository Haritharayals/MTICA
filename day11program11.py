sample_dict={
    "name":"Hari",
    "age":25,
    "salary":8000,
    "city":"Banglore"}
keys=["name","salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
