# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 3/16/20 4:44 PM
# 文件名称： compressString.py 面试题 01.06. 字符串压缩


def compressString(S: str) -> str:
    if not S:
        return ""
    ch = S[0]
    result = ""
    count = 0
    for s in S:
        if s == ch:
            count += 1
        else:
            result += ch + str(count)
            ch = s
            count= 1
    result += ch + str(count)
    return result if len(result) < len(S) else S


print(compressString("aabcccccaaa"))
result = compressString("abbccd")
print(result)