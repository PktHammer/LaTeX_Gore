#!/usr/bin/env python3
def twovarproduct(A,B):
    storedOutput = ''
    for x in range(len(A)):
        for y in range(len(B)):
            storedOutput += '(' + str(A[x]) + ', ' + str(B[y]) + '), '
    storedOutput = storedOutput[:-2] # Slice the last character
    #print(storedOutput)
    storedOutput = latexFormatArray(storedOutput)
    storedOutput = latexMathModeify(storedOutput)

    return storedOutput
    
def latexFormatArray(product):
    product = '\{' + product + '\}'
    return product

def latexMathModeify(toBeMathed): # Temporary, will update with exceptions soon
    toBeMathed = '$' + toBeMathed + '$'
    return toBeMathed

def main():
    # List Defnition
    A = ['twentymillion','w', 'x', 'y', 'z']
    B = ['a', 'infinityplus', 'b']
    
    # Main
    Answer = twovarproduct(A,B)
    
    # Output
    print('Total: ' + str(len(A) * len(B)) + ';', end= ' ')
    print(Answer)

if __name__ == "__main__":
    main()
