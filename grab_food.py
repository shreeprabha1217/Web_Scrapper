import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import gzip
import threading
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GrabFoodScraper:
    def __init__(self, locations):
        self.locations = locations
        self.restaurants = []
        self.lock = threading.Lock()

    def setup_driver(self):
        try:
            options = webdriver.ChromeOptions()
            #options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
            options.add_argument('--window-size=1920,1080')  # Set window size to avoid issues with rendering
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        except Exception as e:
            logging.error(f"Error setting up driver: {e}")
            return None

    def scrape_location(self, location):
        driver = self.setup_driver()
        if not driver:
            return

        try:
            logging.info(f"Scraping location: {location}")
            driver.get("https://food.grab.com/sg/en")
            time.sleep(2)
            
            # Find and enter the location into the search input
            search_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "location-input"))
            )
            search_input.send_keys(location)
            
            # Find and click the search button
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submitBtn___2roqB"))
            )
            search_button.click()
            time.sleep(10)
            
            # Parse the HTML source of the page
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            #parent_element = soup.find('div', class_='wrapper___2mfzz ant-layout')
            # Find all restaurant cards
            restaurant_cards = soup.find_all('div', class_='swiper-slide slide___q2S4n')

            # Extract information from each restaurant card
            for card in restaurant_cards:
                try:
                    name = card.find('p', class_='name___2epcT').text
                    cuisine = card.find('div', class_='basicInfoRow___UZM8d cuisine___T2tCh').text
                    rating = card.find('div', class_='numbersChild___2qKMV').text
                    delivery_time = card.find('div', class_='numbersChild___2qKMV').text
                    promo = card.find('div', class_='promoTagHead___1bjRG')
                    promo_text = promo.text if promo else None
                    image = card.find('img', class_='realImage___2TyNE show___3oA6B')['src']
                    lat, lon = self.extract_lat_lon(card)

                    # Append restaurant details to the list
                    with self.lock:
                        self.restaurants.append({
                            'name': name,
                            'cuisine': cuisine,
                            'rating': rating,
                            'delivery_time': delivery_time,
                            'promo_text': promo_text,
                            'image': image,
                            'lat': lat,
                            'lon': lon,
                        })
                except Exception as e:
                    logging.error(f"Error extracting restaurant details: {e}")
        except Exception as e:
            logging.error(f"Error during scraping location '{location}': {e}")
        finally:
            driver.quit()

    def extract_lat_lon(self, card):
        try:
            # Custom extraction logic for lat and lon
            return "lat", "lon"
        except Exception as e:
            logging.error(f"Error extracting lat/lon: {e}")
            return None, None

    def save_data(self, filename='restaurants.ndjson.gz'):
        try:
            # Save the extracted data to a gzip-compressed ndjson file
            with gzip.open(filename, 'wt', encoding='utf-8') as f:
                for restaurant in self.restaurants:
                    f.write(json.dumps(restaurant) + '\n')
            logging.info(f"Data saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving data: {e}")

    def run(self):
        threads = []
        # Start a separate thread for each location
        for location in self.locations:
            thread = threading.Thread(target=self.scrape_location, args=(location,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        # Save the extracted data
        self.save_data()

if __name__ == '__main__':
    locations = [
         #'PT Singapore - Choa Chu Kang North 6, Singapore, 689577',
         'Chong Boon Dental Surgery - Block 456 Ang Mo Kio Avenue 10, #01-1574, Singapore, 560456'
    ]
    scraper = GrabFoodScraper(locations)
    scraper.run()
