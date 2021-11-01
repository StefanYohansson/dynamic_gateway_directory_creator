import subprocess

class FsCli():
    cli_path = None
    params = []

    def __init__(self, cli_path, params = None):
        self.cli_path = cli_path
        if params:
            self.params = params

    def __get_cli_location(self):
       return self.cli_path 

    def __execute(self, cmd):
        fs_cli = self.__get_cli_location()
        subprocess.run([fs_cli] + self.params + ["-x"] + cmd)

    def reloadxml(self):
       self.__execute(["reloadxml"]) 

    def rescan(self):
        self.__execute(["sofia profile internal rescan reloadxml"])

    def kill_gateway(self, gateway):
        self.__execute(["sofia profile internal killgw {}".format(gateway)])

