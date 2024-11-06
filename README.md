# Project: Child Development Assessment Tool

We created a Python program that acts as an evaluation and monitoring tool for child development. This advanced tool would use different modules and techniques to simulate a system that allows evaluating key areas of a child's development (cognitive, social, emotional, and physical). This program will include advanced object-oriented programming concepts such as inheritance, polymorphism, generators, decorators, and magic methods.

## Objective

This program will help psychologists or educators track child development in different areas, providing an interface to aggregate and evaluate different types of information about the child. You will use an object-oriented approach to represent different areas of development.


## Structure of the Project

* **Evaluation.py**: Classes to model the areas of development (Cognitive, Social, Emotional and Physical).
* **DevelopmentReport.py**: Class to manage the creation of reports and generate development summaries.
* **Decorators.py**: Decorators to add functionality, such as measuring execution times and validating data.
* **DataHandler.py**: Class to manage data storage and access.
* **Main.py**: Main program that allows the user to interact with the classes and functionalities of the system.


## Explanation of the Project

1. **Evaluation Classes**: These represent different areas of child development, each implementing the evaluate method, which provides a specific assessment. They use inheritance to share the common structure from DevelopmentArea.
1. **Decorators**:
* `validate_score`: Ensures that scores are within the range 0-100.
* `measure_time`: Measures how long each evaluation takes.
1. **Development Report**: `DevelopmentReport` uses generators to create a detailed report and a general summary of the child’s development.
1. **Data Management**: `DataHandler` is a context manager that manages file operations to store the development report.
1. **Main Program**: `Main.py` allows the user to enter scores, create evaluations for each area, generate a detailed report, and save it to a file.

This project showcases advanced Python techniques and serves as an educational tool for child development psychology.