# ☕ JavaSwitcher

A lightweight Windows tray tool for switching between multiple JDK versions instantly.

---

## 🚀 Features

- 🧠 Auto-detects installed JDKs
- 🖱 One-click Java version switching
- 🪟 Opens new CMD with selected Java environment
- ⚡ No admin required
- 🪶 Lightweight and simple
- 📁 Supports multiple JDK folders (jdk-8 / jdk-11 / jdk-17 / jdk-21)

---

## 📸 Preview

Example tray menu:

Java Switcher
jdk-8
jdk-17
jdk-21

Exit


---

## 📦 Installation

### 1. Clone repository

```bash
git clone https://github.com/your-username/JavaSwitcher.git
cd JavaSwitcher
2. Install dependencies
pip install pystray pillow
3. Run
python main.py
```
## 📁 JDK Directory Structure

Default scan path:

E:\Java
├── jdk-8
├── jdk-11
├── jdk-17
└── jdk-21

Each JDK must include:

bin/java.exe

## ⚙ How it works
Scans JDK directory
Builds tray menu dynamically
Launches CMD with JAVA_HOME set temporarily

## ❗ Notes

Windows only
Requires correct JDK folder structure
No system modification (safe)
