from selenium import webdriver 
import time
import schedule
from selenium.common.exceptions import NoSuchElementException
chrome_options=webdriver.ChromeOptions()
chrome_options.add_extension('extension_1_9_0_0.crx')
driver = webdriver.Chrome(options=chrome_options)
driver.minimize_window()
def login():
    if len(driver.find_elements_by_id("username"))>0:
        username = driver.find_element_by_id("username")
        username.clear()
        username.send_keys("")
        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys("")
        loginbutton = driver.find_element_by_class_name("btn-primary") 
        loginbutton.click()
    else:
        pass    

def attendance():
    i=0
    while(True):
        if len(driver.find_elements_by_partial_link_text('Submit attendance'))>0:
            driver.find_element_by_link_text('Submit attendance').click()
            if len(driver.find_elements_by_id('id_status_22'))>0:#id is different for different courses
                driver.find_element_by_id("id_status_22").click()
            elif len(driver.find_elements_by_id('id_status_862'))>0:
                driver.find_element_by_id('id_status_862').click()
            else:
                driver.find_element_by_id("id_status_414").click()
            driver.find_element_by_id("id_submitbutton").click()   
            break
        i+=1
        if i>2:
            break
        else:
            time.sleep(5)
            driver.refresh()
def clickmeet():
    i=0
    while(True):
        if len(driver.find_elements_by_partial_link_text("Join Meeting"))>0:
            button = driver.find_element_by_partial_link_text('Join Meeting')  
            button.click()
            if "not currently" in driver.page_source:
                time.sleep(5)
                driver.refresh()
                i+=1    
            else:
                break
        if i>4:
            break    
        else:
            time.sleep(2)
            driver.refresh()
            i+=1

def joinmeet():

    classbutton=driver.find_element_by_partial_link_text("m2020ce")
    classbutton.click()
    transport=driver.find_elements_by_partial_link_text("Transportation Engineering ")
    ge=driver.find_elements_by_partial_link_text("GE-2")
    SD=driver.find_elements_by_partial_link_text("Regular")
    if len(transport)>0:
        transport[0].click()
        clickmeet()
    elif len(ge)>0:
        ge[0].click()
        clickmeet()
    else:
        SD[-1].click()
        clickmeet()
def te():
    
    driver.get("https://eduserver.nitc.ac.in/mod/attendance/view.php?id=3083")
    #these links are unique for courses
    login()
    attendance()
    joinmeet()
    driver.minimize_window()
def ge():
    
    driver.get("https://eduserver.nitc.ac.in/mod/attendance/view.php?id=5250")
    login()
    attendance()
    joinmeet()
    driver.minimize_window()
def sd():
    
    driver.get("https://eduserver.nitc.ac.in/mod/attendance/view.php?id=810")
    login()
    attendance()
    joinmeet()
    driver.minimize_window()
def sa():
    
    driver.get("https://eduserver.nitc.ac.in/course/view.php?id=149")
    login()
    driver.find_element_by_partial_link_text('Lecture').click()
    clickmeet()
    driver.minimize_window()
def nm():
    
    driver.get("https://eduserver.nitc.ac.in/mod/webexactivity/view.php?id=3886")
    login()
    clickmeet()    
    driver.minimize_window()
def gis():
    
    driver.get("https://eduserver.nitc.ac.in/mod/webexactivity/view.php?id=1281")
    login()
    clickmeet()
    driver.minimize_window()

    
schedule.every().monday.at("08:00").do(sa)
schedule.every().monday.at("10:15").do(te)
schedule.every().monday.at("11:15").do(ge)
schedule.every().monday.at("13:00").do(gis)
schedule.every().monday.at("14:00").do(sd)
schedule.every().tuesday.at("08:00").do(ge)
schedule.every().tuesday.at("09:00").do(gis)
schedule.every().tuesday.at("10:15").do(sd)
schedule.every().tuesday.at("11:15").do(nm)
schedule.every().tuesday.at("13:00").do(sa)
schedule.every().wednesday.at("09:00").do(sa)
schedule.every().wednesday.at("11:15").do(te)
schedule.every().thursday.at("08:00").do(te)
schedule.every().thursday.at("09:00").do(ge)
schedule.every().thursday.at("10:15").do(gis)
schedule.every().thursday.at("11:15").do(sd)
schedule.every().friday.at("08:00").do(sd)
schedule.every().friday.at("09:00").do(nm)
schedule.every().friday.at("10:15").do(sa)
schedule.every().wednesday.at("17:54").do(sd)
schedule.every().wednesday.at("17:55").do(sa)
schedule.every().wednesday.at("17:56").do(te)
schedule.every().wednesday.at("17:57").do(ge)
schedule.every().wednesday.at("17:58").do(gis)







while(True):
    schedule.run_pending()
    time.sleep(1)




