# Break Reminder App

The Break Reminder App is a simple Tkinter-based application designed to help users give their eyes regular breaks during work or study sessions. The app allows you to set a time interval before receiving a reminder to take a break, and it also includes a full-screen popup to remind you to look away and rest your eyes.

### TOC
## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [With requirements.txt](#with-requirementstxt)
  - [Piece by Piece](#piece-by-piece)
- [How to Use](#how-to-use)
- [Configuration](#configuration)
  - [Time](#time)
  - [Audio](#audio)
- [License](#license)

## Features
- **Timer for Break Reminders**: Set a time interval (in minutes) to receive a break reminder.
- **Break Popup**: A full-screen popup shows up when it's time for a break, with a countdown timer to indicate how much break time is left.
- **Break Sound**: A nice chime will play when a break ends to avoid the need of peaking at the screen.
- **Start/Stop Controls**: Start or stop the reminder cycle with buttons in the main window.
- **Escape Key to Close Popup**: Dismiss the popup without stopping the cycle anytime by pressing the `esc` key.
- **Configuration File**: Times and sounds can be configured in the [config.cfg](config.cfg) file.

## Requirements - [file](requirements.txt)
- Python 3.11.4
- Tkinter (usually comes with Python by default)
- Playsound 1.3.0

## Installation
### With requirements.txt
```bash
pip install -r requirements.txt
```

### Piece by Piece
1. Ensure you have Python 3.11.4 installed.
2. Tkinter should be installed by default. If it's not, you can install it with:
    ```bash
    pip install tk
    ```
3. Install the Playsound library:
    ```bash
    pip install playsound
    ```

## How to Use
1. Run the application by with the following:
    ```bash
    python main.py
    ```
2. When the main window appears press the `Start` button. This will begin the countdown timer.
3. When the timer reaches 0 a fullscreen pop-up will appear with another countdown reminding you to give your eyes a break.
4. The pop-up will automatically close and play a chime, after which a new countdown will begin. Alternatively the popup can be dismissed using the `esc` key (Will not stop the cycle).
5. Use the `Stop` button or close the application to end the cycle.

## Configuration - [file](config.cfg)
The application uses a `.cfg` file to manage settings, allowing users to easily customize behavior without modifying the source code. If the file doesn't exist or an error occurs while reading the file, a new file will be generated.

### Time
- **`time_between_breaks_in_minutes`**: The time in minutes between breaks. This can be a decimal. Default: `20`.
- **`duration_of_breaks_in_seconds`**: The duration in seconds that breaks will last. This must be an integer. Default: `20`.

### Audio
- **`sound_file`**: The relative path to the sound file that will play at the end of breaks. Default: `./Assets/chime.mp3`

## License 
[MIT License](LICENSE)