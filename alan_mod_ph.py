from urllib.parse import unquote
import re
from urllib.parse import urlparse
import base64
import string
import random
from selenium import webdriver
import time
import hashlib
import requests
import html
import alan_mod_bd
#FUNCTIONS
def IsLive(url):
    r = requests.get(url)
    try:
        if r.status_code == 200:
            return True
        elif r.status_code == 301:
            return True
        else:
            return False
    except:
        print("Error with > ", url)
        pass
def b64phishingv1(value):
    value = str(base64.b64decode(value))
    return(value)  

def DecoderDetector(url):
    decode_url = unquote(url)
    decode_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.#&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',decode_url)
    formated_decode_url = str(decode_url)[2:-2]
    print("Detector URL format decode: ", formated_decode_url)
    parse_url = urlparse(formated_decode_url)
    print("Detector URL Parser", parse_url)
    if parse_url.scheme != '' and parse_url.netloc != '' and parse_url.path != '' and parse_url.params == '' and parse_url.query == '' and parse_url.fragment == '':
        return(DecoderAnubis(formated_decode_url))
    elif parse_url.scheme != '' and parse_url.netloc != '' and parse_url.path != '' and parse_url.params == '' and parse_url.query != '' and parse_url.fragment == '':
        return(DecoderThot(formated_decode_url))
    elif parse_url.scheme != '' and parse_url.netloc != '' and parse_url.path != '' and parse_url.params == '' and parse_url.query != '' and parse_url.fragment != '':
        return(DecoderIsis(formated_decode_url))
    elif parse_url.scheme != '' and parse_url.netloc != '' and parse_url.path != '' and parse_url.params == '' and parse_url.query == '' and parse_url.fragment !='':
        return(DecoderAmon(formated_decode_url))

def DecoderAmon(url):
    #ParseResult(scheme='http', netloc='www.615615.famiaagrofeedslivestock.com', path='/YW50b25pby5yYXlvQGFsYmFzdGFyLmVz', params='', query='', fragment='aHR0cHM6Ly9hc2tkZW5uaXNjb3dhbi5jb20vd3N1L29uMj84MDA5MDUwMDk4OTkwMDA5JmNvbmZpcm09YW50b25pby5yYXlvQGFsYmFzdGFyLmVz')
    url = url.split('#') 
    first_url = url[0]
    parse_f_url = urlparse(first_url)
    b64_f_url = parse_f_url.path[1:] + "=="
    decode_b64_f_url = b64phishingv1(b64_f_url)
    print("Target > ", decode_b64_f_url[2:-1])
    random_mail = 'bill.ford.gallantine@hotmail.com'
    encoded_mail = base64.b64encode(random_mail.encode())
    encoded_mail = str(encoded_mail)[2:-1]
    first_new_url = parse_f_url.scheme + '://' + parse_f_url.netloc + "/" + str(encoded_mail)
    first_new_url = str(first_new_url)[:-1]
    print("REDIRECT URL > ", first_new_url)
    second_url = url[1]
    decode_b64_s_url = b64phishingv1(second_url)
    decode_b64_s_url = decode_b64_s_url[2:-1]
    split_s_url = decode_b64_s_url.split("=") 
    split_s_url[1] = 'bill.ford.gallantine@hotmail.com'
    construct_s_url = str(split_s_url[0]) + "=" + str(split_s_url[1])
    encode_construct_s_url = base64.b64encode(construct_s_url.encode())
    encode_construct_s_url = str(encode_construct_s_url)[2:-2]
    second_new_url = encode_construct_s_url
    print("SECOND > ", second_new_url)
    final_url = first_new_url + "#" + second_new_url
    print("FINAL > ", final_url)
    return(final_url)
    
def DecoderAnubis(decode_url):
    formated_decode_url = str(decode_url)
    parse_url = urlparse(formated_decode_url)
    b64value = parse_url.path[1:]
    b64value = b64phishingv1(b64value)
    print("Target > ", b64value[2:-1])
    domain = parse_url.netloc
    random_mail = 'bill.ford.gallantine@hotmail.com'
    encoded_mail = base64.b64encode(random_mail.encode())
    str_encoded_mail = str(encoded_mail)[2:-1]
    new_domain = 'https://' + str(domain) + '/' + str_encoded_mail
    return(new_domain)

def DecoderThot(decode_url): 
    #ParseResult(scheme='https', netloc='O2ms1xk0.cn', path='/qjqysa2sCdawnnewV2oCD4kXR/', params='', query='zt6058h1Xp2=cmVjb3Jkc0BhbGJhc3Rhci5lcw==', fragment='')
    decode_url[1] = ''
    formated_decode_url = str(decode_url) 
    formated_decode_url = html.unescape(formated_decode_url) 
    formated_decode_url = str(decode_url)[2:-6]
    parse_url = urlparse(formated_decode_url) 
    print(parse_url)
    query = parse_url.query
    lista = []
    for char in query:
        lista.append(char)
        if char == "=":
            break
    jlist = ''.join(map(str, lista))
    new_target = 'bill.ford.gallantine@hotmail.com'
    encoded_mail = base64.b64encode(new_target.encode())
    new_url = str(parse_url.scheme) + "://" + str(parse_url.netloc) + str(parse_url.path) + jlist + str(encoded_mail)[2:-1]
    return(new_url)

def DecoderIsis(decode_url): 
    #ParseResult(scheme='', netloc='', path="['https://firebasestorage.googleapis.com/v0/b/jkhgvcb87895579hffhd.appspot.com/o/owa.html", params='', query='alt=media&token=e987beed-b91c-4799-89a4-de500590f824', fragment="adele.civantos@albastar.es']")
    formated_decode_url = str(decode_url) 
    formated_decode_url = html.unescape(formated_decode_url) 
    print("HTML UNESCAPE: ", formated_decode_url)
    parse_url = urlparse(formated_decode_url) 
    print("PARSE URL: ", parse_url)
    new_target = 'bill.ford.gallantine@hotmail.com'
    new_url = str(parse_url.scheme) + '://' + str(parse_url.netloc) + str(parse_url.path) + '/' + str(parse_url.query) + '#' + str(new_target)
    return(new_url)   
    
def RenderHTTPRequest(request):
    driver = webdriver.Firefox(executable_path='C:\\Users\\anubis\\Desktop\\alan\\alan\\geckodriver.exe')
    driver.get(request)
    salt = str(time.time()).encode('utf-8')
    filename= hashlib.md5(salt).hexdigest() + ".png"
    driver.save_screenshot(filename)
    time.sleep(6)
    driver.quit()

    