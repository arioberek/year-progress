# Year Progress Tracker

This Python application tracks the year's progress and shares a visual progress bar on Instagram. It automatically generates a progress bar image, logs into an Instagram account, and posts the progress image with a caption indicating the percentage of the year completed.

## Features

- Calculates the current year's progress as a percentage.
- Generates a visual representation of the year's progress in the form of a progress bar.
- Logs into an Instagram account using credentials.
- Uploads the generated progress image to Instagram with a caption.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system.
- Instagram account credentials for posting images.
- Required Python packages: install them using `pip install -r requirements.txt`.

## Installation

1. Clone the repository to your local machine.
2. Install the required Python packages using the following command:
   ```
   pip install -r requirements.txt
   ```
3. Configure your Instagram account credentials. (See Configuration section)

## Configuration

To use this application, you need to provide your Instagram login credentials. This can be done by setting environment variables or modifying the `ig_login.py` script directly (not recommended for security reasons).

## Usage

To run the application, execute the following command in your terminal:

```
python main.py
```

This will automatically calculate the year's progress, generate a progress bar image, and post it to your Instagram account.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.
