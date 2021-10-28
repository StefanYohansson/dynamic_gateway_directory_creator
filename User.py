import os

class User:
    id = None

    def __init__(self, id = None, fs_path = None, sip_domain = None):
        self.id = id
        self.fs_path = fs_path
        self.sip_domain = sip_domain

    def _check_requirements(self):
        if not self.id:
            raise Exception('No ID provided')

        if not self.fs_path:
            raise Exception('No FS path configured')

        if not self.sip_domain:
            raise Exception('No sip domain provided')

    def _generate_directory(self, directory_name):
        directory = """
<include>
    <user id="{}">
        <params>
            <param name="password" value="1234"/>
            <param name="jsonrpc-allowed-methods" value="telnyx_rtc"/>
            <param name="jsonrpc-allowed-event-channels" value="demo,conference,presence"/>
            <param name="telnyx_rtc-context" value="public"/>
            <param name="telnyx_rtc-dialplan" value="XML"/>
        </params>
        <variables>
            <variable name="user_context" value="public"/>
            <variable name="rtp_secure_media" value="optional"/>
            <variable name="default_gateway" value="{}"/>
        </variables>
    </user>
</include>
        """
        return directory.format(directory_name, directory_name)

    def _get_directory_file(self):
        directory_path = "{}/directory".format(self.fs_path)
        return "{}/{}.xml".format(directory_path, self.id)

    def _create_directory(self):
        directory = self._generate_directory(self.id)
        filename = self._get_directory_file()
        file = open(filename,"w+")
        file.write(directory)
        file.close()

    def _generate_gateway(self, gateway_name, user_id, sip_domain):
        gateway = """
<include>
    <gateway name="{}">
        <param name="username" value="{}"/>
        <param name="realm" value="{}"/>
        <param name="from-user" value="{}"/>
        <param name="from-domain" value="{}"/>
        <param name="password" value="1234"/>
        <param name="caller-id-in-from" value="false"/>
        <param name="extension" value="{}"/>
        <param name="extension-in-contact" value="true"/>
        <param name="proxy" value="{}"/>
        <param name="register-proxy" value="{}"/>
        <param name="expire-seconds" value="3600"/>
        <param name="register" value="true"/>
        <param name="register-transport" value="udp"/>
        <param name="retry-seconds" value="30"/>
        <variables>
            <variable name="sip_reg_h_X-Telnyx-RTC" value="true"/>
        </variables>
    </gateway>
</include>
        """
        return gateway.format(gateway_name, user_id, sip_domain, user_id, sip_domain, user_id, sip_domain, sip_domain)

    def _get_gateway_file(self):
        gateway_name = "{}-GW".format(self.id)
        gateway_path = "{}/sip_profiles/gateways".format(self.fs_path)
        gateway_file = "{}/{}.xml".format(gateway_path, gateway_name)
        return gateway_file

    def _create_gateway(self):
        gateway_name = "{}-GW".format(self.id)
        filename = self._get_gateway_file()
        gateway = self._generate_gateway(gateway_name, self.id, self.sip_domain)

        file = open(filename, "w+")
        file.write(gateway)
        file.close()

    def create(self):
        self._check_requirements()
        self._create_directory()
        self._create_gateway()

    def _remove_file(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)

    def delete(self):
        self._check_requirements()

        gateway_file = self._get_gateway_file()
        self._remove_file(gateway_file)

        directory_file = self._get_directory_file()
        self._remove_file(directory_file)

user = User(1001, "./test", "192.168.33.10")
user.create()
