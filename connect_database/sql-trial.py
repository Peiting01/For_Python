import pandas as pd
from pandasql import sqldf, load_births, load_meat

births = load_births()
print(sqldf('SELECT * FROM births where births > 250000 limit 5;', locals()))


q = """
    select
        date(date) as DOB, 
        sum(births) as "Total Births"
    from 
        births 
    group by 
        date
        limit 10;
    """
print(sqldf(q, locals()))
print(sqldf(q, globals()))

def pysqldf(q):
    return sqldf(q, globals())
print(pysqldf(q))

dfcust = pd.read_csv(r"C:\Users\USER\Desktop\Lecture1_data\customers.csv")
print(dfcust.head(3))
print(dfcust.dtypes)
print(pysqldf("""select age as "Cust.Age" from dfcust limit 10;"""))


