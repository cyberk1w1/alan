from urllib.parse import urlparse, unquote
import base64
import time
import html
import requests


#http://www.615615.famiaagrofeedslivestock.com/YW50b25pby5yYXlvQGFsYmFzdGFyLmVz#aHR0cHM6Ly9hc2tkZW5uaXNjb3dhbi5jb20vd3N1L29uMj84MDA5MDUwMDk4OTkwMDA5JmNvbmZpcm09YW50b25pby5yYXlvQGFsYmFzdGFyLmVz
#Lab for discover new family
def b64phishingv1(value):
    value = str(base64.b64decode(value))
    return(value)
url = 'http://www.615615.famiaagrofeedslivestock.com/YW50b25pby5yYXlvQGFsYmFzdGFyLmVz#aHR0cHM6Ly9hc2tkZW5uaXNjb3dhbi5jb20vd3N1L29uMj84MDA5MDUwMDk4OTkwMDA5JmNvbmZpcm09YW50b25pby5yYXlvQGFsYmFzdGFyLmVz'
array_gods = ["Ra", "Horus", "Osiris"]

def DecoderRa(url):
    return(url)
def DecoderHorus(url):
    return(url)
def DecoderOsiris(url):
    return(url)

# Detector
#ParseResult(scheme='http', netloc='www.615615.famiaagrofeedslivestock.com', path='/YW50b25pby5yYXlvQGFsYmFzdGFyLmVz', params='', query='', fragment='aHR0cHM6Ly9hc2tkZW5uaXNjb3dhbi5jb20vd3N1L29uMj84MDA5MDUwMDk4OTkwMDA5JmNvbmZpcm09YW50b25pby5yYXlvQGFsYmFzdGFyLmVz')
#if parse_url.scheme != '' and parse_url.netloc != '' and parse_url.path != '' and parse_url.params == '' and parse_url.query == '' and parse_url.fragment == '':
#    return(DecoderAnubis(formated_decode_url))
#elif parse_url.scheme != '' and parse_url.netloc != '' and parse_url.path != '' and parse_url.params == '' and parse_url.query != '' and parse_url.fragment == '':
#    return(DecoderThot(formated_decode_url))
#elif parse_url.scheme != '' and parse_url.netloc != '' and parse_url.path != '' and parse_url.params == '' and parse_url.query != '' and parse_url.fragment != '':
#    return(DecoderIsis(formated_decode_url))
#elif parse_url.scheme != '' and parse_url.netloc != '' and parse_url.path != '' and parse_url.params == '' and parse_url.query == '' and parse_url.fragment !='':
#   return(DecoderAmon(formated_decode_url))
#def DecoderAmon(url):
#    url = url.split('#') #
#    first_url = url[0]
#    parse_f_url = urlparse(first_url)
#    b64_f_url = parse_f_url.path[1:] + "=="
#    decode_b64_f_url = b64phishingv1(b64_f_url)
#    print("Target > ", decode_b64_f_url[2:-1])
#    random_mail = 'bill.ford.gallantine@hotmail.com'
#    encoded_mail = base64.b64encode(random_mail.encode())
#    encoded_mail = str(encoded_mail)[2:-1]
#    first_new_url = parse_f_url.scheme + '://' + parse_f_url.netloc + "/" + str(encoded_mail)
#    first_new_url = str(first_new_url)[:-1]
#    print("REDIRECT URL > ", first_new_url)
#    second_url = url[1]
#    decode_b64_s_url = b64phishingv1(second_url)
#    decode_b64_s_url = decode_b64_s_url[2:-1]
#    split_s_url = decode_b64_s_url.split("=") 
#    split_s_url[1] = 'bill.ford.gallantine@hotmail.com'
#    construct_s_url = str(split_s_url[0]) + "=" + str(split_s_url[1])
#    encode_construct_s_url = base64.b64encode(construct_s_url.encode())
#    encode_construct_s_url = str(encode_construct_s_url)[2:-2]
#    second_new_url = encode_construct_s_url
#    print("SECOND > ", second_new_url)
#    final_url = first_new_url + "#" + second_new_url
#    print("FINAL > ", final_url)
#    return(final_url)
#DecoderAmon(url)