
# Alan

  

**Alan** is a software developed in Python 3 that analyzes different types of threats based on the attacks received. For now it incorporates analysis capabilities of phishing, malware and eml files.

  



## Requeriments

  

- Python 3.x

- requests `pip3 install requests`

- selenium `pip3 install selenium`

- pefile `pip3 install pefile` 

- Geckodriver: [Download Here](https://github.com/mozilla/geckodriver/releases)

- API Key from VT (Setup in alan_mod_mlwscan.py file)

  

## How to use

- **Setup**: *VT_API_KEY*, *DOWNLOAD_GECKODRIVER_LIN32|64/WIN32|64*

- **Run GUI**: python3 alan-gui.py

- **Phishing**: To analyze a phishing file we must only have access to the .html file sent by users for analysis. These files are usually encoded with URLencode. I have found and instrumentalized the two different versions we have of phishing.

- The **Anubis** model is for phishing that have their *PATH* encoded in ***base64*** and only the user part is encoded.

- The **Thot** model contains both the ***PATH*** and the ***QUERY*** of the URL encoded in ***base64***.

- The **Isis** model is for phishing that is hosted on **public platforms** like firebase.

  
 - **Malware**: To scan files suspected of containing malware we can get a **list of the potentially dangeorus functions** for the system. To know the address where the function is located we have another feature that returns ***ADDRES:FUNCTION***. We can upload the suspicious samples to VirusTotal by configuring the platform ***API-KEY***.

     `python3 alan-gui.py`
 
**Phishing**

 - Scan Phishing File
 - Scan URL 

**Malware**
 -  Scan Import EXE File
 -  Scan Address + Functions
 -  Upload & get report to VT
 -  Scan String EXE FILE (regexp)

		 
		 
		
		 
  
## TO DO

  

- [x] Phishing Support

- [x] Decode route PATH & QUERY from b64

- [x] Render web with GeckoDriver

- [x] Generate random mail

- [ ] Upload URL to urlscan.io

- [x] Malware

- [x] Suspicious DLLs

- [x] Upload & Report [VirusTotal](https://www.virustotal.com/gui/home/upload)

- [ ] Upload & Report [tria.ge](https://tria.ge/login?url=/dashboard)

- [ ] RegExp for EXE strings 

- [ ] Analyze DOCX & PDF

- [ ] Spam

- [ ] EML Parser

- [ ] Get connection Flow and Render

- [ ] Check SPF

- [ ] Check DMARC