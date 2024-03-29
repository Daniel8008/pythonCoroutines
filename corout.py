import asyncio
import os
import urllib.request

async def download_courotine(url):
    """This coroutine downloads a file from the internet or local network resource
    """
    request = urllib.request.urlopen(url)
    filename  = os.path.basename(url)
    with open(filename, 'wb') as file_handler:
        while True:
            chunk = request.read(1024)
            if not chunk:
                break
            file_handler.write(chunk)
    msg = 'Finished downloading {filename}'.format(filename=filename)
    return msg
async def main(urls):
    """Creates a group of coroutines an wait for them to finish"""
    coroutines = [download_courotine(url) for url in urls] #list comprehension for coroutine group
    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        print(item.result())

if __name__  == '__main__':
    urls  = [
        "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"
    ]


    #add to event loop for execution
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(urls))   #passing the main couroutine to event_loop to que up coroutines(Chained coroutines)
    finally:
        event_loop.close()
