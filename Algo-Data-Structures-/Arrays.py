'''
Arrays
stock_prices = [298,200,302,301,292]
In python these are dynamic arrays, size can grow, dimensional arrays
Retrieve O(1)
 stock_prices[0]
Insert O(1)
 stock_prices.insert(1, 292) or append for adding to backDelete O(1) 
 stock_prices.remove(1)

Exercise 
-Let us say your expense for every month are listed below,
    * January - 2200
    * February - 2350
    * March - 2600
    * April - 2130
    * May - 2190
'''
#Create a list to store these monthly expenses and using that find out
exp = [2200,2350,2600,2130,2190]
#1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:",exp[1]-exp[0])
#2. Find out your total expense in first quarter (first three months) of the year.
print("Expense for first quarter:",exp[0]+exp[1]+exp[2])
#3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in exp)
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Expenses at the end of June:",exp)
#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp)