# Finding Worst Performing Days of Toyota Stock

This project is a data pipeline designed to extract, transform, and load Toyota's historical stock data. I built this to demonstrate how to bridge raw file parsing with structured SQL storage to gain specific financial insights.

## Technical Requirements & Logic

* **Python 3.x:** Leveraged for its robust string manipulation and file I/O capabilities.
* **SQL Integration:** Integrated to provide a lightweight, serverless database for high-performance sorting and querying.
* **Error Handling:** I implemented specific logic to bypass headers and empty lines, ensuring the script doesn't crash on inconsistent CSV data.
* **Data Schema Knowledge:** I designed the `Down_Days` table with specific data types (REAL, INTEGER, DATE) to ensure mathematical accuracy for percentage calculations.

## Key Achievements in this Code
* **Custom Calculations:** I wrote the logic to isolate "down days" where the close price is lower than the open.
* **Dynamic Querying:** I used SQL ORDER BY and LIMIT clauses to programmatically identify the 20 most volatile days rather than sorting them manually in Python.
* **Formatted UI:** I used f-string alignment to create a clean, professional-looking data table in the console output.
