def get_most_profitable_product(df):
    """Ən çox gəlir gətirən məhsul"""
    profitable_product=df.groupby('product_name')['profit'].sum().reset_index()
    result=profitable_product.loc[profitable_product['profit'].idxmax()]
    return result



def most_sale_5_product(df):
    """Ən Çox Satış Edilən 5 Məhsul"""
    sale_product=df.groupby("product_name")["quantity"].sum().sort_values(ascending=False).head(5)
    return sale_product


def get_most_sale_product(df):
    """Ən çox satılan məhsul"""
    most_sale_product=df.groupby("product_name")["quantity"].sum().idxmax()
    return most_sale_product


def profit_percentage_product(df):
    """Hər bir məhsul üçün ümumi mənfəət faizi"""
    df["profit_percentage"]=(df["profit"]/df["total_price"]*100)
    result=df[["product_name","profit_percentage"]]
    return result
