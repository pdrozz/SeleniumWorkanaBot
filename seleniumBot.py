import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
from os import listdir

url='https://www.workana.com/jobs?category=it-programming'

classTitulos='.project-item .project-title'
classValues="values"
classDescription=".project-item .project-details"

def buildJson(elementsTitles,elementsDescription,elementsValues):
    json='{"data":['
    count=0
    for title in elementsTitles:
        name='"name":"{0}",'.format(title.text)
        value='"value":"{0}",'.format(elementsValues[count].text)
        description='"desc":"{0}",'.format(elementsDescription[count].text)
        link='"link":"{0}"'.format(title.find_element(By.TAG_NAME,"a").get_attribute("href"))

        body="{"+name+value+description+link+"}"
        body=str(body).replace("\n"," ")

        json+=body

        count+=1

        if(count==len(elementsTitles)):
            json+="]}"
        elif(count<len(elementsTitles)):
            json+=","
    return json

def writeJson(filename,json):
    try:
        f=open("projectsJson/"+filename+".json","w")
        f.write(json)
    except Exception as identifier:
        print(str(identifier))
    finally:
        f.close()
   
def writeJson(json):
    try:
        f=open("projectsJson/"+str(date.today())+".json","w")
        f.write(json)
    except Exception as identifier:
        print(str(identifier))
    finally:
        f.close()

def cleanUrl(url):
    url+=url.replace("\n","")
    url+=url.replace('"',"")
    return url

def printGettingStart():
    print("Example workana url")
    print("https://www.workana.com/jobs?category=it-programming\n")


def start():
    try:
        printGettingStart()
        url=str(input("Write the workana url:  "))
        url=cleanUrl(url)

        path="driver/chromedriver.exe"
        driver=webdriver.Chrome(path)

        driver.get(url)

        titles = driver.find_elements(By.CSS_SELECTOR,classTitulos)
        values=driver.find_elements(By.CLASS_NAME,classValues)
        descriptions=driver.find_elements(By.CSS_SELECTOR,classDescription)

        json=buildJson(titles,values,descriptions)
        writeJson(json)

    except Exception as identifier:
        print("error as ",str(identifier))

start()

