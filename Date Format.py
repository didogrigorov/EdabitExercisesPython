# def format_date(date):
#     new_str = ''
#     info = date.split("/")
#     day = info[0]
#     month = info[1]
#     year = info[2]
#     result = year + month + day
#     new_str += result
#     return new_str
#
#
# print(format_date("11/12/2019"))

import re
from collections import deque
def format_date(date):
    pattern = r'[0-9]+'

    result = re.finditer(pattern, date)
    final = []
    top_final = deque(final)

    for item in result:
        result = item.group()
        top_final.appendleft(result)

    return ''.join(top_final)

print(format_date("11/12/2019"))