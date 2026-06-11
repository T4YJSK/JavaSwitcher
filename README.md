# Java Switcher

A lightweight Windows system tray utility designed for developers to quickly launch isolated command-line environments with different JDK versions—**without modifying global system environment variables**.

一个轻量级的 Windows 系统托盘工具，专门用于为开发者快速提供不同 Java 版本的独立命令行环境，**完全不影响和修改系统的全局环境变量**。

---

## 🚀 Features | 核心特性

- **Zero Global Pollution**: Modifies environment variables at the process level (`os.environ`). Your system's global `PATH` and `JAVA_HOME` remain perfectly clean.
- **Dynamic Refresh**: The tray menu scans the directory in real-time. Adding or renaming a JDK folder reflects instantly without restarting the app.
- **No File Littering**: Pure memory/process-level injection; no temporary `.bat` or `.cmd` files are created on your disk.
- **Portable**: Can be placed directly inside your Java tools directory.

---

## 🛠️ Prerequisites | 前置需求

Make sure you have Python 3.x installed along with the required dependencies:

```bash
pip install pystray Pillow
```

## 📸 Preview

Example tray menu:

<img width="175" height="156" alt="image" src="https://github.com/user-attachments/assets/2b1f2e97-db17-48ba-9b54-099c4363f5ee" />



---

## 📦 Directory Setup & Configuration | 目录配置

By default, the script scans directories in two priorities:
1. **Current Directory**: The same folder where this script resides.
2. **Fallback Directory**: `E:\Java` (You can change `DEFAULT_JAVA_BASE` in the script to match your setup).

### Directory Example | 目录结构示例:
Ensure your JDK folders contain the standard `bin\java.exe` structure. The folder names will be directly displayed in the tray menu.
确保你的 JDK 文件夹包含标准的 `bin\java.exe` 路径。文件夹的名称会直接作为托盘菜单的选项显示：

```text
E:\Java\
├── JDK 8\          --> Will show as "JDK 8" in menu
│   └── bin\java.exe
├── OpenJDK 17\     --> Will show as "OpenJDK 17" in menu
│   └── bin\java.exe
└── GraalVM 21\     --> Will show as "GraalVM 21" in menu
    └── bin\java.exe
```

## 📁Modify the actual folder
<img width="936" height="167" alt="image" src="https://github.com/user-attachments/assets/3464f7ea-f5a5-40dd-9298-2995404f1aeb" />


---

### 💻 使用方法部分 (Usage)

```base
1. Run the script | 运行脚本:
   python main.py
```

## ⚙ How it works
Scans JDK directory
Builds tray menu dynamically
Launches CMD with JAVA_HOME set temporarily

## ❗ Notes

Windows only
Requires correct JDK folder structure
No system modification (safe)
