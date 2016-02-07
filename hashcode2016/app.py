from hashcode2016.blob import Blob
from hashcode2016.config import Config


def run():
    config = Config('input')
    for row in config.grid:
        print row

    #pablo todo
    blob = Blob()


if __name__ == "__main__":
    run()