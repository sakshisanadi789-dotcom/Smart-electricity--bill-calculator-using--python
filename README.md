# Smart Electricity Bill Calculator

## Project Overview
This is a beginner-friendly Python console program that calculates an electricity bill using user input, simple validation, and price slabs. It does not use any database, files, APIs, external libraries, or classes.

## How to Run the Program
1. Make sure Python is installed on your computer.
2. Open the project folder.
3. Run the program from the terminal:
   ```bash
   python main.py
   ```

## Program Flow
1. **Get Customer Details**
   - The program asks for the customer name.
   - It asks for the customer ID.
   - It asks for the total electricity units consumed.
   - If the user enters a negative number, the program shows an error and asks again.

2. **Calculate the Bill**
   - The bill is calculated using these slabs:
     - 0 to 100 units: Rs. 2 per unit
     - 101 to 200 units: Rs. 4 per unit
     - 201 to 500 units: Rs. 6 per unit
     - Above 500 units: Rs. 8 per unit
   - A fixed service charge of Rs. 100 is added.
   - The final bill amount is calculated as:
     - total bill = energy charge + service charge

3. **Display the Bill**
   - The program prints a clean bill with:
     - customer name
     - customer ID
     - units consumed
     - energy charge
     - service charge
     - final amount

## Beginner Concepts Used
- variables
- strings
- integers and floats
- functions and parameters
- return values
- input and type conversion
- comparison operators
- if, elif, and else statements
- formatted output

## Features
- simple console interface
- input validation for negative units
- easy-to-read bill layout
- no external dependencies

## Notes
This program is intended for learning and practice. It is a basic console-based calculator and helps beginners understand how Python can be used to solve a real-world problem.