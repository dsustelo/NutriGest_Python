# NutriGest

**NutriGest** is a Python-based program built with Python/Tkinter that allows users to create customized dishes while calculating their nutritional values in real time. The program provides an easy-to-use graphical user interface (GUI) where users can input ingredients and quantities, view nutritional information, and print from a template.

## Features

- **Ingredient Input**: Add ingredients to your dish using text boxes with auto-complete functionality.
- **Real-time Nutritional Calculation**: As ingredients and quantities are added, the program automatically calculates the nutritional values (e.g., calories, proteins, fats, etc.).
- **Excel Report Generation**: Print the entered information in a predefined Excel template for easy record-keeping.
- **Auto-adjusting Rows**: The program automatically adds or removes rows for ingredients based on user input, ensuring that the ingredient list remains organized.
- **Input Validation**: The program ensures that only valid numbers and decimal points can be entered for ingredient quantities.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/dsustelo/NutriGest_Python.git
    cd NutriGest_Python
    ```

2. **Install the required dependencies**:

    Make sure you have Python 3.x installed. You can install the required packages using pip:

    ```bash
    pip install openpyxl tkinter
    ```

## Usage

1. **Run the program**:

    You can run the program by executing the following command:

    ```bash
    python main.py
    ```

2. **Input Ingredients**:
    - In the "Ingredients" section, type the name of the ingredient. The program will automatically suggest matching ingredients from the database.
    - Double-click the suggested ingredient to add it to the dish.
    - Enter the quantity of each ingredient in grams.

3. **View Nutritional Values**:
    - The nutritional values will be calculated and displayed in the "Nutritional Values" section as you add ingredients.

4. **Print**:
    - At any time, click the button to print.

## How It Works

- The program imports nutritional values and ingredient names from an Excel file into a Python dictionary for quick lookup.
- Users type the ingredient name, and the program matches it with the dictionary. When a match is found, the ingredient is added to the dish.
- Nutritional calculations are done in real-time as ingredients and quantities are entered.

## Requirements

- Python 3.x
- Tkinter
- Openpyxl (for Excel integration)
