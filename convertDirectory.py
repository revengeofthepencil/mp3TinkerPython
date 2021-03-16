#!/usr/bin/python
import os
from tinytag import TinyTag 
import sys
from pydub import AudioSegment
from time import time 


# pip install tinytag
# pip install pydub
# you also need ffmpeg installed on the machine

# tags={'artist': 'Various artists', 'album': 'Best of 2011', 'comments': 'This album is awesome!'}


if(len(sys.argv) >= 1):
    dirName = sys.argv[1].strip()
    print("dirName='%s'" % (dirName))
    # path is a directory of which you want to list
    filesInDir = sorted(os.listdir( dirName ))
    gotOne = False
    # This would print all the files and directories
    for file in filesInDir:
        if file.endswith((".mp3")):
            print('got an mp3 %s' % file)
        elif file.endswith((".m4a")):
            if gotOne == False:
                fullFileName = dirName + '/' + file
                outFileName = '/tmp/out_' + str(time()).replace('.','_') + file.replace('.m4a','.mp3')
                print('I want one!! outFileName = "%s", orig name = "%s"' % (outFileName, file))
                audio = TinyTag.get(fullFileName, image=True)
                if (audio != None and audio.bitrate != None):

                    tags = {}
                    tags['artist'] = audio.artist + "_tester"
                    tags['title'] = audio.title
                    tags['albumartist'] = audio.albumartist
                    tags['album'] = audio.album
                    tags['year'] = audio.year
                    tags['date'] = audio.year
                    tags['disc'] = audio.disc
                    tags['genre'] = audio.genre
                    tags['disc_total'] = audio.disc_total


                    bitrate = ("%dk" % (int(audio.bitrate)))

                    print("Title:" + audio.title) 
                    print("Album: " + audio.album) 
                    print("Artist: " + tags['artist'] ) 
                    if(audio.genre != None):
                        print("Genre:" + audio.genre) 
                    if(audio.year != None):
                        print("Year Released: " + audio.year) 
                    print("Bitrate:" + str(bitrate)) 
                    print("Duration: " + str(audio.duration) + " seconds") 

                    convertedVersion = AudioSegment.from_file(fullFileName)
                    convertedVersion.export(outFileName, format="mp3", tags=tags, bitrate=bitrate)

                    gotOne = True
        print(file)