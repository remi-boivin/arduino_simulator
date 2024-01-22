# Contributing to Kingdom intrigue

We welcome and appreciate your contributions to our project! Whether it's reporting bugs, suggesting enhancements, or adding new features, your input is valuable.

## How to Contribute

1. **Fork the Repository**: Create your own fork of the project on GitHub.
2. **Create a Feature Branch**: Make your changes in a new branch (`git checkout -b feature/YourAmazingFeature`).
3. **Commit Your Changes**: Commit your changes with clear, descriptive messages (`git commit -m 'Add some AmazingFeature'`).
4. **Push to the Branch**: Upload your changes to your fork (`git push origin feature/YourAmazingFeature`).
5. **Open a Pull Request**: Submit a pull request for your changes to be reviewed and merged into the main project.

Please ensure that your contributions adhere to the following guidelines and practices.

## Reporting Bugs

When reporting bugs, please include:

- A clear and descriptive title.
- Detailed steps to reproduce the bug.
- The expected behavior and what actually happened.
- Any relevant screenshots or error messages.

## Suggesting Enhancements

Enhancement suggestions are encouraged! Please include:

- A clear and concise description of what you want to happen.
- Any considerations or potential trade-offs.
- Additional context or screenshots if applicable.

## Code Contribution

### Godot Python Coding Style Guide

Adhering to a consistent coding style makes the project more maintainable and accessible to contributors. Here are our conventions for writing Python:

#### Naming Conventions

- **Classes**: PascalCase (e.g., `Core`, `SimulatorCore`).
- **Functions**: snake_case (e.g., `add_component`, `edit_component`).
- **Variables**: snake_case (e.g., `simulator_core`, `get_error`).
- **Constants**: ALL_CAPS (e.g., `SIMULATOR_TIME`, `MAX_SIMULATION`).
- **Signals**: snake_case starting with a verb (e.g., `simulation_started`, `burned_component`).

#### Indentation and Whitespace

- Use 4 spaces for indentation.
- Single empty line between methods, two before class definitions.
- Spaces around operators and after commas.

#### Commenting and Documentation

- Comments should explain why, not how.
- Document all classes and public methods with `##` or `"""`.


#### Control Structures

- Opening brace on the same line.
- Always use braces, even for single-line if statements or loops.

#### Avoiding Magic Numbers

- Use named constants for clarity.

```Python
const RESPAWN_TIME = 5
```

#### Error Checking

- Use assertions and explicit error checks where appropriate.
example
``` Python
assert(resistor > 0, "Speed must be positive")
```

## Conventional Commits

Implementing Conventional Commits in our project ensures a clear, consistent history in version control, facilitating better tracking, versioning, and release automation.

### Commit Message Structure
A Conventional Commit message comprises three parts: the header, body, and footer. The header includes a type, an optional scope, and a subject:
```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

#### Types

| Keyword      | Explanation                                                    |
|--------------|----------------------------------------------------------------|
|     feat     | Introduces a new feature to the user.                          |
|     fix      | Bug fix for the user.                                          |
|     docs     | Documentation updates.                                         |
|     style    | Code style changes (formatting, missing semi-colons, etc.).    |
|     refactor | Code refactoring without adding features or fixing bugs.       |
|     test     | Adding or refactoring tests, no production code change.        | 
|     chore    | Changes to the build process or auxiliary tools and libraries. |

#### Scope

The scope, which is optional, specifies the part of the system affected by the changes, such as npc, ai-system, or pathfinding.
Subject

The subject is a concise description of the change:

    Use the imperative mood, present tense: "add", not "added" nor "adds".
    Don't capitalize the first letter.
    No period (.) at the end.

#### Body

The body should explain the motivation for the change and contrast this with the previous behavior.
Footer

The footer is for noting any Breaking Changes and for referencing GitHub issues that the commit addresses.

Example

```
feat(simulator): add resistor simulation

This commit enhances the simulator module by adding resistor simulation capabilities. It extends Circuit and SimulatorCore classes,
introducing new methods in Component and CircuitImpl for handling resistor-specific functionalities.

This feature expands the simulator's ability to model electronic components, providing a more comprehensive circuit simulation experience.



Closes #123 # github issue id
```

## Pull Requests

- Provide a clear description of the changes.
- Include any relevant issue numbers.
- Ensure that your code adheres to the project's coding style.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (usually MIT).

## Contact

If you have any questions or need further clarification, feel free to reach out.

- Your Name - [remi-boivin](mailto:remi.boivin@epitech.eu)

Project Link: [arduino_simulator](https://github.com/remi-boivin/arduino_simulator)

Thank you for contributing to arduino_simulator !