import os

from reader import read_excel_to_sqlite

import sqlite3

from conf import filepath


def main():
    try:
        os.remove("data.db")
    except Exception as e:
        print(e)
        return

    conn = sqlite3.connect("data.db")

    files = read_excel_to_sqlite(filepath, conn)

    for f in files:
        print(f)

    conn.close()


if __name__ == "__main__":
    main()
