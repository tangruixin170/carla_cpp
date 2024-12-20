# Copyright (c) 2019 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.


from . import SmokeTest
//定义一个名为TestClient的类，它继承自SmokeTest类，意味着TestClient类会拥有SmokeTest类的所有公开属性和方法，并且可以在此基础上进行扩展或重写

class TestClient(SmokeTest):
//定义一个实例方法test_version，方法名通常表明了它用于测试某个版本相关的功能
    def test_version(self):
// 打印出字符串，可能用于在测试执行时输出一些提示信息，方便查看测试执行的进度或者确认是否进入到了这个测试方法中
        print("TestClient.test_version")
        self.assertEqual(self.client.get_client_version(), self.client.get_server_version())
//调用self.client对象的get_client_version方法获取客户端版本号，然后和通过self.client对象的get_server_version方法获取的服务器版本号进行比较，
// 利用assertEqual断言来确保这两个版本号是相等的，如果不相等则测试会失败，通常用于验证客户端和服务器版本的一致性
