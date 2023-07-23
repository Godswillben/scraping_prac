import pandas as pd

states = ["California", "Texas", "Florida", "New York"]
populations = [39613493, 29730311, 21944577, 19299981]

dict_states = {'States':states, 'Population':populations}

df_states = pd.DataFrame.from_dict(dict_states)
# print(df_states)
df_states.to_csv('states.csv')

# with open("test.json", 'w') as file:
#     file.write('{"msg":"Data successfully scraped!", "age":1}')
