'''
Created on 2016. 11. 8.

@author: Seungchan Oh
@student_number: 01603277
'''
# partial function
def arranged(prices):
    #definition
    organized = [0]
    #compare elements in organized and prices and insert value into specific location 
    for price in prices:
        for queue in range(len(organized)):
            if organized[queue] >= price: 
                organized.insert(queue, price)
                break
            elif queue == len(organized)-1:
                organized.append(price)
    # remove buffer number
    organized.remove(0)
    return organized

def together(prices):
    # definition
    total = 0
    freeitem = len(prices)//4 # determining the number of list in list
    # activate partial function for arrangement
    organized = arranged(prices)
    # eliminate cheapest prices
    organized=organized[freeitem:]
    # total spend
    for price in organized:
        total += price
    return round(total, 2)

def group(prices):
    # definition
    freeitem = len(prices)//4
    result = list()
    #arrangement
    organized = arranged(prices)
    # separate into series of lists
    for queue in range(freeitem):
        tupled = tuple(organized[-4:][::-1])
        organized = organized[:-4]
        result.append(tupled)
    # append last one
    if len(organized) != 0:
        result.append(tuple(organized[::-1])) 
    return result

def grouped(prices):
    # definition
    total = 0
    tasks = group(prices)
    # combining discounted spends from each list
    for task in tasks:
       total += together(task)
    return total

def profit(prices):
    # difference between collected spend and divided spends
    result = round(together(prices) - grouped(prices), 2)
    return result
        

prices = [3.23, 5.32, 8.23, 2.23, 9.98, 7.43, 6.43, 8.23, 4.23]
print(together(prices))
print(group(prices))
print(grouped(prices))
print(profit(prices))