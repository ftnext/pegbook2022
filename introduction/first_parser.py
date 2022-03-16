def calc(s):
    pos = s.find("+")
    # 見つからなければ-1、先頭で見つかる(0)はありえない
    # ref: https://docs.python.org/ja/3/library/stdtypes.html#str.find
    if pos > 0:
        left = s[:pos]
        right = s[pos + 1 :]
        return float(left) + float(right)
    return float(s)
