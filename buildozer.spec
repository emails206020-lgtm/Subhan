[app]

title = سُبْحَان
package.name = subhan_app
package.domain = com.drasimelnegar

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,otf,ttc,wav,mp3,json

version = 3.0.0

requirements = python3==3.11.8,hostpython3==3.11.8,kivy==2.3.0,plyer,arabic-reshaper,python-bidi==0.4.2,cython==3.0.11

orientation = portrait
fullscreen = 0

icon.filename = icon.png
presplash.filename = presplash.png
android.presplash_color = #0A1628
android.meta_data = presplash-fit=cover

android.permissions = INTERNET,VIBRATE,WAKE_LOCK,POST_NOTIFICATIONS

android.api = 34
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

android.enable_androidx = True
android.debug = True

[buildozer]
log_level = 2
warn_on_root = 1