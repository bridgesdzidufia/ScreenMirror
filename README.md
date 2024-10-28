Android Mirror Script

This project provides a simple Python automation script to mirror your Android phone’s screen to your Ubuntu PC using scrcpy. 
It allows you to launch screen mirroring directly from the terminal and even automate the process when the phone is connected via USB.

Features

    Automatically detect connected Android devices.
    Launch scrcpy to mirror the phone screen via USB.
    No need to open Visual Studio Code – run the script directly from the terminal.
    Option to automatically start the mirroring using udev rules.

Prerequisites

    1. Android Phone Setup:
        Enable Developer Options:
        Go to Settings → About Phone → Tap Build number 7 times.
        Enable USB Debugging:
        Go to Settings → System → Developer Options → Enable USB Debugging.

    2. Install scrcpy on Ubuntu:
    sudo apt update
    sudo apt install scrcpy adb

    3. Connect your Android device via USB.

    How to Use
1. Run Manually from the Terminal

    Clone this repository:
   git clone https://github.com/bridgesdzidufia/ScreenMirror.git
cd ScreenMirror

2. Make the script executable:
chmod +x mirror.py

3. Run the script:
./mirror.py

Troubleshooting

    If the phone is not detected:
adb kill-server
adb start-server
adb devices

    Ensure scrcpy is installed properly:
scrcpy --version

Contributing
Feel free to open issues or submit pull requests if you encounter bugs or have feature suggestions.

License
This project is licensed under the MIT License – see the LICENSE file for details.

Acknowledgments

    scrcpy – A powerful open-source screen mirroring tool.
    Android Developers Documentation – For enabling Developer Options and USB Debugging.
