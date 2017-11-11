def setup():
    print("setup")


def test():
    while True:
        print("test")


def destroy():
    print("desroy")


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        test()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
