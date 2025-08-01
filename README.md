# ExcelAutoSum

A simple Python tool for automating Excel file processing: grouping, summing, and generating bar charts.

## 🚀 Features

- Automatically processes all `.xlsx` files in the current folder that match the column structure of `config.json`
- Groups and sums data by user-defined columns
- Saves the grouped results into new Excel files
- Generates bar charts on a separate worksheet using `openpyxl`
- Interactive CLI with default values

## 🗂 Project Structure

project/
├── main.py # Main script to run the automation
├── excel_tren.py # WorkwithFiles class: handles grouping and file operations
├── math_class.py # DiagrammDraw class: generates charts using openpyxl
├── config.json # Reference structure for validating Excel files
├── .gitignore
└── README.md

markdown
Копировать
Редактировать

## 🛠 Requirements

- Python 3.8+
- pandas
- openpyxl

Install dependencies:

```bash
pip install -r requirements.txt
⚙️ Usage
Place your .xlsx files and config.json in the project directory.

Run the script:

bash
Копировать
Редактировать
python main.py
When prompted:

Enter the column name to group by (e.g. Category)

Enter the column name to sum (e.g. Amount)

Optionally enter custom names for each output file and data sheet

The script will:

Validate the structure of each .xlsx file

Group and sum the data

Create a new Excel file for each summary

Add a bar chart to a new sheet in each file

📌 Example
If your Excel files contain:

Category	Amount
Food	100
Travel	50
Food	80

You will get a new .xlsx file with:

Category	Amount
Food	180
Travel	50

...and a bar chart on the Диаграмма sheet.
