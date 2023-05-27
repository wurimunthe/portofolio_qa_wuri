from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install()) # BUKA BROWSER SESUAI VERSI CHROME DI LAPTOP
browser.get("https://www.instagram.com/") # BUKA LINK WEB YANG DITUJU
time.sleep(5) # JEDA 5 DETIK
assert browser.title == "Instagram" # VERIFIKASI BAHWA JUDUL WEB/TULISAN DI TAB = Instagram
