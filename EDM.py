import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("~/Downloads/XTern 2024 Artificial Intelegence Data Set.xlsx")
Year1_data = data[data['Year'] == 'Year 1']
Year2_data = data[data['Year'] == 'Year 2']
Year3_data = data[data['Year'] == 'Year 3']
Year4_data = data[data['Year'] == 'Year 4']

Indiana_State_Data = data[data['University'] == 'Indiana State University']
Ball_State_Data = data[data['University'] == 'Ball State University']
Butler_Data = data[data['University'] == 'Butler University']


#Plotting the number of orders for each menu item
order_counts = data['Order'].value_counts()
print(order_counts)
order_counts.plot(kind='bar')
plt.xlabel('Menu Item')
plt.xticks(fontsize=6)
plt.ylabel('Count')
plt.title('Counts of Each Menu Item')
plt.show()

#Menu items ranked by popularity among the Year 1s
Year1_orders = Year1_data['Order'].value_counts()
print(Year1_orders)
Year1_orders.plot(kind='bar')
plt.xlabel('Menu Item')
plt.xticks(fontsize=6)
plt.ylabel('Count')
plt.title('Year 1 Orders')
plt.show()


#Menu items ranked by popularity among the Year 2s
Year2_orders = Year2_data['Order'].value_counts()
print(Year2_orders)
Year2_orders.plot(kind='bar')
plt.xlabel('Menu Item')
plt.xticks(fontsize=6)
plt.ylabel('Count')
plt.title('Year 2 Orders')
plt.show()



#Menu items ranked by popularity among the Year 3s
Year3_orders = Year3_data['Order'].value_counts()
print(Year3_orders)
Year3_orders.plot(kind='bar')
plt.xlabel('Menu Item')
plt.xticks(fontsize=6)
plt.ylabel('Count')
plt.title('Year 3 Orders')
plt.show()


#Menu items ranked by popularity among the Year 1s
Year4_orders = Year4_data['Order'].value_counts()
print(Year4_orders)
Year4_orders.plot(kind='bar')
plt.xlabel('Menu Item')
plt.xticks(fontsize=6)
plt.ylabel('Count')
plt.title('Year 4 Orders')
plt.show()

#Menu items ranked by popularity among Indiana State University
Indiana_State_Orders = Indiana_State_Data['Order'].value_counts()
print(Indiana_State_Orders)
Indiana_State_Orders.plot(kind='bar')
plt.xlabel('Menu Item')
plt.xticks(fontsize=6)
plt.ylabel('Count')
plt.title('Indiana State Orders')
plt.show()

#Menu items ranked by popularity among Ball State University
Ball_State_Orders = Ball_State_Data['Order'].value_counts()
print(Ball_State_Orders)
Ball_State_Orders.plot(kind='bar')
plt.xlabel('Menu Item')
plt.xticks(fontsize=6)
plt.ylabel('Count')
plt.title('Ball State Orders')
plt.show()

#Menu items ranked by popularity among the Butler University
Butler_Orders = Butler_Data['Order'].value_counts()
print(Butler_Orders)
Butler_Orders.plot(kind='bar')
plt.xlabel('Menu Item')
plt.xticks(fontsize=6)
plt.ylabel('Count')
plt.title('Butler Orders')
plt.show()
