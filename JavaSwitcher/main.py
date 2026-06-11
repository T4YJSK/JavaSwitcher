import os
import subprocess
import tempfile
import pystray
from PIL import Image, ImageDraw
from functools import partial

# ===================== 自动从脚本目录或固定目录 =====================
JAVA_BASE = r"E:\Java"   # 你可以改这里

# ===================== 扫描 JDK =====================
def detect_jdks():
    jdks = {}

    if not os.path.exists(JAVA_BASE):
        return jdks

    for name in os.listdir(JAVA_BASE):
        path = os.path.join(JAVA_BASE, name)

        java_exe = os.path.join(path, "bin", "java.exe")

        if os.path.isdir(path) and os.path.exists(java_exe):
            jdks[name] = path

    return jdks

# ===================== 启动 Java =====================
def open_java_terminal(path):
    bat = f"""@echo off
set JAVA_HOME={path}
set PATH=%JAVA_HOME%\\bin;%PATH%

echo =========================
echo JAVA_HOME=%JAVA_HOME%
where java
java -version
echo =========================

cmd
"""

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".bat", mode="w", encoding="utf-8")
    tmp.write(bat)
    tmp.close()

    subprocess.Popen(f'start cmd /k "{tmp.name}"', shell=True)

# ===================== JDK切换 =====================
def set_java(path, icon, item):
    open_java_terminal(path)

# ===================== 图标 =====================
def create_image():
    img = Image.new("RGB", (64, 64), (0, 120, 215))
    d = ImageDraw.Draw(img)
    d.rectangle([10, 10, 54, 54], fill="white")
    d.text((22, 22), "J", fill="black")
    return img

# ===================== 固定菜单（关键修复点） =====================
def build_menu():
    jdks = detect_jdks()

    items = [
        pystray.MenuItem("Java Switcher", lambda icon, item: None, enabled=False),
        pystray.Menu.SEPARATOR,
    ]

    if jdks:
        for name, path in jdks.items():
            items.append(pystray.MenuItem(name, partial(set_java, path)))
    else:
        items.append(pystray.MenuItem("未检测到JDK", lambda icon, item: None, enabled=False))

    items += [
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("退出", lambda icon, item: icon.stop())
    ]

    return pystray.Menu(*items)

# ===================== 托盘 =====================
def run_tray():
    icon = pystray.Icon(
        "JavaSwitcher",
        create_image(),
        "Java Switcher",
        menu=build_menu()   # ⚠ 注意：必须是 Menu 对象
    )

    icon.run()

# ===================== 主程序 =====================
if __name__ == "__main__":
    run_tray()