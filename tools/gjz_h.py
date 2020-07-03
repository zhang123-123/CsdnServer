# -*- coding:utf-8 -*-
import re


def my_highlight(text, q):
    """自定义标题搜索词高亮函数，忽略大小写"""
    if len(q) > 1:
        try:
            text = re.sub(q, lambda a: '|{}|'.format(a.group()),
                          text, flags=re.IGNORECASE)
            text = text.split("|")
        except BaseException as e:
            pass
    return text


if __name__ == '__main__':
    result = my_highlight("我是中国人python", "Python")
    print(result)
