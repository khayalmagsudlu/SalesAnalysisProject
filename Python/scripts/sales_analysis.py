def get_total_number_sales(df):
    """Satışların ümumi sayı"""
    return df['sale_id'].nunique()


def get_highest_totalprice(df):
    """Ən yüksək satış gəliri hansı tarixdə baş verdiyi"""
    totalprice=df.groupby("sale_date")["total_price"].sum()
    highest_price=totalprice.max()
    sale_date=totalprice.idxmax()
    return f"{sale_date}: {highest_price}"


def get_payment_method(df):
    """Hər bir ödəniş üsulu üzrə satışların sayı və ümumi gəlir""" 
    sales_count=df.groupby("payment_method")[["quantity","total_price"]].sum()
    return sales_count


def returns_sale_percentage(df):
    """Satışların  qaytarılma faizi"""
    return_status=df[df["return_status"] == "Returned"]["quantity"].sum()
    sales=df["quantity"].sum()
    result=(return_status/sales)*100
    return f"{result:.2f}% of sales were returned"