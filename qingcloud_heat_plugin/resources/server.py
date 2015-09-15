from heat.engine import properties
from heat.engine import resource
from qingcloud_heat_plugin.client.api_connection import API_Connection
from qingcloud_heat_plugin.log.plugin_log import PluginLog
from heat.common.i18n import _
from heat.common import exception
from heat.engine import constraints

import qingcloud.iaas 

LOG = PluginLog().get_logger()

class QingCloudServer(resource.Resource):

    #plugin_log = PluginLog()
    #LOG = plugin_log.get_logger()
    _return_instance_dict = {}
    _return_instance_dict_test = {}
    _return_instance_dict_delete = {}
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
            constraints=[
                         constraints.Length(1),
            ]
        ),
    }

    update_allowed_keys = ('Properties',)

    def __init__(self, name, json_snippet, stack):
        LOG.debug("Server-__init__() is called.")
        super(QingCloudServer, self).__init__(name, json_snippet, stack)   

    attributes_schema = {
        'instance_id': _('the instance id'),
    }

    def handle_create(self):
        LOG.info("----------------------Heat engine is starting to deploy Server------------------------------")
        

        '''
        qingcloud_image_id = self.PROPERTIES.get(self.IMAGE_ID)
        qingcloud_login_mode = self.PROPERTIES.get(LOGIN_MODE)
        qingcloud_login_passwd = self.PROPERTIES.get(LOGIN_PASSWD)
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

        '''
        A sample of returned strings
        {u'action': u'RunInstancesResponse', u'instances': [u'i-kbvq1jio'], u'job_id': u'j-91chniph', u'ret_code': 0}
        '''

        self._return_instance_dict = ret
        global _return_instance_dict_test
        _return_instance_dict_test = ret

        LOG.debug("ret: run_instance: %s" % ret)

        if 'ret_code' in ret.keys():
            return_code = ret['ret_code']
            LOG.info("return code or instance provisioning is: %s" % ret)
            if return_code == 0:
                return True
            else:   # else can be elaborated later per https://docs.qingcloud.com/api/common/error_code.html
                return False



        return ret

    # def check_create_complete(self):
    def check_create_complete(self, token):
        LOG.debug("server-check_create_complete is executed.")

        ret = self._return_instance_dict
        LOG.debug("instance information is [%s]" % ret)

        if 'ret_code' in ret.keys():
            return_code = ret['ret_code']
            LOG.debug("The status of the VM provisioning is [%s]" % return_code)
            if return_code == 0:
                '''
                Check the status of the instance
                zzxwill
                9/4/2015
                '''
                #ret = conn.describe_instances(['i-668tmejn'])
                instance_status_ret = self._conn.describe_instances(ret['instances'])

                LOG.debug("instance_status_ret: %s" % instance_status_ret)
                instance_status = instance_status_ret['instance_set'][0]['status']
                LOG.debug("The status of the newly provisioned VM is [%s]" % instance_status)

                if instance_status == "pending":
                    return False
                elif instance_status == "running":
                    return True

                LOG.debug("instance_status_ret: %s" % instance_status_ret)
            else:
                LOG.debug("return_code: %s" % return_code)
                exc = exception.Error(_("Server failed to provision with reason: %s" % return_code))
                raise exc

    def handle_delete(self):
        zone = self.properties['zone']
        LOG.debug("zone: %s" % zone)

        api_connection = API_Connection()
        conn = api_connection.get_connection(zone)
        LOG.debug("_return_instance_dict: %s" % self._return_instance_dict)
        LOG.debug("_return_instance_dict_test: %s" % _return_instance_dict_test)
        #ret = conn.terminate_instances(self._return_instance_dict['instances'])
        ret = conn.terminate_instances(_return_instance_dict_test['instances'])

        self._return_instance_dict_delete = ret
        LOG.debug("return of terminate_instances: %s" % ret)
        return


    def check_delete_complete(self, cookie=None):
        LOG.debug("return of terminate_instances: %s" % self._return_instance_dict_delete)
        return_code = self._return_instance_dict_delete['ret_code']
        if return_code == 0:
            return True
        else:
            return_message = self._return_instance_dict_delete['message']
            exc = exception.Error(_("Server failed to be deleted with reason: %s" % return_message))
            raise exc

        return False

    def _resolve_attribute(self, name):
        LOG.debug("-------------------------------_resolve_attribute----------------------------")
        LOG.debug("-------------------------------------------------------------------------------name: %s" % name)

        LOG.debug("-------------equal? %s" % name == 'instance_id')

        if name == 'instance_id':
            LOG.debug("-------------------------------------------------------------------------------resolving attribute %s" % name)
            LOG.debug("_return_instance_dict['instances']: %s" % self._return_instance_dict['instances'])
            return self._return_instance_dict['instances'][0]


def resource_mapping():
    return {
        'COM::TwoFellows::Server': QingCloudServer,
    }

if __name__ == '__main__':
    pass