from heat.engine import properties
from heat.engine import resource
from qingcloud_heat_plugin.client.api_connection import API_Connection
from qingcloud_heat_plugin.log.plugin_log import PluginLog
from heat.common.i18n import _
from heat.common import exception
from heat.engine import constraints

LOG = PluginLog().get_logger()

class QingCloudIP(resource.Resource):
    '''
    To associate an IP address to an instance
    zzxwill
    9/29/2015
    '''

    _conn = None

    properties_schema = {
        'eip': properties.Schema(
            properties.Schema.STRING,
            _('The public IP address'),
            required=True,
            constraints=[
                constraints.Length(1),
            ]
        ),
        'instance_id': properties.Schema(
            properties.Schema.STRING,
            _('instance id'),
            required=True,
        ),
        'zone': properties.Schema(
            properties.Schema.STRING,
            _('data center'),
            required=True,
            constraints=[
                constraints.Length(1),
            ]
        ),
    }

    update_allowed_keys = ('Properties',)

    attributes_schema = {
        'private_key': _('the private SSH key pair'),
    }

    def handle_create(self):
        '''
        To attach a key pair to an instance
        '''
        LOG.info("Heat engine is starting to associate an IP to an instance")
        #import pdb
        #pdb.set_trace()

        eip = self.properties['eip']
        instance_id = self.properties['instance_id']
        zone = self.properties['zone']
        conn = API_Connection().get_connection(zone)
        self._conn = conn

        ret = conn.associate_eip(eip = eip, instance=instance_id)

        LOG.debug("KeyAttachment--return of associate_eip: %s)" % ret)

        '''
        A sample

        '''
        if 'ret_code' not in ret.keys():
            exc = exception.Error(_("Associating an IP to an instance failed without unknown reasons"))
            raise exc

        ret_code = ret['ret_code']
        if ret_code == 0:
            return True
        else:
            message = None
            if 'message' in ret.keys():
                message = ret['message']
            if not message:
                exc = exception.Error(_("Associating an IP to an instance failed with reason: %s, code: %s" % message, ret_code))
                raise exc
            else:
                exc = exception.Error(_("Associating an IP to an instance failed with reason: %s" % ret_code))
                raise exc
            return False

    def check_create_complete(self, token):
        """
        Check the status of attaching a key pair to an instance
        @param token: The return of handle_create()
        @return: True: The resource type is successfully created
                 False: THe resource fails to be created
        """
        LOG.info("Heat engine is starting to check whether an IP address is associated to an instance completes")
        LOG.debug("Token return by associating an IP to an instance is [%s]" % token)
        return token


    def _resolve_attribute(self, name):
        LOG.debug("Resolving attributes of the resource type")

        return "aaa"


def resource_mapping():
    return {
        'COM::TwoFellows::IP': QingCloudIP,
    }





