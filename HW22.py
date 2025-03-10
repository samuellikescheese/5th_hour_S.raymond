#Name: samuel
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class items:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.weight = weight
        self.cost = cost

    def xcost2(self):
        applesauce.cost *= 2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
banana = items(2000, 5, 2)
applesauce = items(50, 10, 500)
raiseeens = items(200, 4, 30)
#3. Print the stock of all three objects and the cost of the second store item.
print (banana.stock)
print (applesauce.stock)
print (raiseeens.stock)
print (applesauce.cost)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
applesauce.xcost2()
print (applesauce.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
raiseeens.stock /= 4
print (raiseeens.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del banana
try:
    print (banana.weight)
except:
    print ("cheese")