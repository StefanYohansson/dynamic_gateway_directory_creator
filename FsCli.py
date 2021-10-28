import subprocess

class FsCli():
    cli_path = None

    def __init__(self, cli_path):
        self.cli_path = cli_path

    def __get_cli_location(self):
       return self.cli_path 

    def __execute(self, cmd):
        fs_cli = self.__get_cli_location()
        subprocess.run([fs_cli, "-x"] + cmd)

    def reloadxml(self):
       self.__execute(["reloadxml"]) 

    def rescan(self):
        self.__execute(["sofia profile internal rescan reloadxml"])

