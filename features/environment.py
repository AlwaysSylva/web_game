from splinter.browser import Browser

def before_all(context):
    driver = context.config.userdata.get("browser", "phantomjs")
    context.browser = Browser(driver)

def after_all(context):
    context.browser.quit()
    context.browser = None