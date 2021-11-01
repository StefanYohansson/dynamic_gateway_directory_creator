import sys
import configparser
import random
import time
from multiprocessing import Pool

from gwcreator.FsCli import FsCli
from gwcreator.User import User 

def add_user(user_name):
    freeswitch_config = config["Freeswitch"]
    cli = FsCli(freeswitch_config.get("CliPath"))

    user = User(user_name, freeswitch_config.get("FsPath"), freeswitch_config.get("SipDomain"))
    user.create()
    cli.rescan()

def remove_user(user_name):
    freeswitch_config = config["Freeswitch"]
    cli = FsCli(freeswitch_config.get("CliPath"))

    user = User(user_name, freeswitch_config.get("FsPath"), freeswitch_config.get("SipDomain"))
    cli.kill_gateway("{}-GW".format(user_name)) 
    user.delete()
    cli.reloadxml()

def main(args, config):
    (users_per_second, users_deleted, deletion_cycle, total_users) = args 
    users = []
    time_to_delete = 0
    while len(users) <= int(total_users):
        user = random.choice([x for x in range(999999) if x not in users])
        #pool = Pool(processes=1) 
        #pool.apply_async(add_user, [user])
        add_user(user)
        users.append(user)
        time_to_delete += 1
        if time_to_delete == int(users_per_second):
            time_to_delete = 0
            deleted_users = 0
            while deleted_users <= int(users_deleted): 
                user = random.choice(users)
                #pool = Pool(processes=1) 
                #pool.apply_async(remove_user, [user])
                remove_user(user)
                deleted_users += 1
                users.remove(user)
            deleted_users = 0
            time.sleep(1)
    time.sleep(600)
    for user in users:
        remove_user(user)
        users.remove(user)

    
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    # @TODO: use getopt instead of simple sequence of args
    '''
    meanwhile the explanation of args:
    python main.py 10 3 2 450
    10 new users per second
    3 deleted
    every 2 cycles
    450 new users at total
    '''
    main(sys.argv[1:], config)
