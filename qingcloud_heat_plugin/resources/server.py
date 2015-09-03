from heat.engine import properties
from heat.engine import resource
from qingcloud_heat_plugin.client.api_connection import API_Connection

import qingcloud.iaas 

class QingCloudServer(resource.Resource):   
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


    properties_schema = {
        IMAGE_ID: properties.Schema(
            properties.Schema.STRING,
            #_('XXX'),
            required=True,
        ),
        LOGIN_MODE: properties.Schema(
            properties.Schema.STRING,
            #_('XXX'),
            required=True,
        ),
        LOGIN_PASSWD: properties.Schema(
            properties.Schema.STRING,
            #_('xxx'),
            required=True,
        ),
        ZONE: properties.Schema(
            properties.Schema.STRING,
            #_('xxx'),
            required=True,
        ),
    }

    update_allowed_keys = ('Properties',)

    def __init__(self, name, json_snippet, stack):
        print "OpenStackHeat-__init__() is called."
        super(QingCloudServer, self).__init__(name, json_snippet, stack)   

    attributes_schema = {
        # 'xxx': _('xxx'),
        'xxx': 'XXX',
        'YYY': 'YYY'
    }

    def handle_create(self):
        print "----------------------Heat engine is starting to deploy Server------------------------------"
        

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
        9/1/2015
        '''
        api_connection = API_Connection()
        conn = api_connection.get_connection(zone)

        ret = conn.run_instances(        
                             image_id=qingcloud_image_id,        
                             cpu=1,        
                             memory=1024,        
                             #vxnets=['vxnet-0'],        
                             login_mode= qingcloud_login_mode,        
                             login_passwd= qingcloud_login_passwd    )
        print ret


        return 

    # def check_create_complete(self):
    def check_create_complete(self, token):
        return True


def resource_mapping():
    return {
        'COM::TwoFellows::QINGCLOUD_Server': QingCloudServer,
    }

if __name__ == '__main__':
    pass