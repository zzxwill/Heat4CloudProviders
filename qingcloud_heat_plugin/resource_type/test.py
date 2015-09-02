'''
Created on Jul 16, 2015

@author: zhouzhengxi
'''
#import http.client

import base64
import hmac
import urllib
from hashlib import sha256

import qingcloud.iaas 

if __name__ == '__main__':
    conn = qingcloud.iaas.connect_to_zone(        
                                          'pek2', 
                                          'OVNQCDZGCMAMQCYQZTPQ',        
                                          'fZmFLDKjswA5ZobyPfmFPgvXXNubgPcJ2QRevVs8'    )
    ret = conn.run_instances(        
                             image_id='trustysrvx64e',        
                             cpu=1,        
                             memory=1024,        
                             #vxnets=['vxnet-0'],        
                             login_mode='passwd',        
                             login_passwd='Heat4Chuck'    )
    print ret

    

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