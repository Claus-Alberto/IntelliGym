import sqlite3

class SQLiteCRUD:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    
    def create_table(self, table_name, columns):
        columns_str = ", ".join([f"{column['name']} {column['type']}" for column in columns])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(query)
        self.connection.commit()
    
    def insert(self, table_name, values):
        columns = ", ".join(values.keys())
        placeholders = ":" + ", :".join(values.keys())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()
    
    def select(self, table_name, columns=None, where=None, join=None):
        columns_str = "*" if not columns else ", ".join(columns)
        where_str = "" if not where else f"WHERE {where}"
        join_str = "" if not join else f"{join}"
        query = f"SELECT {columns_str} FROM {table_name} {join_str} {where_str}"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def update(self, table_name, values, where=None):
        set_values = ", ".join([f"{key}=:{key}" for key in values.keys()])
        where_str = "" if not where else f"WHERE {where}"
        query = f"UPDATE {table_name} SET {set_values} {where_str}"
        self.cursor.execute(query, values)
        self.connection.commit()
    
    def delete(self, table_name, where=None):
        where_str = "" if not where else f"WHERE {where}"
        query = f"DELETE FROM {table_name} {where_str}"
        self.cursor.execute(query)
        self.connection.commit()
