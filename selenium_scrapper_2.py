# browser = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
browser = webdriver.Chrome('/Users/new/Downloads/chromedriver_new')
browser.get("https://www.hsbc.com.hk/personal/mortgages/property-valuation-tool.html")

#browser.find_element_by_class(dijitReset dijitInline dijitSelectLabel dijitValidationTextBoxLabel)
#find a way to check if the button text is "Select"

for button in range(6):

    browser.find_element_by_id("arrowid_hdx_dijits_form_Select_{}".format(button)).click()

    print("{}".format(button))
    #while button text != “Select"

    actions = ActionChains(browser)
    actions.send_keys(u'\ue015')
    actions.send_keys(u'\ue007')
    actions.perform()

    print("{} pressed".format(button))

browser.find_element_by_link_text("Get property valuation")

# browser.find_element_by_id("arrowid_hdx_dijits_form_Select_1").click()
#
# actions = ActionChains(browser)
# actions.send_keys(u'\ue015')
# actions.send_keys(u'\ue007')
# actions.perform()

time.sleep(2)     #Explicit wait

browser.get_screenshot_as_file("image.png")

browser.close()
# browser = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
#
# browser.get("https://www.hsbc.com.hk/personal/mortgages/property-valuation-tool.html")

#browser.find_element_by_class(dijitReset dijitInline dijitSelectLabel dijitValidationTextBoxLabel)
#find a way to check if the button text is "Select"

for button in range(6):

    browser.find_element_by_id("arrowid_hdx_dijits_form_Select_{}".format(button)).click()

    print("{}".format(button))
    #while button text != “Select"

    actions = ActionChains(browser)
    actions.send_keys(u'\ue015')
    actions.send_keys(u'\ue007')
    actions.perform()

    print("{} pressed".format(button))

browser.find_element_by_link_text("Get property valuation")

# browser.find_element_by_id("arrowid_hdx_dijits_form_Select_1").click()
#
# actions = ActionChains(browser)
# actions.send_keys(u'\ue015')
# actions.send_keys(u'\ue007')
# actions.perform()

time.sleep(2)     #Explicit wait

browser.get_screenshot_as_file("image.png")

browser.close()
