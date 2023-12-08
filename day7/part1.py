import sys
sys.path.append("../")
import utils

answer = 0

lines = utils.get_lines_input("input.txt")

superiority = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

for line in lines:
    hand, rank = line.split(' ')

    indieces = []

    for letter in hand:
        indieces.append(superiority.index(letter))

    p = []
    for i in indieces:
        if i not in p:
            p.append(i)
    k = []
    for j in p:
        k.append(indieces.count(j))
    
    
    
    print("="*60)

    
    
