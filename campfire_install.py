"""篝火：首次启动时的收尾安装 —— 生成 conf.py，并下载浏览器内核（patchright Chromium）。"""
import os
import shutil
import subprocess
import sys

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

if not os.path.exists("conf.py"):
    shutil.copy("conf.example.py", "conf.py")
    print("已生成 conf.py")

cmd = [sys.executable, "-m", "patchright", "install", "chromium"]
print("正在下载浏览器内核 Chromium（约 100~200 MB），请稍候...")
code = 1
# 选了国内镜像加速时先试国内镜像；镜像里缺这个版本（404）时自动改用官方地址
if os.environ.get("UV_DEFAULT_INDEX") and "PLAYWRIGHT_DOWNLOAD_HOST" not in os.environ:
    env = dict(os.environ, PLAYWRIGHT_DOWNLOAD_HOST="https://npmmirror.com/mirrors/playwright")
    code = subprocess.call(cmd, env=env)
    if code != 0:
        print("国内镜像下载失败，改用官方地址重试...")
if code != 0:
    code = subprocess.call(cmd)
sys.exit(code)
