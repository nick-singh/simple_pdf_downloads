import os
import requests
import time
from multiprocessing.pool import ThreadPool



url = "https://tatt.org.tt/DesktopModules/Bring2mind/DMX/API/Entries/Download?Command=Core_Download&EntryId=%d&PortalId=0&TabId=222"
downloadable_list = []
def download_file(url):
    r = requests.get(url, allow_redirects=True)
    if r.status_code == 200 and "pdf" in r.headers['content-type'].lower():
        print("We are able to download a pdf from this url:\n%s"%(url))
        file_name = r.headers['Content-Disposition'].split('filename=')[1].replace('"','')
        print("we are now downloadling the file:\n%s"%(file_name))
        with open("downloads/"+file_name, 'wb') as f:
            print("we are now downloadling the file:\n%s"%(file_name))
            f.write(r.content)
        print("done...")
        return True
    return False


consecutive_unsuccessful_count = 0
unsuccessful_threshold = 200
sleep_time = 3

for i in xrange(1,4001):
    if consecutive_unsuccessful_count > unsuccessful_threshold:
        break
    else:
        print("trying number: %d\n\n" %(i))
        if download_file(url % (i)):
            consecutive_unsuccessful_count = 0
            time.sleep(sleep_time)
        else:
            consecutive_unsuccessful_count+=1
