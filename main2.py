import sys
import configparser
import time

from gwcreator.FsCli import FsCli

def main(args, config):
    while True:
        freeswitch_config = config["Freeswitch"]
        cli = FsCli(freeswitch_config.get("CliPath"))
        cli.rescan()
        time.sleep(5) 


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    main(sys.argv[1:], config)
