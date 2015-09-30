from heat.engine import properties
from heat.engine import resource
from qingcloud_heat_plugin.client.api_connection import API_Connection
from qingcloud_heat_plugin.log.plugin_log import PluginLog
from heat.common.i18n import _
from heat.common import exception
from heat.engine import constraints

LOG = PluginLog().get_logger()

class QingCloudKeyAttachment(resource.Resource):
    '''
    To attach a key pair to an instance
    zzxwill
    9/27/2015
    '''

    _conn = None
    private_key = None

    properties_schema = {
        'key_pair_id': properties.Schema(
            properties.Schema.STRING,
            _('key pair id'),
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
    }

    update_allowed_keys = ('Properties',)

    attributes_schema = {
        'private_key': _('the private SSH key pair'),
    }

    def handle_create(self):
        '''
        To attach a key pair to an instance
        '''
        LOG.info("Heat engine is starting to attach a key pair to an instance")
        #import pdb
        #pdb.set_trace()

        key_pair_id = self.properties['key_pair_id']
        instance_id = self.properties['instance_id']
        zone = self.properties['zone']
        conn = API_Connection().get_connection(zone)
        self._conn = conn

        ret = conn.attach_keypairs([key_pair_id], [instance_id])
        LOG.debug("KeyAttachment--return of attach_keypairs: %s)" % ret)

        '''
        A sample
        {u'action': u'AttachKeyPairsResponse', u'job_id': u'j-fd1ww6nr', u'ret_code': 0}
        '''
        if 'ret_code' not in ret.keys():
            exc = exception.Error(_("Attachment of key pair to an instance failed without unknown reasons"))
            raise exc

        ret_code = ret['ret_code']
        if ret_code == 0:
            return True
        else:
            message = None
            if 'message' in ret.keys():
                message = ret['message']
            if not message:
                exc = exception.Error(_("Attachment of key pair to an instance failed with reason: %s, code: %s" % message, ret_code))
                raise exc
            else:
                exc = exception.Error(_("Attachment of key pair to an instance failed with reason: %s" % ret_code))
                raise exc
            return False

    def check_create_complete(self, token):
        """
        Check the status of attaching a key pair to an instance
        @param token: The return of handle_create()
        @return: True: The resource type is successfully created
                 False: THe resource fails to be created
        """
        LOG.info("Heat engine is starting to check whether the attachment of SSH key pair to an instance completes")
        LOG.debug("Token return by create operation is [%s]" % token)
        return token


    def _resolve_attribute(self, name):
        LOG.debug("Resolving attributes of the resource type")

        if name == 'private_key':
            return "aaa"


def resource_mapping():
    return {
        'COM::TwoFellows::KeyAttachment': QingCloudKeyAttachment,
    }





