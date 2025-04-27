Eurasian Times Web Scraper
Name: Program to scrape headlines and article content from Eurasian TimesAuthor: Suman GangopadhyayDate: 27-April-2025Description: This program scrapes headlines and article content from the Eurasian Times website.Email: linuxgurusuman@gmail.com  
This is a Python-based web scraping application that uses Selenium to extract headlines and article content from https://www.eurasiantimes.com/. The project is structured using Object-Oriented Programming (OOP) principles, with separate classes for data, locators, and automation logic.
Features

Scrapes the latest headlines and their URLs from the Eurasian Times website.
Saves headlines and URLs to a CSV file (eurasiantimes_headlines.csv).
Scrapes the main content of each article and saves it to individual text files in an article_contents directory.
Uses modular OOP design with Data, Locator, and AutomationClass classes.
Handles errors gracefully and runs in headless mode for efficiency.

Prerequisites

Python 3.6 or higher
Google Chrome browser (for Selenium WebDriver)
Required Python packages:
selenium
webdriver-manager



Installation

Clone the repository (or download the script):
git clone <repository-url>
cd <repository-directory>


Install dependencies:
pip install selenium webdriver-manager



Usage

Save the script:

Ensure the main script (web_scraper_oop.py) is in your working directory.


Run the script:
python web_scraper_oop.py


Output:

A CSV file named eurasiantimes_headlines.csv will be created with columns Headline and URL.
A directory named article_contents will be created, containing text files named after sanitized headlines (e.g., China_Unveils_New_Stealth_Fighter_Jet.txt). Each text file includes the headline, URL, and article content.



Project Structure

web_scraper_oop.py: Main script containing the OOP-based web scraper.
eurasiantimes_headlines.csv: Output CSV file with headlines and URLs.
article_contents/: Directory containing text files with article content.
README.md: This file.

Classes

Data: Stores application-wide data (e.g., website URL, file paths, encoding).
Locator: Holds Selenium CSS selectors for headlines and article content.
AutomationClass: Inherits from Data and Locator, handles scraping logic, and saves output.

Notes

CSS Selectors: The selectors (h2.entry-title a, h3.entry-title a, a.post-title for headlines; div.entry-content, article, div.post-content for content) are placeholders. Inspect the website's HTML using browser DevTools to confirm the correct selectors and update the Locator class if needed.
Headless Mode: The script runs in headless mode. To see the browser, remove the --headless argument in the AutomationClass initialization.
Error Handling: The script includes robust error handling for network issues, file operations, and incorrect selectors.
File Overwrite: Existing CSV and text files are overwritten. Modify file paths or add append logic to avoid this.
Website Changes: If the website's structure changes, update the CSS selectors in the Locator class.

Troubleshooting

No headlines/content scraped: Inspect the website's HTML and update the CSS selectors in the Locator class.
Selenium errors: Ensure Chrome and ChromeDriver are compatible. The webdriver-manager package handles this automatically in most cases.
File not found: Ensure the script is run in the correct directory where web_scraper_oop.py is located.

License
This project is licensed under the MIT License.
Contact
For issues or suggestions, please contact the author at linuxgurusuman@gmail.com or open an issue on the repository.
