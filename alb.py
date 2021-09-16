#!/usr/bin/env python3
#coding=utf-8
import sys
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.auth.credentials import StsTokenCredential
def ClientServer(accessId,accessSecret):
    credentials = AccessKeyCredential(accessId, accessSecret)
    client = AcsClient(region_id='cn-hangzhou', credential=credentials)
    return client
def SetBackendServers(accessId,accessSecret,resource,BackendServers,Weightservice):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('slb.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2014-05-15')
    request.set_action_name('SetVServerGroupAttribute')
    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('VServerGroupId', resource)
    request.add_query_param('BackendServers', "[{ \"ServerId\": \""+BackendServers+"\", \"Type\": \"ecs\", \"Port\":\"80\",\"Weight\": \""+Weightservice+"\"}]")
    client = ClientServer(accessId,accessSecret)
    response = client.do_action(request)
    return response
if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("输入错误请重新输入!!!")
    else:
        userInput = sys.argv[1:]
        accessId = userInput[0]
        accessSecret = userInput[1]
        resource = userInput[2]
        BackendServers = userInput[3]
        Weightservice = userInput[4]
