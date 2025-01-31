def returns_sale_percentage(df):
    """Satışların neçə faizi qaytarılmasin helli"""
    return_status=df[df["return_status"] == "Returned"]["quantity"].sum()
    sales=df["quantity"].sum()
    result=(return_status/sales)*100
    return f"{result:.2f}% of sales were returned"



def returns_order_count(df):
    """Hər bir məhsul kateqoriyasına görə geri qaytarılmış məhsul sayı"""
    return_order=df[df["return_status"] == "Returned"].groupby("category")["quantity"].count()
    result=return_order.reset_index()
    result.columns=["Category","Returned Product Count"]
    return result
