def first_function():
    x = "Hello Welcome to pyhton 3!"
    return x


def second_function(x):
    import time
    for i in x:
        print(i,end="")
        time.sleep(0.5)

second_function(first_function())

