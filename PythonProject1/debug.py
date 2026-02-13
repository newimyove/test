import traceback


def example2():
    try:
        # 多层函数调用
        func1()
    except Exception as e:
        print("=== 异常详细信息 ===")

        # 获取异常的回溯对象
        tb = traceback.extract_tb(e.__traceback__)

        print(f"异常类型: {type(e).__name__}")
        print(f"异常信息: {str(e)}")
        print("\n调用栈追踪:")

        for frame in tb:
            print(f"  文件: {frame.filename}")
            print(f"  行号: {frame.lineno}")
            print(f"  函数: {frame.name}")
            print(f"  代码: {frame.line}")
            print(f"  {'─' * 40}")


def func1():
    func2()


def func2():
    # 这里会引发异常
    raise ValueError("这是一个测试异常，发生在 func2 中")

if __name__ == '__main__':
    func2()