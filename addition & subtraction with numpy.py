# Muhammad Ilman Mughni
# NPM: 2006537324
# Program penjumlahan dan pengurangan matriks dengan numpy

import numpy as np

a = np.array ([[12, 5, 7], 
               [2, 9, 4]])
b = np.array ([[14, 9, 11], 
               [9, 7, 5]])

print ('select operation:')
print ('1. addition')
print ('2. subtraction')

while True:
    choice = input('enter choice (1/2): ')
    if choice in ('1', '2'):
        if choice == '1':
            print ('addition of two matrices is:')
            print (np.add(a,b))
            break
            
        elif choice == '2':
            print ('subtraction of two matrices is: ')
            print (np.subtract(a,b))
            break
        
    else:
        print ('invalid input!')
        
