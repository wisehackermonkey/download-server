import urllib2
# https://toolbelt.readthedocs.io/en/latest/uploading-data.html
# https://stackoverflow.com/questions/68477/send-file-using-post-from-a-python-script
download_url = "http://127.0.0.1:8080/"
filename = "test.mp3"
# download_url = 'https://pythonspot-9329.kxcdn.com/wp-content/uploads/2017/09/python-tutorials.jpg'
# download_url = "http://www.sample-videos.com/audio/mp3/crowd-cheering.mp3"

mp3file = urllib2.urlopen("{}{}".format(download_url, filename))

with open('download.mp3','w') as file:
  file.write(mp3file.read())


print("DONE!")
