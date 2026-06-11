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

<img width="175" height="156" alt="image" src="https://github.com/user-attachments/assets/2b1f2e97-db17-48ba-9b54-099c4363f5ee" />



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
## 📁Modify the actual folder
<img width="759" height="195" alt="image" src="https://github.com/user-attachments/assets/8a49cf5b-cec6-42bf-91b5-8f3c19aec32a" />



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
