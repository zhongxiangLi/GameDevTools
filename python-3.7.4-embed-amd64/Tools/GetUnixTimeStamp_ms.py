import time

def run():
    now = time.time()
    now = (int(now * 1000))#python3 只有int代表整形 没有long
    print(now)

if __name__=="__main__":
    run()