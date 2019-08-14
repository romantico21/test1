import uiautomator2 as u2
import time
from unittest import TestCase

class Testweather(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb()
        cls.d = cls.u.app_start("com.autoai.weather")  # restart app
        time.sleep(7)  # 等待首页广告结束
        print("车载天气测试开始")

    @classmethod
    def tearDownClass(cls):
        cls.u.app_stop_all()
        cls.u.service(
           "uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行
        print("车载天测试结束")

    def setUp(self):
        self.d = u2.connect_usb()
        self.u.app_start("com.autoai.weather")
#        self.d = self.u.app_start("com.autoai.car")  # restart app
#        time.sleep(7)  # 等待首页广告结束
#        self.d.watcher("ALERT").when(text="确定").click()  #监控弹框，出现就点击确定取消弹框
#        time.sleep(2)

    def tearDown(self):
        pass

#进入车载天气添加城市
    def test01_AddCity(self):
        time.sleep(2)
        self.d(resourceId="com.autoai.weather:id/addcity_left_btn").click()
        time.sleep(2)
        self.d(resourceId="com.autoai.weather:id/add_city_lay").click()
        time.sleep(2)
        self.d(text="北京市").click()
        time.sleep(2)
        city1 = self.d(resourceId="com.autoai.weather:id/citytext")[1].get_text()
        print(city1)
        assert "北京市" in city1
        time.sleep(2)
        self.d.press("back")
        time.sleep(2)
#        self.d(resourceId="com.autoai.weather:id/addcity_left_btn").click()
#        time.sleep(2)
#        assert "北京市" in city1

    def test02_CancelDeleteCity(self):
        time.sleep(2)
        self.d(resourceId="com.autoai.weather:id/addcity_left_btn").click()
        time.sleep(2)
        self.d.drag(0.84, 0.273,0.44, 0.273)
#        self.d(text="5.0").drag_to(text="多云", timeout=0.5)
        time.sleep(2)
        self.d(resourceId="com.autoai.weather:id/right_lay").click()
        time.sleep(2)
        self.d(resourceId="com.autoai.weather:id/dialog_cancel").click()
        time.sleep(2)
        city1 = self.d(resourceId="com.autoai.weather:id/citytext")[1].get_text()
        assert "北京市" in city1

    def test03_DeleteCity(self):
        time.sleep(2)
        self.d.drag(0.94, 0.273,0.44, 0.273)
        time.sleep(2)
        self.d(resourceId="com.autoai.weather:id/right_lay").click()
        time.sleep(2)
        self.d(resourceId="com.autoai.weather:id/dialog_ok").click()
        time.sleep(2)
        i = 0
        city1 = []
        while i < 5:
            hotwords1 = self.d(resourceId="com.autoai.weather:id/citytext")[i].get_text() #遍历天气城市的名称
            i = i + 1
            city1.append(hotwords1)
        time.sleep(2)
        print(city1)
        self.assertFalse("北京市" in city1)



'''
class TestD9Collection(TestCase):
    #点击搜索中换一换
    def test_clickChange(self):
        u = u2.connect_usb()
        self.d = u.app_start("com.autoai.car")
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(5)
        name1 = self.d(resourceId="com.autoai.car:id/list_hot_search").child(resourceId="com.autoai.car:id/textView").get_text()
        self.d(resourceId="com.autoai.car:id/tv_change").click()
        time.sleep(2)
        name2 = self.d(resourceId="com.autoai.car:id/list_hot_search").child(resourceId="com.autoai.car:id/textView").get_text()
        assert name2 != name1
'''

'''
    def test_Conllection(self):
        self.d(resourceId="com.autoai.car:id/btn_local").click()
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/rl_music").click()
        time.sleep(2)
        n = 100
        sum = 0
        counter = 1
        while counter <= n:
            sum = sum + counter
            self.d(resourceId="com.autoai.car:id/iv_play_bar_next").click()
            counter += 1
        time.sleep(2)
        assert self.d(text="歌单广场").exists
'''