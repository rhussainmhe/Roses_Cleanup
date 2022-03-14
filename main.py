import requests
from requests_html import HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import os
import roses

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options, executable_path='/Users/riaz_hussain/Downloads/chromedriver')

class fixer:
    def search_roses_name(self):
        connected_url = 'https://connected.mcgraw-hill.com/connected/login.do'
        connected_search_url = 'https://connected.mcgraw-hill.com/connected/support.accountSearch.do?accountName=&oksAccountId='
        rows=[]
        self.true_roses_name = []

        #Open CSV and read oracle number
        with open("/Users/riaz_hussain/Downloads/testingtesting.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)

            #Move all csv row values to rows varbiable
            for row in csvreader:
                rows.append(row)

            for oracle_ids in rows:
                #login to connected
                driver.get(connected_url)
                connected_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
                connected_html_str = connected_body_el.get_attribute("innerHTML")

                connected_html_obj = HTML(html=connected_html_str)
                time.sleep(2)

                #input connected user pass
                driver.find_element(By.NAME, "loginUserName").send_keys(roses.u)
                driver.find_element(By.NAME, "loginPassword").send_keys(roses.cep + Keys.ENTER)
                time.sleep(2)


                try:
                    driver.get(connected_search_url + oracle_ids[1])
                    print(connected_search_url + oracle_ids[1])
                    time.sleep(2)
                    connected_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
                    connected_html_str = connected_body_el.get_attribute("innerHTML")
                    connected_html_obj = HTML(html=connected_html_str)

                    # actual_roses_name = connected_html_obj.find("#accountName", first=True).text
                    actual_roses_name = driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/div/div[4]/table/tbody/tr/td[2]/div').text

                    if '(Managed)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + 'Skipped--Customer name already flagged with "(Managed)"')
                    elif '(SSO+BUIP)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO+BUIP)','(Managed)'))
                    elif '(SSO + BUIP)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO + BUIP)','(Managed)'))
                    elif '(BUIP+SSO)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(BUIP+SSO)','(Managed)'))
                    elif '(BUIP + SSO)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(BUIP + SSO)','(Managed)'))
                    elif '(SSO+OR)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO+OR)','(Managed)'))
                    elif '(BUIP)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(BUIP)','(Managed)'))
                    elif '(SSO+OR API)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO+OR API)','(Managed)'))
                    elif '(SSO + OR API)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO + OR API)','(Managed)'))
                    elif '(SSO + OR)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO + OR)','(Managed)'))
                    elif '(SSO+OR)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO+OR)','(Managed)'))
                    elif '(SSO +OR)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO +OR)','(Managed)'))
                    elif '(SSO+ OR)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO+ OR)','(Managed)'))
                    elif '(OR + SSO)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(OR + SSO)','(Managed)'))
                    elif '(SSO + OR CSV)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO + OR CSV)','(Managed)'))
                    elif '(SSO+OR API)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO+OR API)','(Managed)'))
                    elif '(SSO)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO)','(Managed)'))
                    elif '(OR+SSO)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(OR+SSO)','(Managed)'))
                    elif '(SSO BUIP)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(SSO BUIP)','(Managed)'))
                    elif '(BUIP+ SSO)' in actual_roses_name:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + actual_roses_name.replace('(BUIP+ SSO)','(Managed)'))
                    else:
                        self.true_roses_name.append(oracle_ids[1] + ',' + actual_roses_name + ',' + 'Skipped--Cannot find search string in roses name')

                except Exception as e:
                    self.true_roses_name.append(oracle_ids[1] + ',' + 'ERRRR could not find oracle account' + ',' + 'Skipped')

                    continue
        file.close()

        #Delete connected csv file if it exists
        if(os.path.exists('oracle_connected_names.csv') and os.path.isfile('oracle_connected_names.csv')):
            os.remove('oracle_connected_names.csv')
            print('file deleted')
        else:
            print('file not found')

        #Create connected csv file
        with open('oracle_connected_names.csv', 'w') as file:
            for a in self.true_roses_name:
                file.write(a + '\n')
        file.close()

    def final_change(self):
        #Write changes to csv and log errors from try
        header = ['oracle_id','oracle_name','updated_oracle_name','status']
        connected_oracle_names = ('oracle_connected_names.csv')
        filename = ('output/RosesAccounts' + time.strftime('%Y%m%d-%H%M%S')+'testingtesting.csv')
        rows = []


        with open(connected_oracle_names, 'r') as file:
            csvreader = csv.reader(file)

        #Move all csv row values to rows varbiable
            for row in csvreader:
                rows.append(row)
        file.close()

        with open(filename, 'w') as file:
            file.write('oracle_num' + ',' + 'oracle_name' + ',' + 'new_oracle_name' + ',' + 'status')
            file.write('\n')

            #login to roses
            print('logging into roses')
            roses_url = 'https://roses-prod.cdiapps.com/roses/login.do'
            search = 'https://roses-prod.cdiapps.com/roses/subscriptionSearchAccount.do'
            time.sleep(4)
            driver.get(roses_url)
            roses_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
            roses_html_str = roses_body_el.get_attribute("innerHTML")

            roses_html_obj = HTML(html=roses_html_str)
            time.sleep(2)

            #input connected user pass
            driver.find_element(By.NAME, "username").send_keys(roses.u)
            driver.find_element(By.NAME, "password").send_keys(roses.p + Keys.ENTER)
            time.sleep(5)

            bad_strings = ['(SSO+BUIP)','(SSO + BUIP)','(BUIP+SSO)','(BUIP + SSO)','(SSO +BUIP)','(SSO+ BUIP)','(BUIP +SSO)','(BUIP+ SSO)','(SSO+OR)','(BUIP)','(SSO+OR API)','(SSO + OR API)','(SSO + OR)','(SSO+OR)','(SSO +OR)','(SSO+ OR)','(OR + SSO)','(SSO + OR CSV)',' (SSO+OR API)','(SSO)','(OR+SSO)','(SSO BUIP)','(BUIP+ SSO)']

            for oracle_names in rows:
                driver.get(search)
                roses_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
                roses_html_str = roses_body_el.get_attribute("innerHTML")

                roses_html_obj = HTML(html=roses_html_str)
                time.sleep(3)

            # Multiple If statements to correct
                if '(Managed)' in oracle_names[1]:
                    print('Managed already in name: ' + str(oracle_names[1]))
                    pass
                elif any(x in oracle_names[1] for x in bad_strings) and 'Err' not in oracle_names[2]:
                    print(oracle_names)
                    print('found oracle name, searching..')
                    driver.find_element(By.NAME, "acctNm").send_keys(oracle_names[1] + Keys.ENTER)
                    time.sleep(3)

                    try:
                        editer = driver.find_element(by=By.LINK_TEXT, value='Edit')
                        editer.click()

                        time.sleep(3)
                        roses_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
                        roses_html_str = roses_body_el.get_attribute("innerHTML")

                        roses_html_obj = HTML(html=roses_html_str)
                        time.sleep(5)
                        current_name = driver.find_element(By.NAME, "acctNm").clear()
                        current_name = driver.find_element(By.NAME, "acctNm").send_keys(oracle_names[2])

                        saver = driver.find_element(by=By.CLASS_NAME, value='buttonFace')
                        saver.click()
                        file.write(str(oracle_names[0]) + ',' + str(oracle_names[1]) + ',' + str(oracle_names[2]) + ',' + 'Success' + '\n')
                        print('Cleared and inputted new Roses name.  Saving..')
                        time.sleep(3)
                        continue
                    except Exception as e:
                        # print(oracle_names, 'error: ' + str(e))
                        print('Could not input roses name and save.')
                        file.write(str(oracle_names[0]) + ',' + str(oracle_names[1]) + ',' + str(oracle_names[2]) + ',' + 'No actions in Roses taken' + '\n')
                        time.sleep(3)
                        continue

                else:
                    file.write(str(oracle_names[0]) + ',' + str(oracle_names[1]) + ',' + str(oracle_names[2]) + ',' + 'No string in roses name--no actions taken' + '\n')
                    print('Could not find Roses name')
                    time.sleep(3)
                    continue
        file.close()
        driver.quit()

r = fixer()
r.search_roses_name()
r.final_change()
