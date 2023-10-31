[app]

# (str) Title of your application
title = Number System Converter

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = kivy

# (str) Custom source folders for requirements
source.kivy = /path/to/your/kivy/installation

# (list) Garden requirements
#garden_requirements = 

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY

# (str) Application version
version = 1.0

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY

# (bool) Skip the build of certain requirements (comma separated)
skip_deps_install = False

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to a custom buildozer.spec file
# buildozer.spec =

# (str) buildozer folder to use for this build (default is the root of the source code)
# build_dir = .buildozer

# (str) Path to a custom distribution
# dist_name = myapp

# (str) Plist to add
# plist =

# (str) Application name
# package.name = myapp

# (str) Application version (source: https://python.org/dev/peps/pep-0440)
# package.version = 0.1

# (int) Application version code
# package.version_code = 1

# (str) Orientation (choices are: landscape, portrait, all, or tablet)
orientation = portrait

# (bool) Change the color of the code
# only works if you don't use the outputcolor option
# color = 0

# (bool) Create a package using python-for-android
create = 1

# (bool) Use a black terminal background
# black = 0

# (str) Title of the application
# title = My Application

# (str) Package name
# package.name = myapp

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
# orientation = portrait

# (str) Application version
# version = 1.0

# (int) Version code - increment by one with each release
# version.code = 1

# (str) URL of your source repository (if available)
# vcs_url = 

# (str) Path to script that will be run at the end of the build process
# postdeploy = my_postdeploy.py

# (list) Application permissions
# android.permissions = INTERNET

# (int) Android API to use
# android.api = 14

# (int) Android API level to use for the default/first target (default is 28)
# android.minapi = 21

# (int) Android API level to use for the default/first target (default is 28)
# android.minapi.default = 14

# (int) Android NDK API to use (optional)
# android.ndk_api = 21

# (int) Android NDK API for the default/first target (optional, default is 28)
# android.ndk_api.default = 21

# (bool) use newest available android ndk (optional)
# android.ndk_use_newest = False

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path = 

# (str) ANT directory (if empty, it will be automatically downloaded.)
# android.ant_path = 

# (str) Android NDK version to use
# android.ndk_version = 21c

# (int) Android NDK toolchain to use (optional, default is 4.9)
# android.toolchain = 4.9

# (int) Android NDK toolchain version to use (optional, default is 4.8)
# android.toolchain_version = 4.9

# (str) Android API / SDK / NDK download cache
# android.cache = downloads

# (list)
