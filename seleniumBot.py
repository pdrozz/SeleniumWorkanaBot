import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date


url='https://www.workana.com/jobs?category=it-programming&subcategory=mobile-development&language=en%2Cpt#page=1'

classTitulos='.project-item .project-title'
classValues="values"
classDescription=".project-item .project-details"

def buildJson(elementsTitles,elementsDescription,elementsValues):
    json='{"data":['
    count=0
    for title in elementsTitles:
        name='"name":"{0}",'.format(title.text)
        value='"value":"{0}",'.format(elementsValues[count].text)
        description='"desc",'.format(elementsDescription[count].text)
        link='"link":"{0}"'.format(title.find_element(By.TAG_NAME,"a").get_attribute("href"))

        body="{",name,value,description,link,"}"
        body+=body.replace("\n"," ")

        count+=1

        if(count==len(elementsTitles)):
            json+="]}'"
        elif(count<len(elementsTitles)):
            json+=","
    return json

def writeJson(filename,json):
    try:
        f=open("projectsJson/",filename,".json","w")
        f.write(json)
    except Exception as identifier:
        print("Error to write json file")
        print(str(identifier))
    finally:
        f.close()

def writeJson(json):
    try:
        f=open("projectsJson/",str(date.today()),".json","w")
        f.write(json)
    except Exception as identifier:
        print("Error to write json file")
        print(str(identifier))
    finally:
        f.close()