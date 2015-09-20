from heat.engine import properties
from heat.engine import resource
from qingcloud_heat_plugin.client.api_connection import API_Connection
from qingcloud_heat_plugin.log.plugin_log import PluginLog
from heat.common.i18n import _
from heat.common import exception
from heat.engine import constraints

LOG = PluginLog().get_logger()


class QingCloudSSHKey(resource.Resource):
    _conn = None

    properties_schema = {
        'zone': properties.Schema(
            properties.Schema.STRING,
            _('data center'),
            required=True,
            constraints=[
                constraints.Length(1),
            ]
        ),
        'name': properties.Schema(
            properties.Schema.STRING,
            _('the name of the key pair'),
            required=True,
        ),
    }

    attributes_schema = {
        'name': _('the name of the SSH key pair'),
    }

    def handle_create(self):
        LOG.info("----------------------Heat engine is starting to create a key pair------------------------------")
        zone = self.properties['zone']
        name = self.properties['name']
        conn = API_Connection().get_connection(zone)
        self._conn = conn

        ret = conn.create_keypair(name)
        LOG.debug("SSH--create_keypair():%s)" % ret)
        return ret

    def check_create_complete(self, token):
        LOG.info("----------------------Heat engine is starting to check whether creation of SSH key pair completes------------------------------")
        LOG.debug("token of check_create_complete %s" % token)
        return False



def resource_mapping():
    return {
        'COM::TwoFellows::SSH': QingCloudSSHKey,
    }





