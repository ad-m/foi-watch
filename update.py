import requests
# import urllib3
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

from io import StringIO
import csv

URL = 'https://hudoc.echr.coe.int/app/transform/csv?library=echreng&query=contentsitename%3AECHR%20AND%20(NOT%20(doctype%3DPR%20OR%20doctype%3DHFCOMOLD%20OR%20doctype%3DHECOMOLD))%20AND%20((languageisocode%3D%22POL%22))%20AND%20((kpthesaurus%3D%22148%22)%20OR%20(kpthesaurus%3D%22149%22)%20OR%20(kpthesaurus%3D%22157%22)%20OR%20(kpthesaurus%3D%22158%22)%20OR%20(kpthesaurus%3D%22160%22)%20OR%20(kpthesaurus%3D%22161%22)%20OR%20(kpthesaurus%3D%22230%22)%20OR%20(kpthesaurus%3D%22105%22)%20OR%20(kpthesaurus%3D%22201%22)%20OR%20(kpthesaurus%3D%22265%22)%20OR%20(kpthesaurus%3D%22235%22)%20OR%20(kpthesaurus%3D%22259%22)%20OR%20(kpthesaurus%3D%22327%22)%20OR%20(kpthesaurus%3D%22331%22)%20OR%20(kpthesaurus%3D%22579%22)%20OR%20(kpthesaurus%3D%22379%22)%20OR%20(kpthesaurus%3D%22389%22)%20OR%20(kpthesaurus%3D%22316%22)%20OR%20(kpthesaurus%3D%22140%22)%20OR%20(kpthesaurus%3D%22452%22))&sort=&start=0&length=500&rankingModelId=11111111-0000-0000-0000-000000000000'
req = requests.get(URL)
req.encoding = 'UTF-8'
content = req.text

with StringIO(content) as infile:
    with open('content.csv', 'w+', encoding="utf-8") as outfile:
        reader = csv.reader(infile, delimiter=',')
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(reader)
