# query_runner.py
from sqlalchemy import create_engine
import pandas as pd

def run_query(conn_str, query):
    engine = create_engine(conn_str)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df
