import time
import csv


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

link = "https://www.hsbc.com.hk/personal/mortgages/property-valuation-tool.html"

driver = webdriver.Chrome('/Users/new/Downloads/chromedriver_new')
driver.get(link)

button_zone = ""
button_district = ""
button_estate = ""
button_block = ""
button_floor = ""
button_unit = ""

# driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_'
#
# """<td class="dijitReset dijitMenuItemLabel" colspan="2" data-dojo-attach-point=
# "containerNode" id="dijit_MenuItem_15_text">New Territories/Island</td>
#
# <td class="dijitReset dijitMenuItemLabel" colspan="2" data-dojo-attach-point=
# "containerNode" id="dijit_MenuItem_14_text">Kowloon</td>
#
# <td class="dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton
# dijitArrowButtonContainer" data-dojo-attach-point="titleNode" role="presentation"><label
# for="arrowid_hdx_dijits_form_Select_0" style="display:none;">!</label><input id="arrowid_hdx_dijits_form_Select_0" class="dijitReset dijitInputField dijitArrowButtonInner" value="▼
# " type="text" tabindex="-1" readonly="readonly" aria-hidden="true" role="presentation"></td>
# """


for i in range(1):
    print("Step: {}".format(i))
    base = "arrowid_hdx_dijits_form_Select_{}".format(i)
    element = driver.find_element_by_xpath('//*[@id="hdx_dijits_form_Select_0"]/tbody/tr/td[1]/div[1]/span')

    element2 = driver.find_element_by_xpath('//*[@id="hdx_dijits_form_Select_0"]/tbody/tr/td[1]/div[1]/span')
    element.click()
    actions = ActionChains(browser)
    actions.send_keys(u'\ue015')
    actions.send_keys(u'\ue007')
    actions.perform()
    # element2.click()
    # actions.send_keys(u'\ue015')
    # actions.send_keys(u'\ue007')

    # print(choices)

driver.close()
