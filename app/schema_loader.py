# schema_loader.py
from sqlalchemy import create_engine, inspect

def load_schema(connection_string):
    engine = create_engine(connection_string)
    inspector = inspect(engine)
    schema = {}
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema[table_name] = [col['name'] for col in columns]
    return schema
