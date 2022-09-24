import pandas as pd

pokemon_data = 'Dataset/pokemon_data.csv'
poke = pd.read_csv(pokemon_data)
 
y = poke.Attack
poke_features = ['HP', 'Defense', 'Speed']
x = poke[poke_features]
print(x.describe())
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
'''
alphabeticalPoke = poke.sort_values('Name')
for index, row, in poke.iterrows():
    print(alphabeticalPoke['Name'])
'''

# ADDING NEW COLUMN BY ADDING VALUES OF OTHER COLUMNS:
    # poke['Combat Stats'] = poke['Attack']+ poke['Sp. Atk'] + poke['Sp. Def']
    # print(poke.head(5))