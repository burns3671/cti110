# sales prediction 
# Date 9/19/18
# CTI-110 P2T1 - Sales Prediction
# omega burns
#

#Get the Projected total sales.
total_sales = float (input('Enter the projected sales: '))

# Calculated the profit as 23% of total sales.
profit = total_sales * 0.23

# Display the profit
print('The profit is $', format(profit, ',.2f'))
