import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Karena Flutter di project ini tidak menggunakan named route (seperti /#/register),
# melainkan menggunakan Navigator.push() dari halaman Login,
# kita harus membuka halaman utama (/) terlebih dahulu.
url = "http://localhost:64852/" # Pastikan port ini sesuai dengan terminal Flutter Anda
driver.get(url)

try:
    print("Menunggu SplashScreen (5 detik)...")
    time.sleep(5)
    
    actions = ActionChains(driver)

    # 1. Kita berada di halaman Login sekarang.
    # Fokuskan ke window dengan mengklik ujung kiri atas agar tidak sengaja mengklik tombol.
    actions.move_by_offset(10, 10).click().perform()
    time.sleep(1)

    print("Berada di Halaman Login. Mencari tombol 'Daftar di sini'...")
    # Urutan TAB di halaman Login:
    # 1. Field Username
    # 2. Field Password
    # 3. Tombol Login
    # 4. Tombol "Daftar di sini"
    actions.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
    
    print("Menunggu transisi ke halaman Register...")
    time.sleep(2)

    # 2. Sekarang kita berada di halaman Register.
    # Urutan TAB di halaman Register:
    # 1. Tombol Back (Panah kiri)
    # 2. Field Username
    # 3. Field Password
    # 4. Field Konfirmasi Password
    # 5. Field Nama Lengkap
    # 6. Field NPM
    # 7. Dropdown Kategori
    # 8. Tombol Daftar

    # Tekan TAB 2 kali untuk menuju ke field Username (Melewati tombol back)
    print("Menuju field Username...")
    actions.send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
    time.sleep(1)
    
    # Mengisi Username
    print("Mengisi field Username...")
    actions.send_keys("testuser123").perform()
    time.sleep(1)

    # Pindah dan Mengisi Password
    print("Mengisi field Password...")
    actions.send_keys(Keys.TAB).send_keys("password123").perform()
    time.sleep(1)

    # Pindah dan Mengisi Konfirmasi Password
    print("Mengisi field Konfirmasi Password...")
    actions.send_keys(Keys.TAB).send_keys("password123").perform()
    time.sleep(1)

    # Pindah dan Mengisi Nama Lengkap
    print("Mengisi field Nama Lengkap...")
    actions.send_keys(Keys.TAB).send_keys("Ananda Raka Aditya Wilangga").perform()
    time.sleep(1)

    # Pindah dan Mengisi NPM
    print("Mengisi field NPM...")
    actions.send_keys(Keys.TAB).send_keys("714230023").perform()
    time.sleep(1)

    # Pindah melewati Dropdown Kategori dan menuju tombol Daftar
    print("Mengklik tombol Daftar...")
    # 1x TAB -> Dropdown Kategori
    # 2x TAB -> Tombol Daftar
    actions.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        
    print("Selesai menekan tombol Daftar! Tunggu respons dari backend...")
    # Tambahkan penundaan waktu untuk melihat popup sukses/gagal
    time.sleep(10)
    
except Exception as e:
    print(f"Terjadi kesalahan: {e}")

finally:
    print("Menutup browser...")
    driver.quit()
