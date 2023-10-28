from playwright.sync_api import sync_playwright


with sync_playwright() as play:
    browser = play.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.youtube.com/@pdpuz/videos')
    data = page.query_selector_all('#video-title')

    for i in data[:5]:
        print(i.text_content())


    page.wait_for_timeout(10000)























