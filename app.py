from modules.browser import TradingViewBrowser


def main():

    ticker = input("Ticker: ")

    browser = TradingViewBrowser()

    browser.start()

    browser.capture_all_timeframes(ticker)

    browser.close()


if __name__ == "__main__":
    main()