################################
# File Name: main.py
# Econ 252 project
# Jeremiah Smith
# 07/22/2014
################################
from functions import *
import sys

#variables
totalCost = []
price = []
quantity = []

totalRev = []
averageTotalCost = []
marginalCost = []
marginalRev = []
netRev = []


endProgram = False #for main program loop

#processing file input for quantity, totalCost and price
getInputData(sys.argv[1], quantity, totalCost, price)

#calculate TR, ATC, MC, MR, NR and populate respective lists
fillLists(quantity, price, totalCost, totalRev, averageTotalCost, marginalCost, marginalRev, netRev)
 
while (endProgram != True):
    printMenu()
    
    answer = int(raw_input())
    
    
    if (answer == 1): 
        printTableData(quantity, price, totalCost, totalRev, averageTotalCost, marginalCost, marginalRev, netRev)
        
    elif (answer == 2):
        graphRevenueCost(totalRev, totalCost, quantity)
        
    elif (answer == 3):
        graphMarginalRevCostATC(marginalRev, marginalCost, price, averageTotalCost, quantity)
        
    elif (answer == 4):
        graphNetRev(quantity, netRev)
        
    elif (answer == 5):
        printFileInfo()
        
    elif (answer == 6):
        print "Thank You for using ECON 252"
        print "Have a nice day"
        endProgram = True
        
    else:
        print "I will assume you want to exit. Have a nice day!"
        endProgram = True
        
        
        







    
    
    



        
   
    
    
