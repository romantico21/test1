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
        time.sleep(1)
        self.d(resourceId="com.autoai.weather:id/add_city_lay").click()
        time.sleep(1)
        self.d(text="北京市").click()
        time.sleep(1)
        city1 = self.d(resourceId="com.autoai.weather:id/citytext")[1].get_text()
        print(city1)
        assert "北京市" in city1
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)
#        self.d(resourceId="com.autoai.weather:id/addcity_left_btn").click()
#        time.sleep(2)
#        assert "北京市" in city1

    #取消删除城市
    def test02_CancelDeleteCity(self):
        time.sleep(1)
        self.d(resourceId="com.autoai.weather:id/addcity_left_btn").click()
        time.sleep(1)
        self.d.drag(0.84, 0.273,0.44, 0.273)
#        self.d(text="5.0").drag_to(text="多云", timeout=0.5)
        time.sleep(1)
        self.d(resourceId="com.autoai.weather:id/right_lay").click()
        time.sleep(1)
        self.d(resourceId="com.autoai.weather:id/dialog_cancel").click()
        time.sleep(1)
        city1 = self.d(resourceId="com.autoai.weather:id/citytext")[1].get_text()
        assert "北京市" in city1
        self.d.press("back")

    # 确认删除城市
    def test03_DeleteCity(self):
        time.sleep(1)
        self.d(resourceId="com.autoai.weather:id/addcity_left_btn").click()
        time.sleep(1)
        self.d.drag(0.94, 0.273,0.44, 0.273)
        time.sleep(1)
        self.d(resourceId="com.autoai.weather:id/right_lay").click()
        time.sleep(1)
        self.d(resourceId="com.autoai.weather:id/dialog_ok").click()
        time.sleep(1)
        city1 = self.d(resourceId="com.autoai.weather:id/citytext").get_text()
        time.sleep(1)
        print(city1)
#        self.assertFalse(self.d(resourceId="com.autoai.weather:id/citytext")[1].exist)
        self.assertFalse("北京市" in city1)
        time.sleep(1)
        self.d.press("back")

    # 删除本地城市
    def test04_DeleteLocalCity(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.weather:id/addcity_left_btn").click()
        time.sleep(1)
        self.d(text="多云").drag_to(text="深圳市", timeout=0.5)
        time.sleep(1)
        self.d(resourceId="com.autoai.weather:id/right_lay").click()
        time.sleep(1)
        assert "本地天气信息不允许删除" in self.d.toast.get_message(5.0, default="")
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)

    # 查看天气详情
    def test05_ViewWeatherDetails(self):
        time.sleep(2)
        self.d(resourceId="com.autoai.weather:id/weather_desc_lay").click()
        time.sleep(1)
        assert self.d(text="旅游指数 :").exists
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)

    # 搜索城市添加
    def test06_SearchCityAdd(self):
        time.sleep(2)
        self.d(resourceId="com.autoai.weather:id/addcity_left_btn").click()
        time.sleep(1)
        self.d(resourceId="com.autoai.weather:id/add_city_lay").click()
        time.sleep(1)
        self.d.set_fastinput_ime(True)   # 切换成FastInputIME输入法
        time.sleep(5)
        self.d.send_keys("湛江")      # adb广播输入
        time.sleep(5)
        self.d(text="湛江市").click()
        time.sleep(1)
        city1 = self.d(resourceId="com.autoai.weather:id/citytext")[1].get_text()
        print(city1)
        assert "湛江市" in city1
        time.sleep(2)
        self.d.drag(0.94, 0.273,0.44, 0.273)
        time.sleep(2)
        self.d(resourceId="com.autoai.weather:id/right_lay").click()
        time.sleep(1)
        self.d(resourceId="com.autoai.weather:id/dialog_ok").click()
        time.sleep(1)
        self.d.press("back")