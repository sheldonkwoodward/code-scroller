# sheldon woodward
# 4/24/18

from code_scroller import CodeScroller
from sys import argv


def main():
    try:
        speed = argv[1]
    except IndexError:
        speed = 100
    c = CodeScroller()
    c.scroll(speed_ms=int(speed))


if __name__ == '__main__':
    main()
