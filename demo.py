import unittest
import time
import requests
import sys
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException


sys.tracebacklimit = 0
warnings.filterwarnings("ignore")

class YouTubeTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new") 
        options.add_argument("--log-level=3")   
        options.add_argument("--disable-notifications")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.set_page_load_timeout(20)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.youtube.com/")

    def test_1_homepage_loads(self):
        """Verify YouTube homepage loads correctly"""
        driver = self.driver
        if "YouTube" in driver.title:
            print("✅ YouTube homepage loaded successfully")
        else:
            print("❌ Failed to load YouTube homepage")
            self.fail()

    def test_2_search_functionality(self):
        """Check if search bar works"""
        driver = self.driver
        try:
            search_box = driver.find_element(By.NAME, "search_query")
            search_box.send_keys("Selenium Python tutorial")
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            results = driver.find_elements(By.ID, "video-title")
            if len(results) > 0:
                print("✅ Search returned results successfully")
            else:
                print("❌ Search returned no results")
                self.fail()
        except NoSuchElementException:
            print("❌ Search bar not found")
            self.fail()

    def test_3_check_trending_link(self):
        """Check if 'Trending' or 'Explore' section is accessible"""
        driver = self.driver
        driver.get("https://www.youtube.com/feed/explore")
        time.sleep(3)
        if "Explore" in driver.title or "Trending" in driver.page_source:
            print("✅ 'Explore' page loaded successfully")
        else:
            print("❌ 'Explore' page did not load properly")
            self.fail()

    def test_4_check_video_playback(self):
        """Open a video and verify playback starts"""
        driver = self.driver
        driver.get("https://www.youtube.com/results?search_query=lofi+music")
        time.sleep(3)
        try:
            video = driver.find_elements(By.ID, "video-title")[0]
            video.click()
            time.sleep(5)
            play_button = driver.find_element(By.CSS_SELECTOR, "button.ytp-play-button")
            aria_label = play_button.get_attribute("title")
            if "Pause" in aria_label or "Play" in aria_label:
                print("✅ Video loaded and playback controls found")
            else:
                print("❌ Playback controls missing")
                self.fail()
        except Exception:
            print("❌ Could not load video or playback failed")
            self.fail()

    def test_5_check_broken_links(self):
        """Check for broken links on the YouTube homepage (sample)"""
        driver = self.driver
        driver.get("https://www.youtube.com/")
        links = [a.get_attribute("href") for a in driver.find_elements(By.TAG_NAME, "a") if a.get_attribute("href")]
        broken_links = []
        for link in links[:20]:  # limit for performance
            try:
                r = requests.head(link, timeout=5)
                if r.status_code >= 400:
                    broken_links.append(link)
            except Exception:
                broken_links.append(link)
        if broken_links:
            print(f"❌ Broken links found: {broken_links}")
        else:
            print("✅ No broken links found")
        self.assertEqual(len(broken_links), 0)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=0)  # Clean readable output only
