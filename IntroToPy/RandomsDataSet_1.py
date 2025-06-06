import pandas
from RandomNumber import RandomNumber

r1 = RandomNumber(10, 0)
r1.add_index(1)
r1.add_index(2)

j1 = r1.to_json()
print(j1)
r2 = RandomNumber.from_json(j1)
print(r2)
