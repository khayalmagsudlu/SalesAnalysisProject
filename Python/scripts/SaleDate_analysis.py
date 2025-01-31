import pandas as pd

def get_yearly_sales_count(df):
    """Hər il üzrə satışların ümumi sayı"""
    df["sale_date"]=pd.to_datetime(df["sale_date"],errors="coerce")
    yearly_sales=df.groupby(df["sale_date"].dt.year)["quantity"].sum()
    return yearly_sales


def get_yearly_sales_totalprice(df):
    """Ən çox satış gəliri  əldə edilən il"""
    df["sale_date"]=pd.to_datetime(df["sale_date"],errors="coerce")
    yearly_sales_price=df.groupby(df["sale_date"].dt.year)["total_price"].sum()
    max_sales_year=yearly_sales_price.idxmax()
    max_sales=yearly_sales_price.max()
    return f"Date: {max_sales_year} TotalPrice: {max_sales}"


def get_monthly_sales_revenue(df):
    """Hər ay üzrə satışların ümumi sayı"""
    df["sale_date"]=pd.to_datetime(df["sale_date"],errors="coerce")
    monthly_sales=df.groupby(df["sale_date"].dt.month)["quantity"].sum()
    result=monthly_sales.reset_index()
    result.columns=["Sale_date","Total_sale"]
    return result


def get_most_sale_month(df):
    """en cox satis olan ay ve sayi"""
    df["sale_date"]=pd.to_datetime(df["sale_date"],errors="coerce")
    most_sale_product=df.groupby([df["sale_date"].dt.month,"product_name"])["quantity"].sum()
    result = most_sale_product.reset_index()
    result.columns = ["Sale_date", "Product Name", "Quantity"]
    max_sale = result.loc[result["Quantity"].idxmax()]
    return max_sale
