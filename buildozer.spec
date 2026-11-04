[app]
title = NokiaTV
package.name = nokiatv
package.domain = com.nokia.tv

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.include_patterns = assets/*,images/*,data/*

version = 1.0
version.regex = __version__ = ['"]([^'"]*)['"]
version.filename = %(source.dir)s/main.py

requirements = python3,kivy,requests,urllib3,certifi

orientation = landscape
fullscreen = 0

[buildozer]
log_level = 2

# Android specific
[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer:android]
android.permissions = INTERNET,ACCESS_NETWORK_STATE
