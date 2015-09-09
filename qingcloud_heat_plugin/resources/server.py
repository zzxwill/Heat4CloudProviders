from heat.engine import properties
from heat.engine import resource
from qingcloud_heat_plugin.client.api_connection import API_Connection
from qingcloud_heat_plugin.log.plugin_log import PluginLog
from heat.common.i18n import _
from heat.common import exception

import qingcloud.iaas 


class QingCloudServer(resource.Resource):

    plugin_log = PluginLog()
    LOG = plugin_log.get_logger()
    _return_instance_dict = {}
    _conn = None

    PROPERTIES = (
        IMAGE_ID,
        LOGIN_MODE,
        LOGIN_PASSWD,
        ZONE
    ) = (
        'image_id',
        'login_mode',
        'login_passwd',
        'zone'
    )

    '''
    _('xxx') it means 'xxx' is 'translate strings', see https://docs.djangoproject.com/en/dev/topics/i18n/translation/ and Heat-Kilo\heat\engine\resources\stack_resource.py
    zzxwill
    9/7/2015
    '''

    properties_schema = {
        IMAGE_ID: properties.Schema(
            properties.Schema.STRING,
            _('ID of the image you want to use'),
            required=True,
        ),
        LOGIN_MODE: properties.Schema(
            properties.Schema.STRING,
            _('ssh login mode, "keypair" or "passwd"'),
            required=True,
        ),
        LOGIN_PASSWD: properties.Schema(
            properties.Schema.STRING,
            _('login passwd'),
            required=True,
        ),
        ZONE: properties.Schema(
            properties.Schema.STRING,
            _('data center'),
            required=True,
        ),
    }

    update_allowed_keys = ('Properties',)

    def __init__(self, name, json_snippet, stack):
        self.LOG.debug("Server-__init__() is called.")
        super(QingCloudServer, self).__init__(name, json_snippet, stack)   

    attributes_schema = {
        'instance_id': _('the instance id'),
    }

    def handle_create(self):
        self.LOG.info("----------------------Heat engine is starting to deploy Server------------------------------")
        

        '''
        qingcloud_image_id = self.PROPERTIES.get(self.IMAGE_ID)
        qingcloud_login_mode = self.PROPERTIES.get(self.LOGIN_MODE)
        qingcloud_login_passwd = self.PROPERTIES.get(self.LOGIN_PASSWD)
        zone = self.PROPERTIES.get(self.ZONE)
        '''
        qingcloud_image_id = self.properties['image_id']
        qingcloud_login_mode = self.properties['login_mode']
        qingcloud_login_passwd = self.properties['login_passwd']
        zone = self.properties['zone']

        '''
        Connect to QingCloud API
        zzxwill
        9/3/2015
        '''
        api_connection = API_Connection()
        conn = api_connection.get_connection(zone)

        self._conn = conn

        ret = conn.run_instances(
                             image_id=qingcloud_image_id,        
                             cpu=1,        
                             memory=1024,        
                             #vxnets=['vxnet-0'],        
                             login_mode= qingcloud_login_mode,        
                             login_passwd= qingcloud_login_passwd)

        self._return_instance_dict = ret
        self.LOG.debug("ret: run_instance: %s" % ret)

        if 'ret_code' in ret.keys():
            return_code = ret['ret_code']
            self.LOG.info("return code or instance provisioning is: %s" % ret)
            if return_code == 0:
                return True
            else:   # else can be elaborated later per https://docs.qingcloud.com/api/common/error_code.html
                return False



        return ret

    # def check_create_complete(self):
    def check_create_complete(self, token):
        self.LOG.debug("server-check_create_complete is executed.")

        ret = self._return_instance_dict
        self.LOG.debug("instance information is [%s]" % ret)

        if 'ret_code' in ret.keys():
            return_code = ret['ret_code']
            self.LOG.debug("The status of the VM provisioning is [%s]" % return_code)
            if return_code == 0:
                '''
                Check the status of the instance
                zzxwill
                9/4/2015
                '''
                #ret = conn.describe_instances(['i-668tmejn'])
                instance_status_ret = self._conn.describe_instances(ret['instances'])

                self.LOG.debug("instance_status_ret: %s" % instance_status_ret)
                instance_status = instance_status_ret['instance_set'][0]['status']
                self.LOG.debug("The status of the newly provisioned VM is [%s]" % instance_status)

                if instance_status == "pending":
                    return False
                elif instance_status == "running":
                    return True

                self.LOG.debug("instance_status_ret: %s" % instance_status_ret)
            else:
                self.LOG.debug("return_code: %s" %return_code)
                exc = exception.Error(_("Server failed to provision with reason: %s" % return_code))
                raise exc


    def _resolve_attribute(self, name):
        if name == "instance_id":
            return self._return_instance_dict['instances']


def resource_mapping():
    return {
        'COM::TwoFellows::Server': QingCloudServer,
    }

if __name__ == '__main__':
    pass