def get_highest_discount(df):
    """ən yüksək endirim əldə edən satış kateqoriyası """
    highest_discount_category=df.groupby("category")["discount"].sum()
    highest_discount=highest_discount_category.max()
    category_name=highest_discount_category[highest_discount_category == highest_discount].index[0]
    return f"{category_name}: {highest_discount}"


def get_discount_product(df):
    """Endirimli məhsullar ümumi gəlirin neçə faizinin elde etmesi"""
    discount_product=df[df["discount"] > 0]["total_price"].sum()
    total_price=df["total_price"].sum()
    result=(discount_product/total_price)*100
    return f"Discounted products account for {result:.2f}% of total revenue."