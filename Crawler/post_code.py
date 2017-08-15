import requests
import xml.etree.ElementTree  as ET
from xml.parsers.expat import ParserCreate
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
class DefaultSaxHandler(object):
    def __init__(self,provinces):
        self.provinces=provinces
    def start_element(self,name,attrs):
        if name!='map':
            name=attrs['title']
            number=attrs['href']
            self.provinces.append((name,number))
    def end_element(self,name):
        pass
    def char_data(self,text):
        pass

def get_province_entry(url):
    content=requests.get(url).content.decode('gb2312')
    start=content.find('<map name=\"map_86\" id=\"map_86\">')
    end=content.find('</map>')
    content=content[start:end+len('</map>')].strip()
    #print content
    provinces=[]
    handler=DefaultSaxHandler(provinces)
    parser=ParserCreate()
    parser.StartElementHandler=handler.start_element
    parser.EndElementHandler=handler.end_element
    parser.CharacterDataHandler=handler.char_data
    parser.Parse(content)
    return provinces

def get_city_entry(url):
    print url
    content=requests.get(url).content
    print content
    start=content.find('<tbody>')
    end=content.find('</tbody>')
    content=content[start:end+len('</tbody>')].strip()
    print content
    
    
if __name__=='__main__':
    u1='http://www.ip138.com/post'
    provinces=get_province_entry(u1)
    for (k,v) in provinces:
        print k+'--------:'
        get_city_entry(u1+v)
        break