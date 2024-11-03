import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    try:
        if file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        else:
            raise ValueError("Unsupported format")
        return data
    except Exception as error:
        print(f"Loading error: {error}")
        return pd.DataFrame()

def clean_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe = dataframe.dropna(subset=['CustomerID'])
    dataframe = dataframe[(dataframe['Quantity'] > 0) & (dataframe['UnitPrice'] > 0)]
    return dataframe

def find_loyal_customers(dataframe: pd.DataFrame, min_orders: int) -> pd.DataFrame:
    customer_orders = dataframe.groupby('CustomerID').size()
    loyal_customers = customer_orders[customer_orders >= min_orders].reset_index()
    loyal_customers.columns = ['CustomerID', 'OrderCount']
    return loyal_customers

def calculate_quarterly_sales(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe['InvoiceDate'] = pd.to_datetime(dataframe['InvoiceDate'])
    dataframe['Quarter'] = dataframe['InvoiceDate'].dt.to_period('Q')
    quarterly_sales = dataframe.groupby('Quarter').apply(lambda x: (x['Quantity'] * x['UnitPrice']).sum()).reset_index()
    quarterly_sales.columns = ['Quarter', 'TotalSales']
    return quarterly_sales

def top_products(dataframe: pd.DataFrame, top_n: int) -> pd.DataFrame:
    product_demand = dataframe.groupby('StockCode')['Quantity'].sum().nlargest(top_n).reset_index()
    product_demand.columns = ['StockCode', 'TotalQuantitySold']
    return product_demand

def product_purchase_patterns(dataframe: pd.DataFrame) -> pd.DataFrame:
    product_summary = dataframe.groupby('StockCode').agg({'Quantity': 'mean', 'UnitPrice': 'mean'}).reset_index()
    product_summary.columns = ['StockCode', 'AverageQuantity', 'AverageUnitPrice']
    return product_summary

def answer_conceptual_questions() -> dict:
    return {
        "Q1": "A",
        "Q2": "B",
        "Q3": "C",
        "Q4": "A",
        "Q5": "A"
    }
