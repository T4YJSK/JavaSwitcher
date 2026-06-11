# ☕ JavaSwitcher - Lightweight Java Version Switcher

A simple Windows tray tool for switching between multiple JDK installations instantly.

---

## 🚀 Features

- 🧠 Automatically detects installed JDKs
- 🖱 Switch Java version with one click
- 🪟 Opens new CMD with selected Java environment
- 📁 Supports multiple JDK folders (jdk-8 / jdk-11 / jdk-17 / jdk-21 etc.)
- ⚡ No admin required
- 🪶 Lightweight and dependency minimal

---

## 📸 Preview

(You can add screenshot here later)

---

## 📦 Installation

### 1. Install dependencies

```bash
pip install pystray pillow

---

2. Run directly
python main.py
📁 JDK Directory Structure

This tool scans JDKs from a base directory like:

E:\Java
 ├── jdk-8
 ├── jdk-11
 ├── jdk-17
 └── jdk-21

Each folder must contain:
bin/java.exe

---

⚙ How It Works
The tool scans the configured Java directory
Displays all valid JDKs in system tray menu
Clicking a version opens a new terminal with:
  JAVA_HOME set
  PATH updated temporarily

---

❗ Limitations
Windows only
Requires JDK folders to follow standard structure
Tray menu is static (by design for stability)

---

🧠 Why this tool exists

Switching Java versions manually is slow and error-prone.
This tool simplifies it into a one-click workflow.