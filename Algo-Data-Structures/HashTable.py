'''
Hash Map

Retrieve O(1)
Insert O(1)
Delete O(1) 

'''


teams = {
'Colorado' : 'Rockies',
'Boston'   : 'Red Sox',
'Minnesota': 'Twins',
}

#get
teams["Colorado"]

#loops
for key, value in teams.items():
    print(key,value)

for key in teams:
    print(key)