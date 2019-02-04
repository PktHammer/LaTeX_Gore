#!/usr/bin/env python3

# TabuLogicChartHeaderMaker.py
# Creates tables with the format
# | IVs(1+) || Negations(0+) || Intermediates(0+) || Final Answers(1+) |
#
# Sample Output: 
# \begin{tabu} spread 0pt{|X|X||X[2c]|X[2c]||X[3c]|X[3c]||X[7c]|} \hline
# $ivar0$ & $ivar1$ & $nega0$ & $nega1$ & $intr0$ & $intr1$ & $final0$  \\\hline{|=|=#=|=#=|=#=|}
# \end{tabu} 
#
### MODIFY THESE VARIABLES ###

# Headers
HEADERSTRING = '\\begin{tabu} spread 0pt{'
IVAR_ALIAS = 'ivar'
NEG_ALIAS = 'nega'
INTERMED_ALIAS = 'intr'
FINALANS_ALIAS = 'final'

# Footer
OUTLINECLOSETABU = '\\end{tabu}'

# Input Variables
INDEPENDENTVARIABLES = 2
INDEPENDENTVARIABLESIZE = 1
NEGATIONS = 2
NEGSIZE = 2
INTERMEDIATES = 2
INTERMEDIATESIZE = 3
FINALANSWERS = 1
FINALANSWERSIZE = 7

### DONT TOUCH BELOW THIS LINE ###

# Concat formatted loop
def concatLoop(count, tempOneSize, alias, sliceOffTwo):
    catOne = ''
    catTwo = ''
    for itr in range(count):
        catOne += 'X'
        if tempOneSize == 1:
            catOne += '|'
        else:
            catOne += '[' + str(tempOneSize) + 'c]|'
        catTwo += '$' + alias + str(itr) + '$ & '        
    if sliceOffTwo > 0:
        catTwo = catTwo[:-(sliceOffTwo)]
    return catOne, catTwo # Ret Tuple

# Add the header string to c1
def addHeader():
    tempOne = HEADERSTRING
    return tempOne

# Superfunction - addElement, does all the below:
    # Add a column+sz to C1, add '$var#$ & '  in C2
    # Add a column+sz to C1, add '$neg#$ & ' in C2
    # Add a column+sz to C1, add '$intr#$ & ' in C2
    # Add a final answer to C1, add '$finalANS$' in C2, final slicer
def addElement(typeCount, typeSize, alias, sliceOffTwo):
    tempOne = '|'
    tempTwo = ''
    catOne, catTwo = concatLoop(typeCount, typeSize, alias, sliceOffTwo)
    tempOne += catOne
    tempTwo += catTwo
    return tempOne, tempTwo # Ret Tuple

# Add Super Ugly Closer That Handles Closing
def addCloser(independentVariables, negations, intermediates, finalAnswers):
    # Format Line One
    tempOne = '} \\hline' # Prints } \hline ender

    # Format Line Two
    titleFormatting = '|'
    for itr in range(independentVariables):
        titleFormatting += '=|'
    # Splice last | and turn it into a #
    titleFormatting = titleFormatting[:-1] 
    # Continue for negations and intermediates
    if negations > 0:
        titleFormatting += '#'
        for itr in range(negations):
            titleFormatting+= '=|'
        titleFormatting = titleFormatting[:-1]
    if intermediates > 0:
        titleFormatting += '#'
        for itr in range(intermediates):
            titleFormatting += '=|'
        titleFormatting = titleFormatting[:-1]
    # Adjust for final answers
    if finalAnswers > 0:
        titleFormatting += '#'
        for itr in range(finalAnswers):
            titleFormatting += '=|'
        #titleFormatting = titleFormatting[:-1] # - Do not remove the last one on the FA sector
    # Concatenate line two
    tempTwo = ' \\\\\\hline{' + titleFormatting + '}' # Prints \\\hhline{|=|=|=#=|=#=|} -like output 

    return tempOne, tempTwo # Ret Tuple

def main():
    ### Import Static Variables ###
    independentVariables = INDEPENDENTVARIABLES
    independentVariableSize = INDEPENDENTVARIABLESIZE
    negations = NEGATIONS
    negSize = NEGSIZE
    intermediates = INTERMEDIATES
    intermediateSize = INTERMEDIATESIZE
    finalAnswers = FINALANSWERS
    finalAnswerSize = FINALANSWERSIZE
    ###

    # Initialize outputs
    outLineOne = ''
    outLineTwo = ''

    # Import Close Tabu line
    outLineCloseTabu = OUTLINECLOSETABU

    # Zeroing temps probably not needed but meh lol
    tempOne = ''
    tempTwo = ''

    # Add Header to L1
    tempOne = addHeader()
    outLineOne += tempOne

    # Add IVs to L1/L2
    tempOne, tempTwo = addElement(independentVariables,independentVariableSize,IVAR_ALIAS,0)
    outLineOne += tempOne
    outLineTwo += tempTwo

    # Add Negations to L1/L2
    tempOne, tempTwo = addElement(negations, negSize,NEG_ALIAS,0)
    outLineOne += tempOne
    outLineTwo += tempTwo

    # Add Intermediates to L1/L2
    tempOne, tempTwo = addElement(intermediates, intermediateSize, INTERMED_ALIAS, 0)
    outLineOne += tempOne
    outLineTwo += tempTwo

    # Add Final Answer to L1/L2
    tempOne, tempTwo = addElement(finalAnswers,finalAnswerSize,FINALANS_ALIAS,2)
    outLineOne += tempOne
    outLineTwo += tempTwo

    # Add Closers to L1/L2
    tempOne, tempTwo = addCloser(independentVariables,negations,intermediates, finalAnswers)
    outLineOne += tempOne
    outLineTwo += tempTwo

    # Print outputs
    print(outLineOne)
    print(outLineTwo)
    print(outLineCloseTabu)


if __name__ == "__main__":
    main()
