'''
Created on Jul 16, 2015

@author: zhouzhengxi
'''
#import http.client
import paramiko

import base64
import hmac
import urllib
from hashlib import sha256
import time

import qingcloud.iaas

if __name__ == '__main__':


    conn = qingcloud.iaas.connect_to_zone(
                                          'pek2',
                                          'MGJYTHJRQYNGAOHKCQPK',
                                          'WalqP1YzFK2tFMI2qm9EA1YDezLGFis9NQSd7ir5'    )
    instance_status_ret = conn.describe_instances(instances=['i-0xjmusae'], verbose=1)
    print instance_status_ret


    keypair_ids = [1,2]
    if keypair_ids.__contains__(1):
        print "yes"


    time.sleep(3)





    #ret = conn.describe_key_pairs([ret['keypair_id']])
    #print ret


    # ret = conn.describe_instances(ret['instances'])
    # #ret = conn.describe_instances(['i-oqgqzoz1'])
    # print ret
    # instance_status = ret['instance_set'][0]['status']
    # if instance_status == "pending":
    #     print("False")
    # elif instance_status == "running":
    #     print("True")





    #print ret

    # if 'ret_code' in ret.keys():
    #         retrun_code = ret['ret_code']
    #         if retrun_code == 0:
    #             '''
    #             Check the status of the instance
    #             zzxwill
    #             9/4/2015
    #             '''
    #             ret = conn.describe_instances(ret['instances'] )
    #             print(ret)
    #




    

    #===========================================================================
    # url = "GET\n/iaas/\naccess_key_id=OVNQCDZGCMAMQCYQZTPQ&action=DescribeInstances&signature_method=HmacSHA256&signature_version=1&time_stamp=2015-08-31T13%3A58%3A35Z&version=1&zone=pek2"
    # h = hmac.new("fZmFLDKjswA5ZobyPfmFPgvXXNubgPcJ2QRevVs8", digestmod=sha256)
    # h.update(url)
    # sign = base64.b64encode(h.digest()).strip()
    # signature = urllib.quote_plus(sign)
    # url += "&signature=" + signature
    # print(url)
    #===========================================================================
    

    pass