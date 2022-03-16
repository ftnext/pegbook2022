def calc(s):
    # +と*では*が先に計算される（*について先に再帰でcalcを呼び出す）ように、+の処理が先
    pos = s.find("+")
    # 見つからなければ-1、先頭で見つかる(0)はありえない
    # ref: https://docs.python.org/ja/3/library/stdtypes.html#str.find
    if pos > 0:
        left = s[:pos]
        right = s[pos + 1 :]
        return calc(left) + calc(right)

    pos = s.find("*")
    if pos > 0:
        left = s[:pos]
        right = s[pos + 1 :]
        return calc(left) * calc(right)
    return float(s)
