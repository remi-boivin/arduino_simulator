# Arduino Simulator
![GitHub License](https://img.shields.io/github/license/remi-boivin/arduino_simulator?style=for-the-badge)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/remi-boivin/arduino_simulator?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/remi-boivin/arduino_simulator?style=for-the-badge)
![Codecov](https://img.shields.io/codecov/c/github/remi-boivin/arduino_simulator?style=for-the-badge)



This repository contains an arduino simulator in Python.

## Table of Contents

- [Getting started](#getting-started)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this simulator:

1. Clone the repository: `git clone https://github.com/remi-boivin/arduino_simulator`
2. Navigate to the repository folder: `cd arduino_simulator`
3. Install required dependencies: `pipenv install`
4. Install gitmogi, husky and commitlint
    ```sh
    npm install husky @commitlint/cli @commitlint/config-conventional commitlint-config-gitmoji
    npm install -g gitmoji    
    ```
4. Configure tools
    ```sh
    gitmoji init
    npx husky install
    npx husky add .husky/commit-msg 'npx --no-install commitlint --edit $1'
    echo "module.exports = {extends: ['gitmoji']};" > commitlint.config.js
    ```
## Roadmap
### Version 1.0.0 (Upcoming Release)

- [ ] **Basic Simulation Components:**
  - Implement the simulation logic for fundamental electronic components (e.g., resistors, capacitors, inductors).
  - Ensure accurate modeling of electrical characteristics and interactions.
  
- [ ] **Component Library:**
  - Develop a diverse library of electronic components.
  - Allow users to easily select and add components to their circuits from the library.

- [ ] **Error Handling and Diagnostics:**
  - Implement robust error-handling mechanisms.
  - Provide clear error messages and diagnostics to assist users in identifying and resolving issues within their circuits.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. checkout develop (git checkout develop)
3. Create your Feature Branch (git checkout -b feature/AmazingFeature)
4. Commit your Changes (git commit -m 'Add some AmazingFeature')
5. Push to the Branch (git push origin feature/AmazingFeature)
6. Open a Pull Request

For more information please read [CONTRIBUTING.md](CONTRIBUTING.md)

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details.
