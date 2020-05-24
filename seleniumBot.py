import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url='https://www.workana.com/jobs?category=it-programming&subcategory=mobile-development&language=en%2Cpt#page=1'

classTitulos='.project-item .project-title'
classValues="values"
classDescription=".project-item .project-details"

def buildJson(elementsTitles,elementsDescription,elementsValues):
    json='{"data":['
    count=0
    for title in elementsTitles:
        name='"name":"{0}",'.format(title.text)
        value='"value":"{0}",'.format(elementsValue[count].text)
        description='"desc",'.format(elementsDescription[count].text)
        link='"link":"{0}"'.format(title.find_element(By.TAG_NAME,"a").get_attribute("href"))

        
