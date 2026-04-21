# SRT Subtitle Translator

## Installation Instructions
1. **Clone the repository**:
   ```
   git clone https://github.com/Unavai95/TT.git
   cd TT
   ```

2. **Install dependencies**:
   Ensure you have Python installed (3.6 or higher). Then, run:
   ```
   pip install -r requirements.txt
   ```

## Setup Guide
1. **Configure settings**:
   Edit the `config.json` file to set your preferred language translations and other settings.

2. **Prepare your SRT files**:
   Place your SRT files in the `srt_files/` directory.

## Usage Instructions
1. **Run the application**:
   Execute the following command in your terminal:
   ```
   python translate.py
   ```

2. **Choose the desired options** from the menu to translate your subtitles.

3. **Output**:
   Translated SRT files will be saved in the `output/` directory.

## Features
- Support for multiple languages
- Fast and efficient translation
- User-friendly command-line interface
- Ability to process multiple SRT files at once

## Troubleshooting
- **Issue**: Application does not start.
  - **Solution**: Ensure that all dependencies are installed and you are using the correct Python version.

- **Issue**: Translated subtitles are incorrect.
  - **Solution**: Double-check your `config.json` settings. Ensure that the source subtitles are clear and correctly formatted.

- **Issue**: Unable to find output files.
  - **Solution**: Verify that the translation command was successful and check the `output/` directory for files.

## Contributing
If you would like to contribute to the SRT Subtitle Translator, feel free to open a pull request or issue.