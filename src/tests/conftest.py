import os
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from dotenv import load_dotenv
from POM.login import LoginPage

load_dotenv() 

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG_PATH = os.path.join(BASE_DIR, "config", "env.yaml")

def load_config(env):
    """Load environment configuration from YAML"""
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Configuration file not found: {CONFIG_PATH}")

    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)

    if "environments" not in config or env not in config["environments"]:
        raise ValueError(f"Environment '{env}' not found in {CONFIG_PATH}")

    env_config = config["environments"][env]
    # Replace environment variable references like ${VAR} with actual values
    for key, value in env_config.items():
        if isinstance(value, str) and value.startswith("${") and value.endswith("}") :
            env_var = value.strip("${}")
            env_config[key] = os.getenv(env_var)

    return env_config

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")
    parser.addoption("--env", action="store", default="prod", help="Environment to run tests")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

@pytest.fixture(scope="session")
def config(request):
    """Fixture to provide environment configuration from YAML"""
    env = request.config.getoption("--env")
    return load_config(env)

@pytest.fixture(scope="function", autouse=True)
def clear_browser_state(driver):
    """Clear cookies and refresh the browser before each test case."""
    driver.delete_all_cookies()
    driver.refresh()
    yield driver

@pytest.fixture(scope="session")
def driver(request, config):
    """Fixture to initialize WebDriver, optionally remote on LambdaTest"""
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    use_lambda = config.get("lt_username") and config.get("lt_access_key")

    if use_lambda:
        capabilities = {
            "browserName": browser.capitalize(),
            "browserVersion": "latest",
            "platformName": "Windows 11",
            "LT:Options": {
                "username": config["lt_username"],
                "accessKey": config["lt_access_key"],
                "build": "Pytest YAML Build",
                "name": "LambdaTest Run",
                "selenium_version": "4.0.0",
                "smartUI.project": "Automation_Hackathon",
                "w3c": True,
                "plugin": "python-pytest"
            }
        }

        remote_url = f"https://{config['lt_username']}:{config['lt_access_key']}@hub.lambdatest.com/wd/hub"
        print(f"🔗 Connecting to LambdaTest at: {remote_url}")

        options = ChromeOptions()
        options.set_capability("LT:Options", capabilities["LT:Options"])
        options.set_capability("browserName", capabilities["browserName"])
        options.set_capability("browserVersion", capabilities["browserVersion"])
        options.set_capability("platformName", capabilities["platformName"])

        driver = webdriver.Remote(command_executor=remote_url, options=options)
    else:
        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)

        elif browser == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    yield driver
    driver.quit()
