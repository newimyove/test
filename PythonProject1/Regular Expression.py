import re


def simple():
    result = re.match('w', 'wyw')
    if result:
        print(result.group())


def more_alpha():
    text = "hello123world"
    result1 = re.match('[a-z]+', text)  # 从开头匹配连续字母
    if result1:
        print(f"more_alpha()匹配连续字母: {result1.group()}")


def single():
    result2 = re.match('[a-z]', 'x123')  # 匹配单个小写字母
    if result2:
        print(f"single()匹配特定单个字母: {result2.group()}")


if __name__ == '__main__':
    simple()
    more_alpha()
    single()
