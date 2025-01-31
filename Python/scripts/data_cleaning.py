import pandas as pd


def clean_data(df):
    df.fillna(method="ffill",inplace=True)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
    number_columns=["quantity","cost_price","price","total_price","profit","discount"]
    for i in number_columns:
        if i in df.columns:
            df[i]=pd.to_numeric(df[i],errors="coerce")
    df=df[(df[number_columns]>0).all(axis=1)]
    q1 = df["price"].quantile(0.25)
    q3 = df["price"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df = df[(df["price"] >= lower_bound) & (df["price"] <= upper_bound)]

    if "sale_date" in df.columns:
        df["sale_date"] = pd.to_datetime(df["sale_date"],errors="coerce")


    df.reset_index(drop=True,inplace=True)


    return df
