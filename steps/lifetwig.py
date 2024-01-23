from time import sleep

from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@step('Navigate to "{env_name}" environment')
def open_url(context, env_name):

    env_dict = {
        "qa": "https://www.qa.lifetwig.com/",
        "uat": "https://www.uat.lifetwig.com/",
        "prod": "https://www.lifetwig.com/",
    }

    url = env_dict[env_name]
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    # context.driver.maximize_window()
    context.driver.get(url)


@step('Login as "{role}"')
def login_as(context, role):

    roles = {
        "Admin": ('pcs.class1223@gmail.com', 'Qwertyui1@'),
        "Manager": ('pcs.class1223+2@gmail.com', 'Qwertyui2@'),
        "User": ('pcs.class1223+3@gmail.com', 'Qwertyui3@')
    }

    xpath = "//input[@placeholder='Email Address']"
    element = context.driver.find_element(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"
    element.send_keys(roles[role][0])

    xpath = "//input[@placeholder='Password']"
    element = context.driver.find_element(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"
    element.send_keys(roles[role][1])

    click_on(context,"Login")


@step('Wait {timeout} seconds')
def wait_for(context, timeout):
    print(f"Waiting for {timeout} seconds")
    sleep(int(timeout))


@step('Verify login page is displayed')
def verify_login_page(context):
    element = context.driver.find_element(By.XPATH, "//div[text()='Let’s Sign You In']")
    assert element, "Element //div[text()='Let’s Sign You In'] not found"


@step('Type "{string}" into field "{input_element}"')
def type_text(context, string, input_element):
    print(string)

    if input_element.upper() == 'EMAIL':
        xpath = "//input[@placeholder='Email Address']"
    elif input_element == 'password':
        xpath = "//input[@placeholder='Password']"
    else:
        assert False, "Unexpected input field"

    element = context.driver.find_element(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"
    element.send_keys(string)


@step('Click on "{element_name}"')
def click_on(context, element_name):
    # if element_name == 'Login':
    #     xpath = "//button[./span[text()='Login']]"
    # elif element_name == 'Settings':
    #     xpath = "//a[.//p[text()='Settings']]"

    xpath_dict = {
        "Login": "//button[./span[text()='Login']]",
        "Settings": "//a[.//p[text()='Settings']]"
    }

    xpath = xpath_dict[element_name]
    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"{xpath}")))
    assert element, f"Element with xpath {xpath} is not found"
    element.click()


@step("Verify user is logged in")
def step_impl2(context):
    # element = context.driver.find_elements(By.XPATH, "//div[text()='pcs.class1223@gmail.com']")
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((
        By.XPATH, "//div[text()='pcs.class1223@gmail.com']")))
    assert element, f"User is not logged in, element //div[text()='pcs.class1223@gmail.com'] not found"


@step('Switch "{state}" element "{xpath}"')
def step_impl(context, state, xpath):
    element = context.driver.find_element(By.XPATH, f"{xpath}")
    element_status = element.get_attribute("class")

    is_on = "ant-switch-checked" in element_status
    # if state == "On" and not is_on or state == "Off" and is_on:
    if state == "On" and not is_on:
        element.click()
    elif state == "Off" and is_on:
        element.click()


@step('Revert switch "{state}" of element "{xpath}"')
def revert_switch(context, state, xpath):
    elements = context.driver.find_elements(By.XPATH, f"{xpath}")

    for element in elements:
        element_status = element.get_attribute("class")
        is_on = "ant-switch-checked" in element_status

        if state == "On" and not is_on:
            element.click()
        elif state == "Off" and is_on:
            element.click()


@step('Click on menu in settings "{menu_item}"')
def click_settings_menu_items(context, menu_item):
    xpath = f"//a[text()='{menu_item}']"
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()


@step('Switch privacy for "{privacy_field}" to "{p_level}"')
def step_impl(context, privacy_field, p_level):
    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, f"//div[./div[./p[text()='{privacy_field}']]]//span[@class='ant-select-selection-item']"
    )))
    element.click()

    # if privacy_field == "Friends and relatives list":
    #     menu = 1
    # if privacy_field == "Feed":
    #     menu = 2

    menu = {
        "Friends and relatives list": 1,
        "Feed": 2
    }

    xpath = f"//div[./div[@id='rc_select_{menu[privacy_field]}_list']]//div[text()='{p_level}']"
    element_menu = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, xpath
    )))
    element_menu.click()


@step('Switch privacy')
def switch_privacy(context):

    for row in context.table:
        element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, f"//div[./div[./p[text()='{row["group"]}']]]//span[@class='ant-select-selection-item']"
        )))
        element.click()

        lists = {
            'Friends and relatives list': 1,
            'Feed': 2,
            'Family Tree': 3,
            'About information': 4,
            'Location': 5,
            'Photos': 6,
            'Videos': 7
        }

        xpath = f"//div[./div[@id='rc_select_{lists[row["group"]]}_list']]//div[text()='{row["level"]}']"
        element_menu = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, xpath
        )))
        element_menu.click()
        sleep(2)


@step('Login with credentials username "{login}" password "{passwd}" result "{res}"')
def login_with_credentials(context, login, passwd, res):

    xpath = "//input[@placeholder='Email Address']"
    element = context.driver.find_element(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"
    element.send_keys(login)

    xpath = "//input[@placeholder='Password']"
    element = context.driver.find_element(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"
    element.send_keys(passwd)

    click_on(context, "Login")

    sleep(2)
    result = None
    try:
        elements = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, f"//div[text()='{login}']")))
        if len(elements) > 0:
            result = True
    except:
        print("No elements found!!!!")
        result = False

    # elements = context.driver.find_elements(By.XPATH, f"//div[text()='{login}']")

    if result and res == 'true':
        assert True
    elif not result and res == 'false':
        assert True
    else:
        assert False


@step("Click google play button")
def google_play(context):
    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, "//a[contains(@href, 'google')]"
    )))

    current_window = context.driver.current_window_handle
    element.click()
    context.driver.switch_to.window(context.driver.window_handles[1])
    gp_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((
        By.XPATH, "//h1[text()='LifeTwig']"
    )))

    assert gp_element, f"Element not found"
    sleep(2)
    context.driver.close()
    context.driver.switch_to.window(current_window)
    sleep(2)


