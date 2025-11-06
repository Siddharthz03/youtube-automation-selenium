# 🎥 YouTube Automation Test Suite  
### **Author:** Siddharth Zende  
### **Tech Stack:** Python, Selenium WebDriver, Pytest  

---

## 📌 Project Overview  
This project is an automated **YouTube Testing Suite** developed using **Selenium** and **Pytest**.  
The test suite imitates real user interactions on YouTube and verifies functionalities like:

- Playing and pausing a video  
- Navigating to the channel page  
- Validating YouTube search results  
- Loading of video playback element  
- Handling invalid URLs  
- Handling missing elements  
- Testing incorrect or nonsense search queries  

It includes both **positive tests** (expected to pass) and **negative tests** (expected to fail) — useful for demonstrating real QA testing scenarios.

---

## ✅ Features Tested

### ✅ **Functional Test Cases**
✔ **Channel Navigation** – Verifies that clicking the channel name redirects correctly  
✔ **Play/Pause Functionality** – Uses YouTube keyboard shortcuts  
✔ **Video Playback Check** – Ensures `<video>` element loads  
✔ **Search Verification** – Confirms video results appear for valid queries  

### ❌ **Negative Test Cases**
❌ **Invalid URL Handling** – Tests how YouTube responds to a broken URL  
❌ **Missing Element Handling** – Verifies script behavior when element is not found  
❌ **Incorrect Search Query** – Searches random gibberish to test “No Results” behavior  

---

## 📁 Project Structure
youtube-automation-selenium/
│
├── tests/
│   └── test_youtube_suite.py
│
├── utils/
│   └── driver_setup.py
│
├── requirements.txt
└── README.md

---

## ⚙️ Tools & Libraries

- **Python 3.10+**
- **Selenium WebDriver**
- **Pytest**
- **ChromeDriver or EdgeDriver**
- **Explicit Waits (WebDriverWait + Expected Conditions)**

---

## 🚀 How to Run the Tests

### ✅ Install Required Libraries
pip install -r requirements.txt
### ✅ Run All Tests
pytest -v
### ✅ Run a Specific Test
pytest tests/test_youtube_suite.py::test_youtube_search

---

## 💡 What This Project Demonstrates

This automation suite showcases:

- Web UI automation using Selenium  
- Functional + Negative testing approach  
- Use of Explicit Waits for stable test execution  
- Keyboard event handling in Selenium  
- Pytest assertions and reporting  
- Exception handling in automation  
- Real-world test case design  

---

## 📌 Author
**Siddharth Zende**  
Automation & Python Developer  
GitHub: [Siddharthz03](https://github.com/Siddharthz03)

---

# ✅ End of README.md
