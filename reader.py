import os
import pandas as pd
from sqlite3 import Connection
from conf import cols


def read_excel_to_sqlite(filepath: str, conn: Connection):
    """
    Read all excel files in a directory and insert the data into a sqlite database.
    """
    files = []
    cursor = conn.cursor()
    for filename in os.listdir(filepath):
        if filename.endswith(".xlsx") and not filename.startswith('~$'):
            tablename = filename.split('.')[0]
            files.append(tablename)
            df = pd.read_excel(os.path.join(filepath, filename), dtype=str)
            df.to_sql(tablename, conn, if_exists="replace", index=False)
            if len(cols[tablename]) != 0:
                for col in cols[tablename]:
                    cursor.execute('ALTER TABLE "{}" ADD COLUMN "{}" TEXT'.format(tablename, col))
    conn.commit()
    return files
