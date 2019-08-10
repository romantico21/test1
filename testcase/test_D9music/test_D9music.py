import uiautomator2 as u2
import time
from unittest import TestCase
import unittest

class TestD9music(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb()
        cls.d = cls.u.app_start("com.autoai.car")  # restart app
        time.sleep(7)  # 等待首页广告结束
        print("抖8在线音乐测试开始")

    @classmethod
    def tearDownClass(cls):
        cls.u.app_stop_all()
        cls.u.service(
           "uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行
        print("抖8在线音乐测试结束")

    def setUp(self):
        self.d = u2.connect_usb()
        self.u.app_start("com.autoai.car")
#        self.d = self.u.app_start("com.autoai.car")  # restart app
#        time.sleep(7)  # 等待首页广告结束
#        self.d.watcher("ALERT").when(text="确定").click()  #监控弹框，出现就点击确定取消弹框
#        time.sleep(2)

    def tearDown(self):
        pass

    #点击搜索中热词换一换，并判断是否更换成功
    def test01_clickChange(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(5)
        i = 0
        name1 = []
        while i < 5:
            hotwords1 = self.d(resourceId="com.autoai.car:id/list_hot_search").child(resourceId="com.autoai.car:id/textView")[i].get_text() #遍历进来时的热词
            i = i + 1
            name1.append(hotwords1)
        self.d(resourceId="com.autoai.car:id/tv_change").click()
        time.sleep(2)
        j = 0
        name2 = []
        while j < 5:
            hotwords2  = self.d(resourceId="com.autoai.car:id/list_hot_search").child(resourceId="com.autoai.car:id/textView")[j].get_text() #遍历刷新后的热词
            j = j + 1
            name2.append(hotwords2)
        assert name1 != name2

    #不输入搜索内容时点击搜索
    def test02_notInputSearch(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/tv_search_button").click()
        assert "搜索关键字不能为空" in self.d.toast.get_message(5.0, default="")

    #点击热词搜索
    def test03_clickHotwords(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(5)
        hotword1 = self.d(resourceId="com.autoai.car:id/list_hot_search").child(resourceId="com.autoai.car:id/textView")[0].get_text()
        self.d(resourceId="com.autoai.car:id/list_hot_search").child(resourceId="com.autoai.car:id/textView")[0].click()
        time.sleep(5)
        hotword2 = self.d(resourceId="com.autoai.car:id/textView").get_text()
        assert hotword1 in hotword2

    #手动输入歌手-张学友名称搜索
    def test04_SingerSearch(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(3)
        self.d.set_fastinput_ime(True)   # 切换成FastInputIME输入法
        time.sleep(2)
        self.d.send_keys("张学友")       # adb广播输入
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/tv_search_button").click()
        time.sleep(5)
        hotword1 = self.d(resourceId="com.autoai.car:id/tv_singer").get_text()
        assert hotword1 in "张学友"
        self.d.set_fastinput_ime(False)  # 切换成正常的输入法


    #手动输入单曲-甜甜的称搜索
    def test05_SingleSearch(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(3)
        self.d.set_fastinput_ime(True)   # 切换成FastInputIME输入法
        time.sleep(2)
        self.d.send_keys("甜甜的")       # adb广播输入
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/tv_search_button").click()
        time.sleep(5)
        hotword1 = self.d(resourceId="com.autoai.car:id/tv_music_name").get_text()
        assert "甜甜的" in hotword1
        self.d.set_fastinput_ime(False)  # 切换成正常的输入法

    #手动输入专辑-寻找周杰伦称搜索
    def test06_AlbumSearch(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(3)
        self.d.set_fastinput_ime(True)   # 切换成FastInputIME输入法
        time.sleep(2)
        self.d.send_keys("寻找周杰伦")       # adb广播输入
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/tv_search_button").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/rb_2").click()
        time.sleep(2)
        hotword1 = self.d(resourceId="com.autoai.car:id/tv_album_title").get_text()
        assert "寻找周杰伦" in hotword1
        self.d.set_fastinput_ime(False)  # 切换成正常的输入法

    # 手动输入节目-一些事一些情搜索
    def test07_ProgramSearch(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(3)
        self.d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        time.sleep(2)
        self.d.send_keys("一些事一些情")  # adb广播输入
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/tv_search_button").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/rb_3").click()
        time.sleep(2)
        hotword1 = self.d(resourceId="com.autoai.car:id/tv_album_title").get_text()
        assert "一些事一些情" in hotword1
        self.d.set_fastinput_ime(False)  # 切换成正常的输入法


    # 手动输入歌单-失恋解药搜索
    def test08_SongsheetSearch(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(3)
        self.d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        time.sleep(2)
        self.d.send_keys("失恋解药")  # adb广播输入
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/tv_search_button").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/rb_1").click()
        time.sleep(2)
        hotword1 = self.d(resourceId="com.autoai.car:id/tv_album_title").get_text()
        assert "失恋解药" in hotword1
        self.d.set_fastinput_ime(False)  # 切换成正常的输入法


    #点击清空历史搜索
    def test09_clearhistorySearch(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/list_hot_search").child(resourceId="com.autoai.car:id/textView")[0].click()
        time.sleep(2)
        self.d.press("back")
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/list_hot_search").child(resourceId="com.autoai.car:id/textView")[1].click()
        time.sleep(2)
        self.d.press("back")
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/list_hot_search").child(resourceId="com.autoai.car:id/textView")[3].click()
        time.sleep(2)
        self.d.press("back")
        time.sleep(2)
        self.d(resourceId="com.autoai.car:id/tv_clear").click()
        time.sleep(2)
        self.assertFalse(self.d(resourceId="com.autoai.car:id/list_history_search").exists())

    def test10_test1(self):
        time.sleep(3)
        self.d(resourceId="com.autoai.car:id/rl_search_container").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/list_hot_search").child(resourceId="com.autoai.car:id/textView")[0].click()
        time.sleep(2)


'''
    def test_ergodicRecommendFloating(self):          #遍历推荐列表中浮层菜单，并判断切换成功
        self.d(resourceId="com.autoai.car:id/btn_local").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/rl_recommend").click()
        time.sleep(3)
        categoryname = ['相声精选', '9.9元超值', '精品榜', '有声书', '成长', '新知', '娱乐', '商业', '亲子', '生活', '健康', '情感', '音乐', '外语', '国学教育']
        for i in categoryname:
            self.d(resourceId="com.autoai.car:id/iv_select_category_new").click()
            time.sleep(2)
            if self.d(text=i).exists:                 #先判断菜单是否存在不，不存在就滑动
                self.d(text=i).click()
                time.sleep(2)
                assert self.d(text=i).exists
            else:
                self.d(text="情感").drag_to(text="商业", timeout=0.25)
                time.sleep(2)
                self.d(text=i).click()
                time.sleep(2)
                assert self.d(text=i).exists
        self.d.press("back")

    def test_ergodicFmFloating(self):          #遍历推荐列表中浮层菜单，并判断切换成功
        self.d(resourceId="com.autoai.car:id/btn_local").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/rl_fm").click()
        time.sleep(3)
        categoryname = ['付费节目', '搞笑', '脱口秀', '儿童', '音乐FM', '情感', '历史', '汽车', '人文', '科技', '财经',
                        '教育', '英文', '旅游', '戏曲', '电影', '游戏动漫', '健康养生', '广播剧', '0.1元听书']
        for i in categoryname:
            self.d(resourceId="com.autoai.car:id/iv_select_category_new").click()
            time.sleep(2)
            if self.d(text=i).exists:                 #先判断菜单名是否存在不，不存在就先滑动
                self.d(text=i).click()
                time.sleep(2)
                assert self.d(text=i).exists
            else:
                self.d(text="教育").drag_to(text="儿童",timeout=0.25)
                time.sleep(2)
                self.d(text=i).click()
                time.sleep(2)
                assert self.d(text=i).exists
        self.d.press("back")

    def test_SlideRecommendlist(self):          #热门推荐列表上下滑动
        self.d(resourceId="com.autoai.car:id/btn_local").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/rl_recommend").click()
        time.sleep(3)
        self.d(text="热门推荐").click()
        time.sleep(2)
        self.d.swipe(0.393, 0.440, 0.393, 0.126, 0.5)  #上滑三次
        time.sleep(1)
        self.d.swipe(0.393, 0.440, 0.393, 0.126, 0.5)
        time.sleep(1)
        self.d.swipe(0.393, 0.440, 0.393, 0.126, 0.5)
        time.sleep(1)
        self.d.swipe(0.393, 0.126, 0.393, 0.440, 0.5) #下滑三次
        time.sleep(1)
        self.d.swipe(0.393, 0.126, 0.393, 0.440, 0.5)
        time.sleep(1)
        self.d.swipe(0.393, 0.126, 0.393, 0.440, 0.5)
        time.sleep(2)
        assert self.d(text="热门推荐").exists
        self.d.press("back")

    def test_SlideMusiclist(self):          #上下滑动音乐列表
        self.d(resourceId="com.autoai.car:id/btn_local").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/rl_music").click()
        time.sleep(3)
        self.d(text="歌单广场").click()
        time.sleep(2)
        self.d.swipe(0.393, 0.440, 0.393, 0.126, 0.5)  #上滑三次
        time.sleep(1)
        self.d.swipe(0.393, 0.440, 0.393, 0.126, 0.5)
        time.sleep(1)
        self.d.swipe(0.393, 0.440, 0.393, 0.126, 0.5)
        time.sleep(1)
        self.d.swipe(0.393, 0.126, 0.393, 0.440,0.5) #下滑三次
        time.sleep(1)
        self.d.swipe(0.393, 0.126, 0.393, 0.440,0.5)
        time.sleep(1)
        self.d.swipe(0.393, 0.126, 0.393, 0.440,0.5)
        time.sleep(2)
        assert self.d(text="歌单广场").exists
        self.d.press("back")

    def test_SlideFMlist(self):          # 上下滑动FM列表
        self.d(resourceId="com.autoai.car:id/btn_local").click()
        time.sleep(5)
        self.d(resourceId="com.autoai.car:id/rl_fm").click()
        time.sleep(3)
        self.d(text="热门").click()
        time.sleep(2)
        self.d.swipe(0.393, 0.440, 0.393, 0.126, 0.5)  #上滑三次
        time.sleep(1)
        self.d.swipe(0.393, 0.440, 0.393, 0.126, 0.5)
        time.sleep(1)
        self.d.swipe(0.393, 0.440, 0.393, 0.126, 0.5)
        time.sleep(1)
        self.d.swipe(0.393, 0.126, 0.393, 0.440, 0.5)  #下滑三次
        time.sleep(1)
        self.d.swipe(0.393, 0.126, 0.393, 0.440,0.5)
        time.sleep(1)
        self.d.swipe(0.393, 0.126, 0.393, 0.440,0.5)
        time.sleep(2)
        assert self.d(text="热门").exists
        self.d.press("back")
'''