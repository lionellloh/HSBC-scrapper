# TODO: output.csv should have column names
# TODO: arg flags for different starting state to support "threading"
# TODO: readme.md for reference
# TODO: reduce redundant time.sleeps
# TODO: Time measurements
# TODO: Phantom JS switch



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

browser = webdriver.Chrome(executable_path='/Users/new/Downloads/chromedriver_new')

def write_to_csv(x, filename = "output.csv"):
    if x == ['Address:\nValuation HKD\nGross floor area (sq ft)\nSaleable area (sq ft)\nProperty age (year/s)\nValuation date']:
        return
    print("Writing")
    x = x[0].split('\n')
    print(x[0])
    x[0] = x[0].split(": ")[1]
    x = [x[i] for i in range(0, len(x),2)]
    for i in range(1,5):
        x[i] = float("".join(x[i].split(",")))

    print(x)
    print(len(x))

    with open(filename,'a') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerow(x)

def start():
    for button in range(6):

        browser.find_element_by_id("arrowid_hdx_dijits_form_Select_{}".format(button)).click()

        print("{}".format(button))

        actions = ActionChains(browser)
        actions.send_keys(u'\ue015')
        actions.send_keys(u'\ue007')
        actions.perform()

        print("{} pressed".format(button))

        time.sleep(1)

    browser.find_element_by_id("btnPropertyEvaluation").click()

def field_iter(i):

    old_text = "old"
    current_text = "current"
    while old_text != current_text:
        browser.find_element_by_id("arrowid_hdx_dijits_form_Select_{}".format(i)).click()

        actions = ActionChains(browser)


        actions.send_keys(u'\ue015')
        # Enter
        actions.send_keys(u'\ue007')

        actions.perform()

        time.sleep(1)

        if i+1 <= 5:
            field_iter(i+1)

        else:
            pass

        old_text = current_text
        current_text = browser.find_elements_by_xpath('//*[@id="hdx_dijits_form_Select_{}_Text"]'.format(i))[0].text
        print("Old Text:", old_text)
        print("Current Text:", current_text)
        time.sleep(1)

        browser.find_element_by_id("btnPropertyEvaluation").click()
        time.sleep(1)

        elems = browser.find_elements_by_class_name('propvaluationresult')
        elems_text = [e.text for e in elems]
        write_to_csv(elems_text)

    return ("End loop")


def one_field_iter(i):

    old_text = "old"
    current_text = "current"

    browser.find_element_by_id("arrowid_hdx_dijits_form_Select_{}".format(i)).click()

    actions = ActionChains(browser)


    actions.send_keys(u'\ue015')
        # Enter
    actions.send_keys(u'\ue007')

# Open the browser
browser.get("https://www.hsbc.com.hk/personal/mortgages/property-valuation-tool.html")

# start()
# elems = browser.find_elements_by_class_name('propvaluationresult')
# for elem in elems:
#     print (elem.text)


for i in range(5, -1, -1):

    print("i is ", i)
    print("Button {}".format(i))
    start_text = browser.find_elements_by_xpath('//*[@id="hdx_dijits_form_Select_{}_Text"]'.format(i))[0].text



    field_iter(0)


