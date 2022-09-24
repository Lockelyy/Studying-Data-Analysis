import pandas as pd

pokemon_data = 'pokemon_data.csv'
poke = pd.read_csv(pokemon_data)
 
print(poke.Name)