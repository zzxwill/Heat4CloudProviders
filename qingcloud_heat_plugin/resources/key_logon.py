from heat.engine import properties
from heat.engine import resource
from qingcloud_heat_plugin.log.plugin_log import PluginLog
from heat.common.i18n import _
from heat.common import exception
from heat.engine import constraints
import paramiko

LOG = PluginLog().get_logger()


class QingCloudKeyLogon(resource.Resource):
    '''
    To log on to an instance and execute some command
    zzxwill
    9/28/2015
    '''
    private_key = None

    properties_schema = {
        'ip': properties.Schema(
            properties.Schema.STRING,
            _('IP address of an instance'),
            required=True,
            constraints=[
                constraints.Length(1),
            ]
        ),
        'private_key_file': properties.Schema(
            properties.Schema.STRING,
            _('private key file of a key pair'),
            required=True,
        ),
        'user': properties.Schema(
            properties.Schema.STRING,
            _('SSH user, normally it is root'),
            required=True,
        ),
    }

    update_allowed_keys = ('Properties',)

    attributes_schema = {
        'ip': _('IP address of an instance'),
    }

    def handle_create(self):
        import logging
        r = logging.getLogger()
        r.debug("-----------------------------------------------")
        r.error("-------------------------eeeeeeeeeeeeeee--------------------")
        '''
        To log on to an instance and execute some command
        '''
        LOG.info("Heat engine is starting to log on to an instance and execute some commands")

        ip = self.properties['ip']
        private_key_file = self.properties['private_key_file']
        user = self.properties['user']
        r.debug("ip: %s" % ip)
        r.debug("private_key_file: %s" % private_key_file)
        r.debug(" user: %s" %  user)

        ssh_client = paramiko.SSHClient()
        private_key = paramiko.RSAKey.from_private_key_file(private_key_file)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            r.debug("connect before")
            ssh_client.connect(hostname=ip, username=user, password=None, pkey=private_key)
            r.debug("connect after")
            cmd = "touch /root/zhouzhengxi.txt; yum -qy install nginx; service nginx start"
            stdin, stdout, stderr = ssh_client.exec_command(cmd)

            exit_status = stdout.channel.recv_exit_status()
            ssh_client.close()
            return exit_status

        except Exception as e:
            LOG.error("Fail to log on the instance with reason: [%s]" % e)
            exc = exception.Error((("Failed: %s" %e)))
            r.debug("------------%s-----------" % e)
            raise exc



    def check_create_complete(self, token):
        """
        Check the status of instance logging on and command executing
        @param token: The return of handle_create()
        @return: True: The resource type is successfully created
                 False: THe resource fails to be created
        """
        LOG.info("Heat engine is starting to check whether it's successful to log on to the instance and execute some commands")
        LOG.debug("Token return by create operation is [%s]" % token)
        if token == 0:
            return True
        return False

    def _resolve_attribute(self, name):
        LOG.debug("Resolving attributes of the resource type")

        return "aaa"


def resource_mapping():
    return {
        'COM::TwoFellows::KeyLogon': QingCloudKeyLogon,
    }





