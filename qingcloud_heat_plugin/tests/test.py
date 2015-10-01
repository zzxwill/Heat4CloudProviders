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

from heat.common import exception
import qingcloud.iaas

if __name__ == '__main__':




    """
        test by lbc
        """
    conn = qingcloud.iaas.connect_to_zone(
                                          'pek2',
                                          'MGJYTHJRQYNGAOHKCQPK',
                                          'WalqP1YzFK2tFMI2qm9EA1YDezLGFis9NQSd7ir5'    )
    # ret = conn.run_instances(
    #                          image_id='trustysrvx64e',
    #                          cpu=1,
    #                          memory=1024,
    #                          #vxnets=['vxnet-0'],
    #                          login_mode='passwd',
    #                          login_passwd='Heat4Chuck'
    # )


    #ret = conn.create_keypair(keypair_name="keypair1")
    #ret = conn.attach_keypairs(['kp-otrvk2jk'], ['i-qevfnj8e'])


    #print ret

    # import paramiko, base64
    # key = paramiko.RSAKey(data=base64.decodestring('MIIEpAIBAAKCAQEAwAnuUgOL1y3yK1YcGnQaGGB4UUUjPQsW5Jey4mhgmJxUzVMbkXx84H9Bu/zSUOM46aeCe5Ah12j22w9NGPBJF/r1AT6OpgNxWg1+/ZvDpisK8mvxJBj/sQlqWM9CjOWg14Q9OAVHqdWVVMH78HDXWer7F7P1EYIFNBa67GQRJ02TASm/Hs1jbhaFGFPkIhvydyWBGrEvN/WtYfqJnby8n2izwq8bu3BJ94KJl8NwQumwPev7yU0z5UkthiLpEYI2ztWeJ3jr+fw69pBfNEhf7YwmBfn0em9NA/PhMTUhcXjhD2sz/VAO9i5RVzoQKwKvn0ocf03ADc3WymkonJK84wIDAQABAoIBAGjOQrGh29Tw72S1Vxsc2A0LwT5hZCzxe2oAXJFx8532W9W/EKGi9igza3WkMkgQ6kOitvSmocGFOIwvWp1MrieXP9WRBZsW7+r8yJyyQOHUReIuBOn1dr5w7AhR/PkWbWSReDO1tfm7Zgde4xfDDdS2CJlUDmCivCJEcXmH11DB8z7sCgPYhSQapUVKESjCt9lD+/2NjdmvKMGd0hMEyqiKT106P+Y91OtXxWzdpxpujwfw0nhO8wZ2fBlE8V1JXjJ0TEduk3duZKf4IlF83QLm1L3r6FBr03k4ShWJ5z4wuu8p3tQjLQ9Ya+gNVDbIBDBpaUsozmrzWqL6JYmjJHkCgYEA9XJuyMHCYaG2YtIt5R9IYUyp6uDc1W5HhndvDkN/0K58g/jcsRBXMO7OJrhu5fRuYyQUXmptHX4gRETgqcDLHPCJ1c2e8xnsxaNJ+qJ2iGE2LXIcR+ZIkIv1Tx+QFIXaQkaO7qOAQEmzGO6aii5qWbqYsCSu5RMTPtTeaqFM7r8CgYEAyEumF3tSgLPOOhSCWjvZwP329wFA03DoEvD/KZvLPDlDVhdTTo6+AQMslSuXl2Hx9C44c69M6fd24VcuhFNdizNQzx3fiMLYQJuyBjkWcUNRGW6Xrg0A7JomweVpcBCEMbEVt27iGa4RHAwrOjtK5GxmoVJ0A5XVB2mQx4Ch3t0CgYEAv4NKbdrBkOxdIz5cESsXjtQCwQIzTVV++ay3OqnwUSPUhCTqDj5xyfyLXisKXOMcPr8oJYNlIF4JTztvEQUddrc41Vpba9QOqyd90dJyKnevjkY7St6kQCT0g4hdI6ZNZuknHYz1xTO8SvfiHW+aC+lMuiPlU1hO6/eslAbHwIECgYAiDjK8VVyOw4Ox/mC3hOueU9AU6WKjUNQ0vEM2SOYCZF4dmjOw7LZDp82Bw3qv45hnAyDYEptKQKg24kLnfuEt1NjNjm++ahqoyZA4XKaDNYXphBNIJa/disxCNYZ65mQDqu9dU/4fjagdE7iZ2xD9y6ybi1Bsd6JT81AJi8Z6BQKBgQDZa4sUKsN7EcM797DLkYW1lKSHVmfyySXenNNPKU4DuJb3yT6KWIlQDnECLVTxWczkFpkACyMnrR4vMq6y0fYoBX2T9zoUUsUEykWprObAOboYHm01NLG0ffZCMejfS4EH3ukoleqVkfh2OQ6Y1bJ97wbR2Df+hsKZS7Get/GHLw=='))
    # client = paramiko.SSHClient()
    # client.get_host_keys().add('119.254.100.229', 'ssh-rsa', key)
    # client.connect('119.254.100.229', username='root',)
    # stdin, stdout, stderr = client.exec_command('ls')
    # for line in stdout:
    #     print '... ' + line.strip('\n')
    # client.close()

    import paramiko

    #ssh = paramiko.SSHClient()
    #ssh = paramiko.Transport("119.254.100.229", "22")

    #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect("119.254.100.229",22,"root",)
    #ssh.co
    #ssh.connect(username="root", pkey="MIIEpAIBAAKCAQEAwAnuUgOL1y3yK1YcGnQaGGB4UUUjPQsW5Jey4mhgmJxUzVMbkXx84H9Bu/zSUOM46aeCe5Ah12j22w9NGPBJF/r1AT6OpgNxWg1+/ZvDpisK8mvxJBj/sQlqWM9CjOWg14Q9OAVHqdWVVMH78HDXWer7F7P1EYIFNBa67GQRJ02TASm/Hs1jbhaFGFPkIhvydyWBGrEvN/WtYfqJnby8n2izwq8bu3BJ94KJl8NwQumwPev7yU0z5UkthiLpEYI2ztWeJ3jr+fw69pBfNEhf7YwmBfn0em9NA/PhMTUhcXjhD2sz/VAO9i5RVzoQKwKvn0ocf03ADc3WymkonJK84wIDAQABAoIBAGjOQrGh29Tw72S1Vxsc2A0LwT5hZCzxe2oAXJFx8532W9W/EKGi9igza3WkMkgQ6kOitvSmocGFOIwvWp1MrieXP9WRBZsW7+r8yJyyQOHUReIuBOn1dr5w7AhR/PkWbWSReDO1tfm7Zgde4xfDDdS2CJlUDmCivCJEcXmH11DB8z7sCgPYhSQapUVKESjCt9lD+/2NjdmvKMGd0hMEyqiKT106P+Y91OtXxWzdpxpujwfw0nhO8wZ2fBlE8V1JXjJ0TEduk3duZKf4IlF83QLm1L3r6FBr03k4ShWJ5z4wuu8p3tQjLQ9Ya+gNVDbIBDBpaUsozmrzWqL6JYmjJHkCgYEA9XJuyMHCYaG2YtIt5R9IYUyp6uDc1W5HhndvDkN/0K58g/jcsRBXMO7OJrhu5fRuYyQUXmptHX4gRETgqcDLHPCJ1c2e8xnsxaNJ+qJ2iGE2LXIcR+ZIkIv1Tx+QFIXaQkaO7qOAQEmzGO6aii5qWbqYsCSu5RMTPtTeaqFM7r8CgYEAyEumF3tSgLPOOhSCWjvZwP329wFA03DoEvD/KZvLPDlDVhdTTo6+AQMslSuXl2Hx9C44c69M6fd24VcuhFNdizNQzx3fiMLYQJuyBjkWcUNRGW6Xrg0A7JomweVpcBCEMbEVt27iGa4RHAwrOjtK5GxmoVJ0A5XVB2mQx4Ch3t0CgYEAv4NKbdrBkOxdIz5cESsXjtQCwQIzTVV++ay3OqnwUSPUhCTqDj5xyfyLXisKXOMcPr8oJYNlIF4JTztvEQUddrc41Vpba9QOqyd90dJyKnevjkY7St6kQCT0g4hdI6ZNZuknHYz1xTO8SvfiHW+aC+lMuiPlU1hO6/eslAbHwIECgYAiDjK8VVyOw4Ox/mC3hOueU9AU6WKjUNQ0vEM2SOYCZF4dmjOw7LZDp82Bw3qv45hnAyDYEptKQKg24kLnfuEt1NjNjm++ahqoyZA4XKaDNYXphBNIJa/disxCNYZ65mQDqu9dU/4fjagdE7iZ2xD9y6ybi1Bsd6JT81AJi8Z6BQKBgQDZa4sUKsN7EcM797DLkYW1lKSHVmfyySXenNNPKU4DuJb3yT6KWIlQDnECLVTxWczkFpkACyMnrR4vMq6y0fYoBX2T9zoUUsUEykWprObAOboYHm01NLG0ffZCMejfS4EH3ukoleqVkfh2OQ6Y1bJ97wbR2Df+hsKZS7Get/GHLw==")
    #stdin, stdout, stderr = ssh.exec_command("ls")
    #print stdout.readlines()
    #ssh.close()

    ssh = paramiko.SSHClient()
    #pkey_file = 'c:\zhouzhengxi\Programming\Python\Heat4CloudProviders\qingcloud_heat_plugin\client\private_key_pair'
    pkey_file = '/usr/lib/heat/qingcloud_heat_plugin/client/private_key_pair'
    pkey_pass = '123321'
    ip = '119.254.100.229'
    ssh_port = 22
    ssh_user = 'root'
    print 1
    ssh_client = paramiko.SSHClient()
    print 2
    private_key = paramiko.RSAKey.from_private_key_file(pkey_file)
    print 3
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print 4
    try:
        ssh_client.connect(hostname=ip, username=ssh_user, password=None, pkey=private_key)
        print 5
        cmd = "touch /root/zhouzhengxi.txt"
        stdin, stdout, stderr = ssh_client.exec_command(cmd)

        exit_status = stdout.channel.recv_exit_status()
        ssh_client.close()

    except Exception as e:
        print("Fail to log on the instance with reason: [%s]" % e)
        exc = exception.Error(((e)))
        raise exc




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