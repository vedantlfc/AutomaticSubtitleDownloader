import sys, os, requests, re, zipfile, shutil

from bs4 import BeautifulSoup

prep = "https://subscene.com"
url = prep+"/subtitles/release?q="

sot = str(sys.argv[1])
#sot = "D:\Movies\Movies set 2\Repo Men {2010} DVDRIP. Jaybob\Repo Men {2010} DVDRIP. Jaybob.avi"
#sot = "D:\Movies\dls\Butch Cassidy\Butch Cassidy and the Sundance Kid_1969_DVDrip_XviD~Ekolb.avi"
#sot = "D:\Movies\dls\Art Of the steal\The.Art.of.the.Steal.2013.SweSub.BRRip.x265-HQM.mkv"
#sot = "D:\Movies\dls\Blade (1998)\Blade 1998.mkv"
#sot = "D:\Movies\Movies set 2\Primal Fear (1996)"
print(sot)
print("Done 10")

movie = str(os.path.splitext(os.path.basename(sot))[0])

mabba = movie.lower()

if mabba.__contains__("rip") or mabba.__contains__("bluray"):
    print("yolo")
else:
    movi = movie.replace(" ", ".")
    movie = movi+".brrip"


print(movie)

page = requests.get(url+movie)

soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find(class_='content')
body = content.find('tbody')
print("done 20")


sub_items = body.find_all('tr')

for sub in sub_items:
    al = sub.find('a')
    linko = str(al.get('href'))
    p = re.match(r'(.*/english/.*$)', linko)
    if(p):
        print("done 32")

        comp_linko = prep + linko
        print(comp_linko)

        page2 = requests.get(comp_linko)

        soup2 = BeautifulSoup(page2.content, 'html.parser')

        dl = soup2.find(class_='download')
        a2 = dl.find('a')
        acq_link = str(a2.get('href'))

        sublink = requests.get(prep + acq_link)

        print("done 47")
        # save to file
        zipFile1 = open('sub.zip', 'wb')

        for chunk in sublink.iter_content(100000):
            zipFile1.write(chunk)

        zipFile1.close()

        print("done 56")
        try:
            with zipfile.ZipFile("sub.zip", "r") as zip_ref:
                for name in zip_ref.namelist():
                    localFilePath = zip_ref.extract(name, '/tmp/')
                    print(localFilePath)
        except zipfile.BadZipFile:
            continue
        break





s = re.sub(r"\....$", ".srt", sot)
shutil.move(localFilePath, s)
os.remove("sub.zip")
print("done 63")

