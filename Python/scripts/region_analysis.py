def get_most_sales_region(df):
    """Ən çox satış olan bölgə"""
    highest_sales_region=df.groupby("region")["quantity"].sum()
    region_name=highest_sales_region.idxmax()
    high_sales=highest_sales_region.max()
    return f"{region_name}: {high_sales}"

def get_returns_sales(df):
    """Geri qaytarılan satışların sayı regionlar üzrə  bölüşdürülmesi"""
    Returned_count_sales=df[df["return_status"] == "Returned"].groupby("region")["quantity"].sum()
    return Returned_count_sales



def region_by_productprofit(df):
    """Regionlara görə ən çox gəlir gətirən kateqoriya"""
    highest_category=df.groupby(["region","category"])["profit"].sum()
    result=highest_category.reset_index()
    result.columns=["Region","Category","Profit"]
    high_profit=result.loc[result["Profit"].idxmax()]
    return high_profit



def region_by_categorydiscount(df):
    """Regionlara görə endirimlərin daha çox tətbiq edildiyi kateqoriya"""
    highest_discount=df.groupby(["region","category"])["discount"].sum()
    result=highest_discount.reset_index()
    result.columns=["Region","Category","Discount"]
    result = result.sort_values(by="Discount", ascending=False)
    return result
