"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
# creating a list for salespeople to be added to 
melons_sold = []
# creating a list for all the melons that were sold 

f = open('sales-report.txt')
#opens the text file and assigns it to a variable-- though the variable name isn't very intutive. 
# it propably should be 'Sales_Report'. 
for line in f:
    #for loop that reads each line in the text 
    line = line.rstrip()
    # then it removes any trailing white space or arguments (if any are passed in) after a string.
    entries = line.split('|')
    #splits lines that we created previously into a list of strings. Now we have a list to work with. 


    salesperson = entries[0]
    # assigns salesperson to the first row in our list 
    melons = int(entries[2])
    # assigns melons as an integer to the third row in our list 

    if salesperson in salespeople:
        #'if statement' that checks our list
        # if that person is already in the 'salespeople' list, it 
        # moves to the next name
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
        # uses 'position' to check melons sold to see if the amount 
        #matches

    else:
        salespeople.append(salesperson)
        #else assigns the salesperson to the list 'salespeople'
        melons_sold.append(melons)
        # it also assigns melons to the 'melons_sold' list 


for i in range(len(salespeople)):
    # loops over 'salespeople' and uses it to create an index for salespeople 
    # and melons_sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
    # generates the report showing who sold which melons 
