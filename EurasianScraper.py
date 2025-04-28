"""
Name : Program to scrape headlines and article content from Eurasian Times
Author : Suman Gangopadhyay
Date : 27-April-2025
Description : This program scrapes headlines and article content from the Eurasian Times website.
Email : linuxgurusuman@gmail.com
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import os
import re

class Data:
    """Class to hold basic data for the application."""
    def __init__(self):
        self.website_url = "https://www.eurasiantimes.com/"
        self.csv_file = "eurasiantimes_headlines.csv"
        self.output_dir = "article_contents"
        self.encoding = "utf-8"

class Locator:
    """Class to hold all Selenium locators."""
    def __init__(self):
        self.headline_selector = "h2.entry-title a, h3.entry-title a, a.post-title"
        self.content_selector = "div.entry-content, article, div.post-content"
        self.fallback_content_selector = "div.entry-content p, article p"

class SumanNewsExtractor(Data, Locator):
    """Class to handle web scraping automation, inheriting Data and Locator."""
    def __init__(self):
        Data.__init__(self)
        Locator.__init__(self)
        # Set up Chrome options
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")  # Run in headless mode
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        # Initialize WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def sanitize_filename(self, filename):
        """Sanitize headline for valid filename."""
        return re.sub(r'[^\w\s-]', '', filename.replace(' ', '_')).strip()[:100]

    def scrape_headlines(self):
        """Scrape headlines and URLs, save to CSV."""
        try:
            print(f"Scraping headlines from {self.website_url}...")
            self.driver.get(self.website_url)
            
            # Find headline elements
            headline_elements = self.driver.find_elements(By.CSS_SELECTOR, self.headline_selector)
            
            # Prepare data for CSV
            headlines_data = []
            for headline in headline_elements:
                text = headline.text.strip()
                url = headline.get_attribute("href")
                if text and url:  # Ensure headline and URL are not empty
                    headlines_data.append({"Headline": text, "URL": url})
            
            # Write to CSV
            with open(self.csv_file, mode="w", newline="", encoding=self.encoding) as file:
                writer = csv.DictWriter(file, fieldnames=["Headline", "URL"])
                writer.writeheader()
                for data in headlines_data:
                    writer.writerow(data)
            
            print(f"Headlines saved to {self.csv_file}")
            return True
        
        except Exception as e:
            print(f"Error scraping headlines: {e}")
            return False

    def scrape_article_content(self):
        """Scrape content from URLs in CSV and save to text files."""
        try:
            print("\nScraping article content from URLs...")
            
            # Read the CSV file
            if not os.path.exists(self.csv_file):
                raise FileNotFoundError(f"{self.csv_file} not found. Run scrape_headlines first.")
            
            with open(self.csv_file, mode="r", encoding=self.encoding) as file:
                reader = csv.DictReader(file)
                articles = [(row["Headline"], row["URL"]) for row in reader]
            
            # Create output directory
            os.makedirs(self.output_dir, exist_ok=True)
            
            # Process each article
            for headline, url in articles:
                try:
                    # Navigate to the article URL
                    self.driver.get(url)
                    
                    # Find the main content
                    content_elements = self.driver.find_elements(By.CSS_SELECTOR, self.content_selector)
                    content = ""
                    for element in content_elements:
                        text = element.text.strip()
                        if text:
                            content += text + "\n\n"
                    
                    # Fallback to paragraphs if no content found
                    if not content:
                        paragraphs = self.driver.find_elements(By.CSS_SELECTOR, self.fallback_content_selector)
                        content = "\n".join(p.text.strip() for p in paragraphs if p.text.strip())
                    
                    # Sanitize headline for filename
                    filename = self.sanitize_filename(headline) + ".txt"
                    filepath = os.path.join(self.output_dir, filename)
                    
                    # Save content to text file
                    with open(filepath, mode="w", encoding=self.encoding) as f:
                        f.write(f"Headline: {headline}\nURL: {url}\n\n{content}")
                    
                    print(f"Saved content for '{headline}' to {filepath}")
                
                except Exception as e:
                    print(f"Error processing {url}: {e}")
        
        except Exception as e:
            print(f"Error scraping article content: {e}")

    def run(self):
        """Execute the full scraping process."""
        if self.scrape_headlines():
            self.scrape_article_content()

# Main execution function
if __name__ == "__main__":
    automation = SumanNewsExtractor()
    automation.run()
