import multiprocessing

def worker():
    print("its a multi processing")

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()


