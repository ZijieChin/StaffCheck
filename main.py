from reader import read_excel_to_sqlite, clear_tables, export_sqlite_to_excel
from funcs import simple_match, complex_match
from conf import filepath


def main():
    clear_tables()
    read_excel_to_sqlite(filepath)

    simple_match()
    complex_match()

    export_sqlite_to_excel(filepath)


if __name__ == "__main__":
    main()
