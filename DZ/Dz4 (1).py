year = input ('Put Year \n')
month = input ('Put month \n')
day = input ('Put day \n')
print ('Correct' if 0 < year else 'Incorrect')
print ('Correct' if 1 <= month <= 12 else 'Incorrect')
print ('Correct' if 1 <= day <= 31 else 'Incorrect')