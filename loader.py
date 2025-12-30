from pymem import *
import os
import sys
import time
import ctypes

print('Добро пожаловать в лоадер кряка PlagueCheat.cc.')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_internal_path(filename):
    """Определяет путь к файлу, вшитому внутрь EXE"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, filename)

if not is_admin():
    print("!!! ОШИБКА: Запустите программу от имени АДМИНИСТРАТОРА !!!")
    time.sleep(5)
    sys.exit()

path_plsteam = get_internal_path('plsteam.dll')
path_pl = get_internal_path('pl.dll')
os.makedirs(r'C:/plaguecheat.cc', exist_ok=True)

if not os.path.exists(path_plsteam) or not os.path.exists(path_pl):
    print("Ошибка: DLL не найдены во временной папке!")
    time.sleep(10)
    sys.exit()

try:
    steam = Pymem('steam.exe')
    print('Steam найден.')
    pymem.process.inject_dll_from_path(steam.process_handle, path_plsteam)
    print('Инжект: plsteam.dll')
except Exception as e:
    print('Steam не запущен. Запуск.')
    os.startfile('steam://open/main')
    time.sleep(20)
    try:
        steam = Pymem('steam.exe')
        pymem.process.inject_dll_from_path(steam.process_handle, path_plsteam)
        print('Инжект в steam.exe - Успешно.')
    except Exception as e2:
        print(f"Ошибка инжекта в Steam: {e2}")

# --- Запуск CS2 ---
time.sleep(5)
os.startfile('steam://run/730/-allow_third_party_software')
print('Запуск CS2...')
time.sleep(30) # Для надежности увеличил до 30 сек

try:
    cs2 = Pymem('cs2.exe')
    pymem.process.inject_dll_from_path(cs2.process_handle, path_pl)
    print('Инжект в cs2.exe - Успешно.')
except Exception as e:
    print(f"Ошибка инжекта в CS2: {e}")

os.startfile('https://t.me/somethingbio')
time.sleep(10)