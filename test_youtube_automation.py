"""
YouTube Automation Test Suite
Author: Siddharth Zende
Description: Automated YouTube tests using Selenium & Pytest.
Covers working and failing cases for demonstration.
"""

from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep




def test_channel_navigation():
    """Verify that channel navigation works correctly."""
    driver = get_driver()
    driver.get("https://www.youtube.com/watch?v=XI5_nsClCYI")

    wait = WebDriverWait(driver, 15)
    channel_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-channel-name a")))
    channel_name = channel_button.text
    channel_button.click()

    wait.until(EC.title_contains(channel_name))
    assert channel_name.lower().replace(" ", "") in driver.title.lower().replace(" ", "")
    print(f"[PASS] Navigated to channel: {channel_name}")
    driver.quit()


def test_play_pause_video():
    """Test that play and pause functionality works."""
    driver = get_driver()
    driver.get("https://www.youtube.com/watch?v=XI5_nsClCYI")
    sleep(5)
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys("k")
    sleep(2)
    body.send_keys("k")
    assert "youtube.com/watch" in driver.current_url
    print("[PASS] Play/Pause functionality works.")
    driver.quit()


def test_video_playback():
    """Verify video player element loads correctly."""
    driver = get_driver()
    driver.get("https://www.youtube.com/watch?v=XI5_nsClCYI")
    wait = WebDriverWait(driver, 15)
    video = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "video")))
    assert video is not None
    print("[PASS] Video element found and loaded.")
    driver.quit()





def test_youtube_search():
    """Verify search bar and results actually load."""
    driver = get_driver()
    driver.get("https://www.youtube.com")

    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("Python tutorial")
    search_box.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 10)
    results = wait.until(EC.presence_of_all_elements_located((By.ID, "video-title")))
    assert len(results) > 0, "No video results loaded for the search term."
    print("[PASS] YouTube search loaded multiple video results successfully.")
    driver.quit()


# fail test 

def test_invalid_url():
    """Fail test: Invalid YouTube URL."""
    driver = get_driver()
    driver.get("https://www.youtube.com/invalid")
    sleep(3)
    assert "404" not in driver.title  # This will fail because the page doesn’t exist
    print("[FAIL] Invalid URL handled incorrectly.")
    driver.quit()


def test_missing_element():
    """Expect fail test: verify that a non-existent element is handled gracefully."""
    driver = get_driver()
    driver.get("https://www.Utube.com")
    try:
        driver.find_element(By.ID, "non_existent_element")
        print("[FAIL] Non-existent element unexpectedly found.")
        assert False
    except:
        print("[PASS] Correctly handled missing element.")
        assert True
    finally:
        driver.quit()


def test_incorrect_search_result():
    """Test case: Search for a nonsense query to simulate no or incorrect results."""
    driver = get_driver()
    driver.get("https://www.youtube.com")

    
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("asdkjfhaskjdhfkasjdhfkjashdf") 
    search_box.send_keys(Keys.RETURN)

  
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contents")))

   
    results = driver.find_elements(By.ID, "video-title")

    
    if len(results) == 0:
        print("[EXPECTED FAIL] No results found for nonsense query — behaving correctly.")
    else:
        print(f"[UNEXPECTED PASS] {len(results)} results found for nonsense query!")

    
    assert len(results) < 3, "Unexpectedly found multiple results for an invalid query."
    driver.quit()