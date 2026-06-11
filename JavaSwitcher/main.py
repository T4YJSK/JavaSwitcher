import os
import subprocess
import pystray
from PIL import Image, ImageDraw
from functools import partial

# ===================== Configuration =====================
# Prioritize checking the script directory; fallback to this default path if not found.
DEFAULT_JAVA_BASE = r"E:\Java"  

def get_java_base():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if any(os.path.exists(os.path.join(script_dir, d, "bin", "java.exe")) for d in os.listdir(script_dir) if os.path.isdir(os.path.join(script_dir, d))):
        return script_dir
    return DEFAULT_JAVA_BASE

# ===================== Scan JDKs =====================
def detect_jdks():
    jdks = {}
    java_base = get_java_base()

    if not os.path.exists(java_base):
        return jdks

    for name in os.listdir(java_base):
        path = os.path.join(java_base, name)
        java_exe = os.path.join(path, "bin", "java.exe")

        if os.path.isdir(path) and os.path.exists(java_exe):
            jdks[name] = path

    return jdks

# ===================== Launch Java =====================
def set_java(path, icon, item):
    """
    Launch CMD by modifying child process environment variables,
    completely eliminating the need for temporary .bat files.
    """
    # Clone and modify the current environment variables
    env = os.environ.copy()
    env["JAVA_HOME"] = path
    env["PATH"] = f"{path}\\bin;" + env["PATH"]

    # Chain initialization commands using '&' to display environment info
    init_cmds = (
        'echo ========================= & '
        f'echo JAVA_HOME={path} & '
        'where java & '
        'java -version & '
        'echo ========================='
    )
    
    # Launch a new window; '/k' keeps the command prompt open
    subprocess.Popen(f'start cmd /k "{init_cmds}"', env=env, shell=True)

# ===================== Icon Generation =====================
def create_image():
    img = Image.new("RGB", (64, 64), (0, 120, 215))
    d = ImageDraw.Draw(img)
    d.rectangle([10, 10, 54, 54], fill="white")
    # Slightly adjusted position for better centering with default fonts
    d.text((28, 20), "J", fill="black")
    return img

# ===================== Dynamic Menu =====================
def get_menu_items():
    """
    This function is called every time the tray menu opens,
    enabling dynamic, real-time JDK list refreshing.
    """
    jdks = detect_jdks()
    
    items = [
        pystray.MenuItem("Java Switcher", lambda icon, item: None, enabled=False),
        pystray.Menu.SEPARATOR,
    ]

    if jdks:
        for name, path in jdks.items():
            items.append(pystray.MenuItem(name, partial(set_java, path)))
    else:
        items.append(pystray.MenuItem("No JDK Detected", lambda icon, item: None, enabled=False))

    items += [
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Exit", lambda icon, item: icon.stop())
    ]
    return items

# ===================== Tray Application =====================
def run_tray():
    icon = pystray.Icon(
        "JavaSwitcher",
        create_image(),
        "Java Switcher",
        # Pass the callable function directly to make the menu dynamic
        menu=pystray.Menu(get_menu_items) 
    )
    icon.run()

# ===================== Main Entry Point =====================
if __name__ == "__main__":
    run_tray()
