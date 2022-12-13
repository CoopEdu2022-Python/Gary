def longest_common_prefix(strs: list[str]) -> str:
    g=[]
    for i in range(len(strs)):
        a=len(strs[i])
        g.append(a)
    h=g.index(min(g))
    min_len = strs[h]
    y=[]

    for i in range(len(min_len),1,-1):
        if not sum(y)==len(min_len):
            for c in strs:
                if c ==min_len[0:i]:
                    y.append(1)
                else:
                    y.append(0)
        else:
            return min_len[0:i]
    else:
        return '没有'

