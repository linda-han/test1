import random
import re

import pytest
import requests
from filelock import FileLock

@pytest.fixture(scope="session")
def get_token():
    corpid = "wwa0d8d38a46ce5d8b"
    corpsecret = "lcMgpdwH8FxArwX4F8IGULOAC6UvTpLkhW0UG3PIkXg"
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    return res.json()["access_token"]


# 读取成员
def get_user(userid, get_token):
    try:
        res = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token}&userid={userid}")
        return  res.json()["errmsg"]

    except AssertionError as e:
        print(e.__str__())


# 创建成员
def creat_user(userid, name, mobile, get_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1]
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token}", json=data)
    return res.json()["errmsg"]


# 更新成员
def update(userid, name, get_token):
    data = {
        "userid": userid,
        "name": name
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token}", json=data)
    return  res.json()["errmsg"]


# 删除成员
def delete(userid, get_token):
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token}&userid={userid}')
    return res.json()["errmsg"]

def generate_user():
    while FileLock("session filelock"):

        data=[("linda"+str(x), "AAA", "138%08d"%x) for x in range(10)]
        return data


@pytest.mark.parametrize("userid, name, mobile,",generate_user())
def test_all(userid, name, mobile, get_token):
    #创建用户，若因资源占用创建失败则先找出此用户删除后再创建
    try:
        assert "created" == creat_user(userid, name, mobile, get_token)
    except AssertionError as e:
        del_userid = re.findall(":(.*)", e.__str__())[0]
        if del_userid.endswith("'") or del_userid.endswith('"'):
            del_userid = del_userid[:-1]
            # print(del_userid)
        delete(del_userid, get_token)
        assert "created" == creat_user(userid, name, mobile, get_token)

    # 更新成员
    assert "updated" == update(userid, name, get_token)

    #查询成员
    assert "ok" == get_user(userid, get_token)

    #删除成员
    assert "deleted" == delete(userid, get_token)

