import pandas as pd

pokemon_data = 'pokemon_data.csv'
poke = pd.read_csv(pokemon_data)
 
# PRINT SPECIFIC COLUMNS:
#   print(poke[['Name', 'Type 1', 'HP']])

# PRINT A SPECIFIC ITEM BASED ON ITS INDEX:
#   print(poke.iloc[2,1])

# PRINT OUT ALL ROWS:
# for index, row in poke.iterrows():
 #    print(index, row['Name'])

# PRINT OUT ALL WATER TYPE POKEMON ROWS:
# waterTypes = poke.loc[poke['Type 1'] == 'Water']
# print(waterTypes)

# GET IN DEPTH STATS ON EVERY ROW AND COLUMN:
# poke.describe()