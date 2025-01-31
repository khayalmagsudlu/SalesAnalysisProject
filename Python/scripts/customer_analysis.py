def get_customer_most_purchases(df):
    """ən çox alış-veriş edən müştəri"""
    most_purchases=df.groupby("customer_name")["quantity"].sum().reset_index()
    result=most_purchases.loc[most_purchases["quantity"].idxmax()]
    return result


def get_customer_avarage_sales(df):
    """Müştərilərin orta alış dəyəri"""
    customer_total=df.groupby("customer_name")["total_price"].sum()
    customer_order=df.groupby("customer_name")["total_price"].count()
    avarage_sales=customer_total/customer_order
    return avarage_sales



def customer_order(df):
    """Müştərilər ən çox hansı məhsul kateqoriyasından alış-veriş etdiyinin tapilmasi"""
    order=df.groupby(["customer_name","category"])["quantity"].sum().reset_index()
    highest_order_value=order["quantity"].max()
    result=order[order["quantity"] == highest_order_value]
    return result


def customer_order_return_status(df):
    """Musterilerin daha çox geri qaytardiqi categoriya"""
    order_return=df[df["return_status"] == "Returned"].groupby(["customer_name","category"])["quantity"].sum().reset_index()
    order_return_value=order_return["quantity"].max()
    result=order_return[order_return["quantity"] == order_return_value]
    return result




