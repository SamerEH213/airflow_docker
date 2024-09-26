from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import socket
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def create_driver():
    options = Options()
    options.add_argument("--headless")
    myProxy = "172.28.0.3:9050"
    ip, port = myProxy.split(':')
    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', ip)
    profile.set_preference('network.proxy.socks_port', int(port))
    profile.set_preference('permissions.default.image', 2)
    options.profile = profile

    # Selenium WebDriver URL pointing to the Firefox node container
    selenium_url = "http://selenium_firefox_container:4444/wd/hub"

    driver = webdriver.Remote(command_executor=selenium_url,options=options)
    return driver

def test():
    driver = create_driver()
    url="https://jo.opensooq.com/ar"
    driver.get(url)
    print(driver.page_source)
    driver.quit()

default_args = {
    'owner': 'moayad',
    'email': ['altlawy19@gmail.com'],
    'email_on_failure': True
}
with DAG(
        dag_id='test',
        schedule_interval=timedelta(days=100),
        # start_date=datetime(2023,12,30,10,0)
        start_date=datetime(2024, 1, 1, 21, 5),
        default_args=default_args,
        catchup=False
) as dag:
    connection_task = PythonOperator(
        task_id='print',
        python_callable=test,
    )
connection_task
