import pandas as pd
import random as rand
df = pd.read_csv('data.csv')


i = 300

while i>=0:
    new_data = {
        'Temp': rand.randrange(400, 900),
        'Humd': rand.randrange(200,900),
        'Label': 0
    }

    df = df.append(new_data, ignore_index=True)
    i= i-1

df.to_csv("data.csv", index=False)