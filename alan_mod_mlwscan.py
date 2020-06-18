import pefile
import requests
apikey = 'SETUP THIS'
def GetLineFromFile(file):
    arrayF = []
    f = open(file, 'r')
    for l in f:
        l = str(l)[:-1]
        arrayF.append(l)
    return arrayF
def ShowImportsDllEXE(file):
    pe = pefile.PE(file)
    pe.parse_data_directories()
    functionarray = []
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        for imp in entry.imports:
           functionarray.append(str(imp.name)[2:-1])
    return functionarray

def CompareTwoList(exefile, textfile):
    l1= ShowImportsDllEXE(exefile)
    l2 = GetLineFromFile(textfile)
    ctl = set(l1) & set(l2)
    arrayAux = []
    for function in ctl:
        arrayAux.append(function)
    return arrayAux

def GetHexFromImportFunctions(file):
    pe = pefile.PE(file)
    pe.parse_data_directories()
    HexList = {}
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        for imports in entry.imports:
            HexList[hex(imports.address)] = str(imports.name)[2:-1]
    return HexList

def WrapperVTApiScanFile(file):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': apikey}
    files = {'file': (file, open(file, 'rb'))}
    response = requests.post(url, files=files, params=params)
    js = response.json()
    resource = js['resource']
    return(resource)
    
def WrapperVTApiGetReportFile(resource):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey':apikey, 'resource': resource}
    response = requests.get(url, params=params)
    js = response.json()
    r = js['resource'] # HASH
    p = js['positives'] # TOTAL POSITIVES
    ListResult = {}
    ListResult[r] = p
    return(ListResult)
