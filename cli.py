import argparse
import requests
# Source - https://stackoverflow.com/a/16696317
# Posted by Roman Podlinov, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-30, License - CC BY-SA 4.0

def download_file(url,local_filename):
    if locak_file name is None:
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()
#add command line argument
parser.add_argument("url",help="description of argument 1")
# parser.add_argument("output",help = "by which name do you want to save the file")
parser.add_argument("-o","--output",help = "name of the file" , default = None)
# for adding optional argument we use -o 

args = parser.parse_args()

print(args.url)
print(args.output)
download_file(args.url,args.output)