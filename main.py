import os
import json

 
with open( 'data.json', 'r', encoding='UTF-8') as f:
    read_data = json.load(f)

for i in range(len(read_data)):
    print('player: ', read_data[i][0])
    print('games: ', read_data[i][1])
    print('wins: ', read_data[i][2])
    print()

