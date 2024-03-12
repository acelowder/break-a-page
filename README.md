# Break-a-Page

Break-a-Page is a Python-based stress testing tool built on top of Selenium WebDriver. It allows users to stress test web applications by simulating user interactions such as clicking buttons, filling forms, and navigating through links.
![Demo](https://media.giphy.com/media/Qx2suERgvb598BBtEv/giphy.gif)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Stress test web applications by simulating user interactions.
- Test various elements including buttons, input fields, and links.
- Generate test reports with detailed results.
- Easy to use command-line interface.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/break-a-page.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```


3. Download the Chrome WebDriver compatible with your version of Chromium:
- Visit the [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) page.
- Download the appropriate version for your operating system.

4. Add the Chrome WebDriver to your system's PATH:
- Extract the downloaded Chrome WebDriver archive.
- Move the `chromedriver` executable to a directory included in your system's PATH.

5. Ensure you have Google Chrome installed:
- For Windows and macOS: Ensure you have Google Chrome installed on your system.
- For Linux: You can install Chromium using your package manager. For example, on Debian-based systems, you can use the command:
  ```
  sudo apt install chromium-browser
  ```

## Usage

1. Navigate to the project directory:
   ```
   cd break-a-page
   ```

2. Run the main script:
   ```
   python main.py
   ```

3. Follow the prompts to specify the URL of the web application to be tested and choose testing options.

## Contributing

Feel free to contribute to Break-a-Page! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions, feedback, or support, please contact me at [ace.lowder@gmail.com](mailto:ace.lowder@gmail.com).
