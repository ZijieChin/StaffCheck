import os
import pandas as pd
import sqlite3
from conf import cols

conn = sqlite3.connect("data.db")


def clear_tables():
    """
    Clear all tables in a sqlite database.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    for table in tables:
        cursor.execute('DROP TABLE "{}"'.format(table[0]))
    conn.commit()


def read_excel_to_sqlite(filepath: str):
    """
    Read all excel files in a directory and insert the data into a sqlite database.
    """
    files = []
    cursor = conn.cursor()
    for filename in os.listdir(filepath):
        if filename.endswith(".xlsx") and not filename.startswith('~$'):
            tablename = filename.split('.')[0]
            files.append(tablename)
            df = pd.read_excel(os.path.join(filepath, filename), dtype=str, engine='openpyxl')
            df.to_sql(tablename, conn, if_exists="replace", index=True, index_label="id")
            if len(cols[tablename]) != 0:
                for col in cols[tablename]:
                    cursor.execute('ALTER TABLE "{}" ADD COLUMN "{}" TEXT'.format(tablename, col))
    conn.commit()
    return files


def export_sqlite_to_excel(filepath: str):
    """
    Export all tables in a sqlite database to excel files.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    for table in tables:
        df = pd.read_sql_query("SELECT * FROM {}".format(table[0]), conn)
        out_file_path = os.path.join(filepath, table[0] + '_result.xlsx')
        df.to_excel(out_file_path, index=False)
