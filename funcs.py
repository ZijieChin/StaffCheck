from sqlite3 import Connection
from conf import dupcols, dupcustomcols
from reader import conn


# 查找两张表中手机号相同但客户号不同的值
def get_dup_from_diff_custom(conn: Connection, table1: str, table2: str, table1phone: str, table2phone: str,
                             table1custom: str, table2custom: str, table2show: str):
    cursor = conn.cursor()
    sql = f'''SELECT {table1}.id, {table2}.{table2show} FROM {table1} INNER JOIN {table2} ON {table1}.{table1phone} = 
        {table2}.{table2phone} WHERE {table1}.{table1custom} != {table2}.{table2custom}'''
    result = cursor.execute(sql).fetchall()
    return result


# 查找两张表中手机号相同的值
def get_dup_phone(conn: Connection, table1: str, table2: str, table1phone: str, table2phone: str, table2show: str):
    cursor = conn.cursor()
    sql = f'''SELECT {table1}.id, {table2}.{table2show} FROM {table1} INNER JOIN {table2} ON {table1}.{table1phone} = 
        {table2}.{table2phone}'''
    result = cursor.execute(sql).fetchall()
    return result


# 处理一个手机号对应多个客户号的情况
def phone_to_multi_customers(reslist: list):
    result_dict = {}
    for item in reslist:
        if item[0] in result_dict:
            result_dict[item[0]] += "\n" + item[1]
        else:
            result_dict[item[0]] = item[1]

    result_list = [(k, v) for k, v in result_dict.items()]
    return result_list


# 将重复项写回数据库
def write_dup_to_db(conn: Connection, dups: list):
    cursor = conn.cursor()
    for dup in dups:
        table = dup['table']
        res = dup['check']
        for r in res:
            if len(r['result']) != 0:
                for item in r['result']:
                    sql = f'''UPDATE {table} SET {r["table"]} = '{item[1]}' WHERE id = {item[0]}'''
                    cursor.execute(sql)
    conn.commit()


# 检查手机号是否重复
def simple_match():
    dups = []
    for col in dupcols:
        table = col['table']
        phone = col['col']
        tabledup = {'table': table, 'check': []}
        for check in col['check']:
            print(f'检查表 {table} 及表 {check["table"]}...')
            result = get_dup_phone(conn, table, check['table'], phone, check['col'], check['show'])
            result = phone_to_multi_customers(result)
            tabledup['check'].append({'table': check['table'], 'result': result})
            dups.append(tabledup)
    write_dup_to_db(conn, dups)


# 检查手机号是否重复，若重复则检查客户号是否相同
def complex_match():
    dups = []
    for col in dupcustomcols:
        table = col['table']
        phone = col['phone']
        custom = col['custom']
        tabledup = {'table': table, 'check': []}
        for check in col['check']:
            print(f'检查表 {table} 及表 {check["table"]}...')
            result = get_dup_from_diff_custom(conn, table, check['table'], phone, check['phone'], custom,
                                              check['custom'],
                                              check['show'])
            result = phone_to_multi_customers(result)
            tabledup['check'].append({'table': check['table'], 'result': result})
            dups.append(tabledup)
    write_dup_to_db(conn, dups)
