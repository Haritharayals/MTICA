employees=['Hari','Prem','Sharath']
defaults={"destignation":'developer',"salary":80000}

data=dict.fromkeys(employees,defaults)
print(data)
print(data["Hari"])
