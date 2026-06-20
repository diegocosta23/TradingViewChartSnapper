from playwright.sync_api import sync_playwright

from config import TRADINGVIEW_URL


class TradingViewBrowser:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.page = self.browser.new_page()

        self.page.goto(TRADINGVIEW_URL)

    def capture_all_timeframes(self, ticker):

        print("Searching:", ticker)

    def close(self):

        self.browser.close()

        self.playwright.stop()