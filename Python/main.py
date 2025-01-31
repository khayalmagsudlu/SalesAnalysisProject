import pandas as pd
from scripts.data_cleaning import clean_data 
from scripts.sales_analysis import *
from scripts.customer_analysis import *
from scripts.product_analysis import *
from scripts.category_analysis import *
from scripts.discount_analysis import *
from scripts.region_analysis import *
from scripts.returns_analysis import *
from scripts.SaleDate_analysis import *
from Visual.visual_matplotlib import *
import  os
# CSV file
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "Data", "global_sales_analysis_data.csv")
df = pd.read_csv(file_path)

# Data Cleaning
df=clean_data(df)

#Sales analytics
print(get_total_number_sales(df))
print(get_highest_totalprice(df))
print(get_payment_method(df))
print(returns_sale_percentage(df))

# Customer analytics.
print(get_customer_most_purchases(df))
print(get_customer_avarage_sales(df))
print(customer_order(df))
print(customer_order_return_status(df))


# Product analytics
print(get_most_profitable_product(df))
print(get_most_sale_product(df))
print(profit_percentage_product(df))
print(most_sale_5_product(df))


# Category analytics.
print(total_sale_revenue_category(df))
print(category_most_sale_product(df))
print(avarage_sale_category(df))
print(sales_channel_bycategory(df))


# SaleDate analytics.
print(get_yearly_sales_count(df))
print(get_yearly_sales_totalprice(df))
print(get_monthly_sales_revenue(df))
print(get_most_sale_month(df))


# Regional analytics.
print(get_most_sales_region(df))
print(get_returns_sales(df))
print(region_by_productprofit(df))
print(region_by_categorydiscount(df))


# Discount analytics.
print(get_highest_discount(df))
print(get_discount_product(df))

# Return analytics.
print(returns_sale_percentage(df))
print(returns_order_count(df))


# Visual Matplotlib.
print(plot_category_most_sale_product(df)) 
print(plot_most_sale_5_product(df))
print(plot_yearly_sales_count(df))
print(plot_get_monthly_sales_revenue(df))











