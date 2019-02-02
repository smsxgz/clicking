clicking

基于PyUserInput, 适用于Ubuntu系统的简单的鼠标连点器！

Usage:
1. For Ubuntu, just run it by
```bash
python clicking.py
```
and use key 'F8' to start and 'F9' to stop.

2. For Android, follow the steps below.
    1. Install adb tools, link to your phone, and check by
    ```bash
    adb devices
    ```
    2. Get resolution of the screen of your phone.
    ```bash
    adb shell getevent -p | grep -e "0035" -e "0036"
    ```
    3. Get the tap position.
    ```bash
    adb shell getevent | grep -e "0035" -e "0036"
    ```
    4. At last, run it by
    ```bash
    python clicking.android.py
    ```
