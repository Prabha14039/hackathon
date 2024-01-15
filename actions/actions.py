# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService  # Use EdgeService for Edge
from selenium.webdriver.edge.options import Options as EdgeOptions  # Use EdgeOptions for Edge
import selenium.webdriver as webdriver
import time

class ActionPerformWebAutomation(Action):
    def name(self) -> Text:
        return "action_perform_web_automation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Initialize Edge service
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/120.0.0.0'
        driver_path = r"C:\Users\sharm\Desktop\dummy\msedgedriver.exe"
        edge_service = EdgeService(driver_path)
        edge_options = EdgeOptions()
        edge_options.add_argument(f'user-agent={user_agent}')

        # Create an Edge WebDriver instance with specified options
        browser = webdriver.Edge(service=edge_service, options=edge_options)

        try:
            # Navigate to the website
            browser.get('https://bhuvan-app3.nrsc.gov.in/aadhaar/')

            # Wait for the button to be clickable
            search_button = WebDriverWait(browser, 7).until(
                EC.element_to_be_clickable((By.ID, 'locate'))
            )

            # Click on the button using JavaScript
            browser.execute_script("arguments[0].click();", search_button)

            # Wait for 60 seconds (you may adjust this based on your needs)
            time.sleep(20)

        finally:
            # Close the browser window
            browser.quit()

        return []
