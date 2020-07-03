# -*- coding:utf-8 -*-
import re


def my_highlight(text, q):
    """自定义标题搜索词高亮函数，忽略大小写"""
    if len(q) > 1:
        try:
            text = re.sub(q, lambda a: '<span class="highlighted">{}</span>'.format(a.group()),
                          text, flags=re.IGNORECASE)
        except BaseException as e:
            pass
    return text


if __name__ == '__main__':
    result = my_highlight("我是中国人", "中国")
    print(result)