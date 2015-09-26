from heat.engine import properties
from heat.engine import resource
from qingcloud_heat_plugin.client.api_connection import API_Connection
from qingcloud_heat_plugin.log.plugin_log import PluginLog
from heat.common.i18n import _
from heat.common import exception
from heat.engine import constraints

LOG = PluginLog().get_logger()


class QingCloudKey(resource.Resource):
    _conn = None
    private_key = None
    pub_key = None

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

    update_allowed_keys = ('Properties',)

    attributes_schema = {
        'name': _('the name of the SSH key pair'),
    }

    def handle_create(self):
        LOG.info("----------------------Heat engine is starting to create a key pair------------------------------")
        #import pdb
        #pdb.set_trace()
        zone = self.properties['zone']
        name = self.properties['name']
        conn = API_Connection().get_connection(zone)
        self._conn = conn

        ret = conn.create_keypair(name)
        LOG.debug("SSH--create_keypair():%s)" % ret)
        '''
        {u'action': u'CreateKeyPairResponse',
        u'private_key': u'-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAuwKg9F+ms+7QzmKefCVTpgutkz/XUHWUpOqQyBXbN5KHsSbb\nHNTeOY7cowM7kzdbYh+ohcqry9uf7JFg8o7V+kIM9SswWJKTtaM+WPLv4RXoN49L\ner+0KqH2OgmYU4IpdBaaUeXspCU0l7Xy8XK84HbXsuoFB7AtxxlplbTDu64SvzkF\nQNi5MY/L+yCTSrnXVduYIQEMHaFPhMPwHivNWuNCod+cxlFdi584DBfJrduCmR/g\nbWX8abYVNby2wCle5NPiykwWm+nHXrd8Mf+NhA4X1UM+CWxO76FWri9SLr9d11LF\nmNNo4eIb99kUx1lDPtoRbkte8Ab/pQgF//aSGQIDAQABAoIBAB078vdgwImeSqwI\nxKe5mhL5/l9nenxMdTk2pf1xVTyhvm6WGWivajHrQFiHV9fSrolvU4Pew+5xXdW4\ngERKye5+RtJItx0RhN+/Li7vg0pXh16wGueMcli7yucVuudLELniEqu82rpqSodw\n3RKbkiUwztVcOf8SroVSVqwdfv+mmUD7cxyerxIFCQgR37lLzPejYKSywtSV8zue\nS7ErQZB3Vf0bD3AquGrTSLd+RlOqqXRmeOcmd5jfE6OiLrQSrdRULqWz16iMD81g\n5D+AVCRP2p1aY0cieTzpPQGiDMmjn1pPo3jFhH0hqYUoZl+j8PUfPdqSSGDFwkhp\n2C6HUYUCgYEA33gV+B4b0invL4x3rvmY6DpXP6gcG2qs/xKmmY8KhXCzilN8MN9c\ncDciPENyWK0z+9NI3N3gEUiXaLY9wyivHcCiNc4Ta2W5IIrjUjyU8W0BsJXo+5qd\n61kBk8znofcc+9P5u6vhTyuvtv929aSgiTBHlgaCgfC7CPNURuAfAFcCgYEA1jvZ\nj1IFGZZnsAUjfLaXS20rIdJwwjzxRS/iO/XhkZX0fMyZuzuWIj2U9VFHneHR2k4z\nPH4FvMS/ge0SZWedyh/SJeEMIatKNJjj4/umI7uX3K9ZC1i/iXXUA0baoY6oFI10\noXdg3WZhzhLMIa7x+9+KSWJvDvJMtj8OEAaKuw8CgYAa1BPvIc49QQOSNc74lsag\nusBWyBv3vqreRKLztJSSyKEFblhulaJHZpcZnQ9RThn7lbYdrhWEfa6Px7FKiMvd\nSo8u3nq+XgwHuCTqbpODGI8nYBgEfN+QrbLex67XZw93vE8zFMOL+bayxaDGhOkx\nDzbI8Cci6n/J50yq5aVTKQKBgQCrIHey0jOcstX0dsZYEopcB8ISbEUCAyg+ufcf\nKlOatYvsPIr4Uqqkg0h/hQOODBpTJXAr/AadORQ4tqShN9mE4VI+S7wjEO5fgVlY\nfWXC2VB/Sdn5BFVLekF2tJxjvM5qTGxDplZLxEKQF9fTeCl3pqKR5/0KlWXNliSn\njHI45QKBgQDPYxO/bn6+Mde52FTnVhRcFXRHSkQ64aBwcz6TUdbbeOnAuI/wMCOf\nvhz+SfCYjMjBClDcnhypWJt8qged1hXZmZrAMIM8Ix+X2qdtbrVmtj82yWLzdnL9\nUGc9MZYgqnDPsyQTdS/HLrhytDaiwGzorFY+8LnzLe8W2oHwz5laJA==\n-----END RSA PRIVATE KEY-----\n',
        u'keypair_id': u'kp-1kaua86u',
        u'ret_code': 0})
        '''
        if 'ret_code' not in ret.keys() or 'keypair_id' not in ret.keys():
            exc = exception.Error(_("Creation of key pair failed  failed without unknown reasons"))
            raise exc

        ret_code = ret['ret_code']
        if ret_code == 0:
            if 'private_key' in ret.keys():
                global private_key
                private_key = ret['private_key']
            return ret['keypair_id']
        else:
            if 'message' in ret.keys():
                message = ret['message']
            if not message:
                exc = exception.Error(_("Creation of key pair failed  failed to provision with reason: %s, code: %s" % message, ret_code))
                raise exc
            else:
                exc = exception.Error(_("Creation of key pair failed  failed to provision with reason: %s" % ret_code))
                raise exc

    def check_create_complete(self, token):
        """
        Check the status of create operation of the resource type
        @param token: The return of handle_create()
        @return: True: The resource type is successfully created
                 False: THe resource fails to be created
        """
        LOG.info("Heat engine is starting to check whether creation of SSH key pair completes")
        LOG.debug("Token return by create operation is [%s]" % token)
        key_pair_id = token
        operation_name = 'Key pair creation'
        return self.check_operation_complete(operation_name, key_pair_id)

    def check_operation_complete(self, operation_name, resource_id):
        """ Check the complete status of an operation
            @param operation_name: the name of the operation like 'create', 'update'
            @param operation_result: The dict of the result of the operation
        """
        #LOG.debug("The of %s is: %s" % operation_name, operation_result)
        key_pair_id = resource_id
        resource_status_ret = self._conn.describe_key_pairs([key_pair_id])
        '''
        a sample
        {u'action': u'DescribeKeyPairsResponse', u'total_count': 1, u'keypair_set': [{u'description': None, u'tags': [], u'encrypt_method': u'ssh-rsa', u'keypair_name': u'keypair1', u'create_time': u'2015-09-26T08:56:47Z', u'keypair_id': u'kp-a0pyyvko', u'pub_key': u'AAAAB3NzaC1yc2EAAAADAQABAAABAQDJqGlUdXlYmP4lMGzFiXilqwxUzQwOd/XqQ5aUJ7NADVHS6gTgzaRViREsb8mcc1yA54vB+Chrbh0N1+kumM5c/Co8jCUWmHvvDI4HSWto0Kstvc3CiRwssnuuI72+7nXriWLaDpUZ1SuOs8BfbD1e8eMfwp34RnDXcP6aYwCqhcMSV1YLV2aoy+C9icP3YhxDkEHFVm8lcXbVNMpjM40XAkoSVnvffUHdGpNAg+y2tsEwAiQZvP1JA96IzL9O59D4rdyAZAlw/x5eegx+UZ6YXrqO4WOSXSneKgSI2RlAqsKHOVIDlEkK75aqPI4zSG8yTN8ugu5gnX9l7v/c2mQf'}], u'ret_code': 0}
        '''
        LOG.debug("The status dict of the resource is: %s" % resource_status_ret)

        if 'ret_code' not in resource_status_ret.keys() or 'keypair_set' not in resource_status_ret.keys() \
                or 'total_count' not in resource_status_ret.keys():
            exc = exception.Error(_("Creation of key pair failed without unknown reasons"))
            raise exc

        return_code = resource_status_ret['ret_code']

        if return_code == 0:
            key_pair_num = resource_status_ret['total_count']
            LOG.debug("Number of key pairs creation: [%d]. " % key_pair_num)
            if key_pair_num == 1:
                LOG.debug("key_pair_num: %s" % key_pair_num)
                key_pair = resource_status_ret['keypair_set'][0]
                LOG.debug("1")
                global pub_key
                LOG.debug("2")
                pub_key = key_pair['pub_key']
                LOG.debug("3")
                return True
            elif key_pair_num == 0:
                LOG.debug("key_pair_num: %s" % key_pair_num)
                return False
        else:
            exc = exception.Error(_("Creation of key pair failed with reason: %s" % return_code))
            raise exc

    def _resolve_attribute(self, name):
        LOG.debug("Resolving attributes of the resource type")
        if name == 'pub_key':
            return pub_key
        if name == 'private_key':
            return private_key


def resource_mapping():
    return {
        'COM::TwoFellows::Key': QingCloudKey,
    }





