import pytest

# chrom の webdriver の情報
from selenium import webdriver
# html の タブの情報を取得
from selenium.webdriver.common.by import By
# キーボードを叩いた時に web ブラウザに情報を送信する
from selenium.webdriver.common.keys import Keys
# 次にクリックしたページがどんな状態になっているかチェックする
from selenium.webdriver.support import expected_conditions as EC
# 待機時間を設定
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

class TestPythonOrgTest(object):
    def setup_method(self):
        # webdriver を指定(chorme)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1280,1024')
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self):
        self.driver.close()

    # webdriver の立ち上げ
    def test_python_org(self):
        # 指定したURLへ移動
        self.driver.get('http://www.python.org')

        #　画面イメージの取得
        self.driver.save_screenshot('test_python_org.png')

    def test_aster(self):
        self.driver.get('http://aster.or.jp/business/contest.html')
        self.driver.save_screenshot('test_aster.png')
