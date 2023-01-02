sample_dict={
    "name":"Hari",
    "age":25,
    "salary":8000,
    "city":"Banglore"}
keys=["name","salary"]

res=dict()
for k in keys:
    res.update({k:sample_dict[k]})
print(res)
