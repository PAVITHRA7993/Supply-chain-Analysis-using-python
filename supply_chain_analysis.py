# -*- coding: utf-8 -*-
"""Supply Chain Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DwP9JsSO33OPY7T_qvxDfl75YOavij_e

# Supply chain analysis using python

Supply chain analysis is an important aspect of business operations. Python is a popular language for data analysis and visualization, and there are many libraries available to help with supply chain analysis. One such library is Pandas, which is used for data manipulation and analysis. Another library is Plotly, which is used for creating interactive visualizations.

Here is a brief outline of how you can use Python to perform supply chain analysis:

1.Collect data on the different stages of the supply chain, such as sourcing, manufacturing, transportation, inventory management, sales, and customer demographics.

2.Use Pandas to clean and manipulate the data.

3.Use Plotly to create interactive visualizations that help you understand the data.

4.Analyze the data to identify areas where the supply chain can be improved.
"""

#importing the necessary Python libraries
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"

# loading the data
from google.colab import files
uploaded = files.upload()

# read the dataset
data = pd.read_csv("supply_chain.csv")
print(data.head())

# Descriptive statitics of the dataset
print(data.describe())

# Relationship between the price of the products and the revenue generated by them
fig = px.scatter(data, x='Price',
                 y='Revenue generated',
                 color='Product type',
                 hover_data=['Number of products sold'],
                 trendline="ols")
fig.show()

"""The company derives more revenue from skincare products, and the higher the price of skincare products, the more revenue they generate."""

# sales by product type
sales_data = data.groupby('Product type')['Number of products sold'].sum().reset_index()

pie_chart = px.pie(sales_data, values='Number of products sold', names='Product type',
                   title='Sales by Product Type',
                   hover_data=['Number of products sold'],
                   hole=0.5,
                   color_discrete_sequence=px.colors.qualitative.Pastel)

pie_chart.update_traces(textposition='inside', textinfo='percent+label')
pie_chart.show()

"""So 45% of the business comes from skincare products, 29.5% from haircare, and 25.5% from cosmetics."""

# Total revenue generated from shipping  carriers
total_revenue = data.groupby('Shipping carriers')['Revenue generated'].sum().reset_index()
fig = go.Figure()
fig.add_trace(go.Bar(x=total_revenue['Shipping carriers'],
                     y=total_revenue['Revenue generated']))
fig.update_layout(title='Total Revenue by Shipping Carrier',
                  xaxis_title='Shipping Carrier',
                  yaxis_title='Revenue Generated')
fig.show()

"""The company is using three carriers for transportation, and Carrier B helps the company in generating more revenue."""

# Average lead time and Average Manufacturing Costs for all products of the company
avg_lead_time = data.groupby('Product type')['Lead time'].mean().reset_index()
avg_manufacturing_costs = data.groupby('Product type')['Manufacturing costs'].mean().reset_index()
result = pd.merge(avg_lead_time, avg_manufacturing_costs, on='Product type')
result.rename(columns={'Lead time': 'Average Lead Time', 'Manufacturing costs': 'Average Manufacturing Costs'}, inplace=True)
print(result)

"""# Analyzing SKU
SKU stands for Stock Keeping Units. They’re like special codes that help companies keep track of all the different things they have for sale. Imagine you have a large toy store with lots of toys. Each toy is different and has its name and price, but when you want to know how many you have left, you need a way to identify them. So you give each toy a unique code, like a secret number only the store knows. This secret number is called SKU.
"""

revenue_chart = px.line(data, x='SKU',
                        y='Revenue generated',
                        title='Revenue Generated by SKU')
revenue_chart.show()

"""Another column in the dataset as Stock levels. Stock levels refer to the number of products a store or business has in its inventory."""

# stock levels of each SKU
stock_chart = px.line(data, x='SKU',
                      y='Stock levels',
                      title='Stock Levels by SKU')
stock_chart.show()

#Order quality of each SKU
order_quantity_chart = px.bar(data, x='SKU',
                              y='Order quantities',
                              title='Order Quantity by SKU')
order_quantity_chart.show()

"""# Cost Analysis"""

#shipping cost of Carriers
shipping_cost_chart = px.bar(data, x='Shipping carriers',
                             y='Shipping costs',
                             title='Shipping Costs by Carrier')
shipping_cost_chart.show()

""" The Carrier B helps the company in more revenue. It is also the most costly Carrier among the three."""

#cost distribution  by transportation mode
transportation_chart = px.pie(data,
                              values='Costs',
                              names='Transportation modes',
                              title='Cost Distribution by Transportation Mode',
                              hole=0.5,
                              color_discrete_sequence=px.colors.qualitative.Pastel)
transportation_chart.show()

"""Company spends more on Road and Retail modes of transportation for the transportation of goods.

# Analzing Defect Rate
The defect rate in the supply chain refers to the percentage of products that have something wrong or are found broken after shipping.
"""

#Avarage defect rate of all product types
defect_rates_by_product = data.groupby('Product type')['Defect rates'].mean().reset_index()

fig = px.bar(defect_rates_by_product, x='Product type', y='Defect rates',
             title='Average Defect Rates by Product Type')
fig.show()

"""The defect rate of haircare products is higher"""

#Defect rates by mode of transformation
pivot_table = pd.pivot_table(data, values='Defect rates',
                             index=['Transportation modes'],
                             aggfunc='mean')

transportation_chart = px.pie(values=pivot_table["Defect rates"],
                              names=pivot_table.index,
                              title='Defect Rates by Transportation Mode',
                              hole=0.5,
                              color_discrete_sequence=px.colors.qualitative.Pastel)
transportation_chart.show()

"""Road transportation results in a higher defect rate, and Air transportation has the lowest defect rate.

# Summary
Supply Chain Analysis means analyzing various components of a Supply Chain to understand how to improve the effectiveness of the Supply Chain to create more value for customers.
"""