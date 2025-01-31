from typing import Any
import time, random, string


def generate_uid():
    # 获取当前时间戳，转换为整数形式
    timestamp = int(time.time())
    # 生成一个包含所有字母（大小写）和数字的字符集
    characters = string.ascii_letters + string.digits
    # 将时间戳转换为字符串
    timestamp_str = str(timestamp)
    # 初始化一个空字符串用于存储最终的 UID
    uid = ""
    # 循环 10 次来生成 10 位的 UID
    for i in range(10):
        # 如果时间戳字符串还有字符可用，则随机选择使用时间戳字符或字符集中的字符
        if i < len(timestamp_str):
            uid += random.choice(timestamp_str + characters)
        # 如果时间戳字符串已用完，则只从字符集中选择字符
        else:
            uid += random.choice(characters)
    return uid


class Person:
    def __init__(self, **kwargs):
        """
        create a man without info, it should exist objectively
        """
        self.uid = generate_uid()
        for key, value in kwargs.items():
            # 将键值对设置为类实例的属性
            setattr(self, key, value)
        """
        it should be exist but without must
        mother、father、birthday、uid
        """



p = Person(name='xu', age=20)
for item in dir(p):
    if "__" not in item:
        print(item)
        print(getattr(p, item))