# sheldon woodward
# 4/24/18

from os import getcwd, walk
from os.path import expanduser, join
from time import sleep


class CodeScroller:
    def __init__(self):
        self.base_dir = expanduser(getcwd())
        self.files = []
        for root, directories, filenames in walk(self.base_dir):
            for filename in filenames:
                if filename[-3:] == '.py':
                    self.files.append(join(root, filename))

    def scroll(self, speed_ms=100):
        counter = 0
        while True:
            f = open(self.files[counter % len(self.files)])
            while True:
                line = f.readline()
                if line == '':
                    break
                line = line.rstrip('\n')
                print(line)
                sleep(speed_ms * .001)
            print()
            counter += 1
            f.close()
