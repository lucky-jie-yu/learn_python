#实现一个秒表功能
import time

print("按下回车开始计时，按 Ctrl+C 停止计时")

while True:
    try:
        input("")
    except KeyboardInterrupt:
        print("\n已退出")
        break

    start_time = time.perf_counter()
    print("开始计时...")

    try:
        while True:
            elapsed = time.perf_counter() - start_time
            print(f"计时:{elapsed:5.1f}秒", end="\r", flush=True)
            time.sleep(0.1)          # 每 0.1 秒刷新，更平滑
    except KeyboardInterrupt:
        total = time.perf_counter() - start_time
        # 清掉当前行再输出结果
        print("\r" + " " * 30 + "\r", end="")
        print(f"计时结束，总共时间为: {total:.2f} 秒")
        break