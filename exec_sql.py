import sqlite3




def eval_exec_match(db, p_str, g_str, pred=None, gold=None):
    """
    return 1 if the values between prediction and gold are matching
    in the corresponding index. Currently not support multiple col_unit(pairs).
    """
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute(p_str)
        p_res = cursor.fetchall()
    except:
        return "p_res error!" ,"q_res not excute"

    cursor.execute(g_str)
    q_res = cursor.fetchall()

    # def res_map(res, val_units):
    #     rmap = {}
    #     for idx, val_unit in enumerate(val_units):
    #         key = tuple(val_unit[1]) if not val_unit[2] else (val_unit[0], tuple(val_unit[1]), tuple(val_unit[2]))
    #         rmap[key] = [r[idx] for r in res]
    #     return rmap
    #
    # p_val_units = [unit[1] for unit in pred['select'][1]]
    # q_val_units = [unit[1] for unit in gold['select'][1]]
    # return res_map(p_res, p_val_units) == res_map(q_res, q_val_units)
    return p_res,q_res


db='/home/yj/python/Github/syntaxSQL/data/spider/database/'+'concert_singer/concert_singer'+'.sqlite'
p_str='SELECT count(Singer_ID) FROM singer;'
g_str='SELECT count(*) FROM singer;'

p_res, q_res = eval_exec_match(db, p_str, g_str)

print(p_res)
print(q_res)