from pylab import *


###########################
#function: getInputData
#inputs: filename, quantity list, totalCost list, price list
#outputs: assign the file inputs to the correct list for processing
###########################
def getInputData(inputFileName, quantity, totalCost, price):
    print "Opening file: {0}\n".format(inputFileName) 
    f = open(inputFileName)
    close()
    print "Processing File: {0}".format(inputFileName)
    for record in f:
        inputLines = record.split("\r")
        
    print('Assigning Input:'),
    for line in inputLines:
        temp = line.split(',')
        quantity.append(float(temp[0]))
        totalCost.append(float(temp[1]))
        price.append(float(temp[2]))
        print('*'),
    print "\n"
    
###########################
#function: fillLists
#inputs: quantity, price, totalCost, totalRev, averageTotalCOst
#inputs: marginalRev, marginalCost, netRev
#outputs: filed lists
###########################
def fillLists(quantity, price, totalCost, totalRev, averageTotalCost, marginalCost, marginalRev, netRev):
    for x in range(len(quantity)):
        totalRev.append(calTotalRevenue(price[x], quantity[x]))
        
        netRev.append(calNetRev(totalRev[x], totalCost[x]))
        if (x == 0):
            marginalCost.append(nan)
            marginalRev.append(nan)
            averageTotalCost.append(nan)
        else:
            marginalCost.append(calMargin(totalCost[x-1], totalCost[x], quantity[x-1], quantity[x]))
            marginalRev.append(calMargin(totalRev[x-1], totalRev[x], quantity[x-1], quantity[x]))
            averageTotalCost.append(calSRATC(totalCost[x], quantity[x]))

###########################
#function: printTableData
#inputs: quantity, price, totalCost, totalRev, averageTotalCost, marginalRev, marginalCost, netRev
#outputs: Table of input data
###########################
def printTableData(quantity, price, totalCost, totalRev, averageTotalCost, marginalCost, marginalRev, netRev):
    print "\n"
    for x in range(37):
        print('-'),
    
    print "\n" 
    print "|   Q    |   TC   |   P    |   TR   |  ATC   |   MC   |  MR    |   NR   |"
    
    for x in range(len(quantity)):
        print "|{0:8}|{1:8}|{2:8}|{3:8}|{4:8.2f}|{5:8.2f}|{6:8.2f}|{7:8}|".format(int(quantity[x]), totalCost[x], price[x], 
                                                                                                               totalRev[x], averageTotalCost[x], marginalCost[x], 
                                                                                                               marginalRev[x], netRev[x])
    for x in range(37):
        print('-'),
        
    print "\n"

###########################
#function: printFileInfo
#inputs: none
#outputs: file information
###########################
def printFileInfo():  
    print "\n"
    print "File Name: main.py"
    print "ECON 252 CH 13/14 Project"
    print "Author: Jeremiah Smith"
    print "Date: 07/22/2014"
    print "\n"

###########################
#function: printFileInfo
#inputs: none
#outputs: file information
###########################
def printMenu():
    for x in range(37):
        print('-'),
    print "\n"
    print "Please Choose an Option Below"
    print "1. Show Table Data"
    print "2. Show Graph for Revenue, Cost vs Quantity"
    print "3. Show Graph for Marginal Revenue, Marginal Cost, ATC vs Quantity"
    print "4. Show Graph for Net Revenue"
    print "5. Show program information"
    print "6. Exit Program"
    for x in range(37):
        print('-'),
    print "\n"
    print('--->'),
    
    
###########################
#function: calTotalRevenue
#description: Calculates total revenue
#inputs: price, quantity
#outputs: Total Revenue
###########################   
def calTotalRevenue(price, quantity):
    return price * quantity

###########################
#function: calSRATC
#description: Calculates short run average total cost
#inputs: totalCost, quantity
#outputs: Short Run ATC
###########################
def calSRATC(totalCost, quantity):
    if (quantity == 0):
        return 0;
    else:
        return totalCost/quantity

###########################
#function: calNetRev
#description: Calculates Net Revenue
#inputs: Total Revenue, Total Cost
#outputs: Net Revenue
###########################
def calNetRev(totalRev, totalCost):
    return totalRev - totalCost

###########################
#function: calMargin
#description: Calculates marginal difference
#inputs: prevMoney, currentMoney, preQuantity, currentQuantity
#outputs: Marginal Difference
###########################
def calMargin(prevMoney, currentMoney, prevquantity, currentquantity):
    changeInquantity = currentquantity - prevquantity
    changeInMoney = currentMoney - prevMoney
    return changeInMoney / changeInquantity

###########################
#function: graphNetRev
#description: Graphs Net Revenue and Quantity on a 2D graph
#inputs: Net Revenue, Quantity
#outputs: 2D Graph
###########################
def graphNetRev(quantity, netRev):
    graphYMin = 0
    graphYMax = 0
    for x in range(len(netRev)):
        if (netRev[x] < graphYMin):
            graphYMin = netRev[x]
            
        if (netRev[x] > graphYMax):
            graphYMax = netRev[x]
    
    figure(facecolor = 'g', edgecolor = 'b')
    title('Net Revenue')
    xlabel('Quantity')
    ylabel('Net Revenue')
    grid('on', which='both', axis = 'both')
    xlim(int(quantity[0]), int(len(quantity)+1))
    ylim(int(graphYMin) - 5, int(graphYMax + 5))
    plot(quantity, netRev, label = 'Net Rev')
    legend(loc = 0)
    show()

###########################
#function: graphRevenueCostATC
#description: Calculates total revenue
#inputs: price, quantity
#outputs: Total Revenue
########################### 
def graphRevenueCost(totalRev, totalCost, quantity):
    figure(facecolor = 'g', edgecolor = 'b')
    title('Revenue and Cost')
    xlabel('Quantity')
    ylabel('Revenue/Cost')
    grid('on')
    
    plot(quantity, totalRev, label = 'TR')
    plot(quantity, totalCost, label = 'TC')
    legend(loc = 0)
    show()

###########################
#function: graphMarginalRevCostATC
#description: Graphs Marginal Revenue, Marginal Cost and Short Run Average Total Cost
#inputs: price, quantity
#outputs: Total Revenue
###########################  
def graphMarginalRevCostATC(marginalRev, marginalCost, price, shortRunATC, quantity):
    figure(facecolor = 'g', edgecolor = 'b')
    title('Marginal Revenue, Cost and ATC')
    xlabel('Quantity')
    ylabel('Revenue/Cost')
    grid('on')
    xlim(quantity[1], quantity[-1])
    
    if(marginalRev[-1] == price[-1]):
        plot(quantity, marginalRev, 'm', label ='MR')
    else:
        plot(quantity, marginalRev, 'm', label = 'MR')
        plot(quantity, price, 'b', label = 'Price')
        
    plot(quantity, marginalCost, 'g', label = 'MC')
    plot(quantity, shortRunATC, 'b', label = 'ATC')
    legend(loc = 0)
    show()

    

