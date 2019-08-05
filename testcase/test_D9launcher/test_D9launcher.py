import uiautomator2 as u2
import time
from unittest import TestCase

class TestD9launcher(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb()
        cls.d = cls.u.session("com.autoai.car")  # restart app
        time.sleep(7)  # 等待首页广告结束
        print("D9桌面测试开始")

    @classmethod
    def tearDownClass(cls):
        cls.u.app_stop_all()
        cls.u.service(
            "uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行
        print("D9桌面测试结束")

    def setUp(self):
#        self.d = self.u.session("com.autoai.car")  # restart app
#        time.sleep(7)  # 等待首页广告结束
        self.d.watcher("ALERT").when(text="确定").click() #监控弹框，出现就点击确定取消弹框
        time.sleep(2)

    def tearDown(self):
        pass

    def test_playstarmusic(self):
        self.d(resourceId="com.autoai.car:id/iv_car_logo").click()
        time.sleep(5)
        assert self.d(resourceId="com.autoai.car:id/fl_voice").exists
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/iv_close").click()
        time.sleep(2)

    def test_changlistmode(self):
        self.d(resourceId="com.autoai.car:id/tv_list_mode").click()
        time.sleep(5)
        assert self.d(resourceId="com.autoai.car:id/tv_planet_mode").exists
        self.d(resourceId="com.autoai.car:id/tv_planet_mode").click()
        time.sleep(2)

    def test_changstarmode(self):
        self.d(resourceId="com.autoai.car:id/tv_list_mode").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/tv_planet_mode").click()
        time.sleep(5)
        assert self.d(resourceId="com.autoai.car:id/tv_list_mode").exists
        time.sleep(2)

    def test_Jumplocal(self):
        self.d(resourceId="com.autoai.car:id/btn_local").click()
        time.sleep(5)
        assert self.d(text="我的收藏").exists
        self.d.press("back")

    def test_JumpRecommend(self):
        self.d(text="推荐").click()
        time.sleep(3)
        assert self.d(text="热门推荐").exists
        self.d.press("back")

    def test_JumpNews(self):
        self.d(text="新闻").click()
        time.sleep(3)
        assert self.d(text="新闻").exists
        self.d.press("back")

    def test_JumpMusicRadio(self):
        self.d(text="音乐电台").click()
        time.sleep(3)
        assert self.d(text="音乐电台").exists
        self.d.press("back")

    def test_JumpCustom(self):
        self.d(resourceId="com.autoai.car:id/tv_custom").click()
        time.sleep(5)
        assert self.d(text="我的应用").exists
        self.d(resourceId="com.autoai.car:id/custom_close").click()
        time.sleep(2)

    def test_Jumpplayer(self):
        self.d(resourceId="com.autoai.car:id/tv_music_name").click()
        time.sleep(3)
        assert self.d(resourceId="com.autoai.car:id/cl_detail").exists
        self.d.press("back")

    def test_Lyric(self):
        self.d(resourceId="com.autoai.car:id/tv_word").click()
        time.sleep(3)
        assert self.d(resourceId="com.autoai.car:id/ll_source").exists
        self.d(resourceId="com.autoai.car:id/iv_close").click()
        self.d.press("back")

    def test_changeCustom(self):
        self.d(resourceId="com.autoai.car:id/tv_custom").click()
        time.sleep(2)
        self.d(text="教育").drag_to(text="新闻", timeout=0.5)
        time.sleep(2)
        self.d(text="完成").click()
        time.sleep(2)
        assert self.d(text="教育").exists
        time.sleep(2)
        self.d(text="教育").click()
        time.sleep(2)
        assert self.d(text="教育").exists
        self.d.press("back")
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/tv_custom").click()
        time.sleep(2)
        self.d(text="音乐电台").drag_to(text="教育",timeout=0.5)
        time.sleep(2)
        self.d(text="新闻").drag_to(text="教育",timeout=0.5)
        time.sleep(2)
        self.d(text="完成").click()
        time.sleep(2)

    def test_starmoderefresh(self):
        if self.d(resourceId="com.autoai.car:id/tv_list_mode").exists:
            self.d(resourceId="com.autoai.car:id/btn_refresh").click()
            time.sleep(15)
            assert self.d(resourceId="com.autoai.car:id/iv_car_logo").exists
        else:
            self.d(resourceId="com.autoai.car:id/tv_planet_mode").click()
            time.sleep(2)
            self.d(resourceId="com.autoai.car:id/btn_refresh").click()
            time.sleep(15)
            assert self.d(resourceId="com.autoai.car:id/iv_car_logo").exists

    def test_listmoderefresh(self):
        if self.d(resourceId="com.autoai.car:id/tv_planet_mode").exists:
            self.d(resourceId="com.autoai.car:id/btn_refresh").click()
            time.sleep(15)
            assert self.d(resourceId="com.autoai.car:id/iv_car_logo").exists
        else:
            self.d(resourceId="com.autoai.car:id/tv_list_mode").click()
            time.sleep(2)
            self.d(resourceId="com.autoai.car:id/btn_refresh").click()
            time.sleep(15)
            assert self.d(resourceId="com.autoai.car:id/iv_car_logo").exists
            self.d(resourceId="com.autoai.car:id/tv_planet_mode").click()

    def test_menuMyconcern(self):
        self.d(resourceId="com.autoai.car:id/btn_home_menu").click()
        time.sleep(2)
        self.d(text="我的关注").click()
        time.sleep(5)
        assert self.d(text="我的关注").exists
        self.d.press("back")

    def test_menuMysharing(self):
        self.d(resourceId="com.autoai.car:id/btn_home_menu").click()
        time.sleep(2)
        self.d(text="我的分享").click()
        time.sleep(5)
        assert self.d(text="我的分享语").exists
        self.d.press("back")

    def test_menuMusicLabel(self):
        self.d(resourceId="com.autoai.car:id/btn_home_menu").click()
        time.sleep(2)
        self.d(text="音乐标签").click()
        time.sleep(5)
        assert self.d(text="音乐标签").exists
        self.d(resourceId="com.autoai.car:id/iv_close").click()
