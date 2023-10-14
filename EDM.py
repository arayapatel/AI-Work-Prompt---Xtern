import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("~/Downloads/XTern 2024 Artificial Intelegence Data Set.xlsx")
Year1_data = data[data['Year'] == 'Year 1']
Year2_data = data[data['Year'] == 'Year 2']
Year3_data = data[data['Year'] == 'Year 3']
Year4_data = data[data['Year'] == 'Year 4']

#print(Year2_data.head)

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