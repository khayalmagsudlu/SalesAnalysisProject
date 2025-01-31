
def total_sale_revenue_category(df):
    """Hər bir məhsul kateqoriyasına görə ümumi satış miqdarı və gəlir """
    total_revenue_sale=df.groupby("category")[["quantity","total_price"]].sum()
    return total_revenue_sale



def category_most_sale_product(df):
    """Hər bir məhsul kateqoriyasında ən çox satılan məhsul"""
    sales=df.groupby(["category","product_name"])["quantity"].sum().reset_index()
    max_sales=sales.groupby("category")["quantity"].transform("max")
    result=sales[sales["quantity"] == max_sales]
    return result



def avarage_sale_category(df):
    """Hər bir məhsul kateqoriyası üzrə orta satis dəyəri"""
    avarage_sale=df.groupby("category")["total_price"].sum()
    total_sale=df.groupby("category")["quantity"].sum()
    result=avarage_sale/total_sale
    return result

def sales_channel_bycategory(df):
    """Hər bir satış kanalında məhsul kateqoriyalarına görə satışların paylanması"""
    sales_channel=df.groupby(["sales_channel","category"])["quantity"].sum()
    total_sales_channel=df.groupby("sales_channel")["quantity"].sum()
    calculator=sales_channel / total_sales_channel
    result=calculator.reset_index()
    result.columns=["sales_channel","category","quantity"]
    return result