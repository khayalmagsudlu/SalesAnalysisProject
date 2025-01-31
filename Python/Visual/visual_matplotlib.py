import matplotlib.pyplot as plt
from scripts.sales_analysis import *
from scripts.customer_analysis import *
from scripts.product_analysis import *
from scripts.category_analysis import *
from scripts.discount_analysis import *
from scripts.region_analysis import *
from scripts.returns_analysis import *
from scripts.SaleDate_analysis import *



def plot_category_most_sale_product(df):
    result=category_most_sale_product(df)
    plt.figure(figsize=(12,12))
    category=result["category"]
    products=result["product_name"]
    quantity=result["quantity"]
    bars=plt.bar(category,quantity,color="skyblue")
    for bar, product, qty in zip(bars, products, quantity):
        plt.text(
            bar.get_x() + bar.get_width() / 2,  
            bar.get_height() + 1,  
            f"{product}\n{qty}", 
            ha="center", va="bottom", fontsize=8
        )
    plt.xlabel("Category")
    plt.ylabel("Quantity")
    plt.title("Hər Kateqoriyada Ən Çox Satılan Məhsul")
    plt.show()

def plot_most_sale_5_product(df):
    product=most_sale_5_product(df)
    plt.figure(figsize=(10,8))
    bars=plt.bar(product.index,product.values,color="orange")
    for i in bars:
        plt.text(
            i.get_x() + i.get_width() / 2,
            i.get_height(),
            f'{i.get_height():,.0f}',
            ha="center",
            va="bottom",
            fontsize=10
        )
    plt.title("Ən Çox Satış Edilən 5 Məhsul")
    plt.xlabel("Products")
    plt.ylabel("Total")
    plt.tight_layout()
    plt.show()




def plot_yearly_sales_count(df):
    result = get_yearly_sales_count(df)
    years = result.index
    quantity = result.values
    plt.figure(figsize=(10, 6))
    bars = plt.bar(years, quantity, color="skyblue")
    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2,  
            bar.get_height() + 1,  
            f"{bar.get_height()}",
            ha="center", va="bottom", fontsize=10
        )

    plt.title("Hər İl Üzrə Satış Sayı")
    plt.xlabel("İl")
    plt.ylabel("Satış Miqdarı")
    plt.xticks(rotation=45)  
    plt.tight_layout()
    plt.show()


def plot_get_monthly_sales_revenue(df):
    result=get_monthly_sales_revenue(df)
    month=result["Sale_date"]
    quantity=result["Total_sale"]
    plt.figure(figsize=(10, 6))
    bars=plt.bar(month,quantity,color="orange")
    for i in bars:
        plt.text(
            i.get_x() + i.get_width() / 2,
            i.get_height() + 1,
            f"{i.get_height()}",
            ha="center",
            fontsize=8
        )
    plt.title("Hər ay üzrə satışların ümumi sayı")
    plt.xlabel("Months")
    plt.ylabel("Quantity")
    plt.xticks(month,["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.tight_layout()
    plt.show()