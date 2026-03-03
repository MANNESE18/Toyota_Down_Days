# Stock Description Fetcher

Allows users to quickly pull official company descriptions and business overviews directly into their terminal.

## Features

* **Simple Interface:** Interactive CLI that prompts for ticker and API key.
* **Real-time Data:** Leverages the Alpha Vantage API for up-to-date information.
* **Error Handling:** Includes a try-except block to catch invalid ticker inputs and prevent script crashes.
  
## Built With

* **Python 3.x:** Core Programming Language
* **Alpha Vantage API:** Used for fetching "Overview" stock metadata
* **Requests Library:** An external library used to send HTTP requests to the Alpha Vantage API.
* **JSON Module:** A built-in Python module used to parse the data returned by the API.

## Usage

**1) Prerequisites**

Before running the script, ensure you have the requests library installed:
```
pip install requests
```

**2) Get your API Key**

You will need a free API key from Alpha Vantage. You can get it here -> https://www.alphavantage.co/support/

This script operates as an interactive command-line tool. To use it, follow the steps below:

**3) Run the script**

Open your terminal or command prompt, navigate to the project folder and execute the file:
```
python TSLA_Overview.py
```

**4) Enter Data and Credentials**


This script will pause and promt you for two specific pieces of information:

**stock ticker:** enter the symbol for the company you want to research (ex. MSFT for Microsoft)
**API Key:** Paste your unique Alpha Vantage API Key. You can get one here -> https://www.alphavantage.co/support/

**5) Example Workflow**

```
Stock Ticker or Type 'quit' to exit: TSLA
Enter API Key: YOUR_API_KEY_HERE
Description: Tesla, Inc. is an American electric vehicle and clean energy company...
```

**6) Handling Errors**

The script includes build-in error handling to manage common issues:

**Invalid Tickers:** If you enter a symbol that does not exist or is misspelled, the console will display Invalid Ticker instead of crashing.
**Exiting:** To close the program at any time during the ticker prompt, simply type "quit".

**7) API Limits**

Since this script fetches data in real-time, ensure you stay within the Alpha Vantage free-tier limits (typically 25 requests per day). If you exceed this limit, the "Description" may return as empty or show an API warning.
