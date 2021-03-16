#!/usr/bin/python
import os
from tinytag import TinyTag 
import sys
from pydub import AudioSegment
from time import time 


# pip install tinytag
# pip install pydub
# you also need ffmpeg installed on the machine

if(len(sys.argv) >= 1):
    dirName = sys.argv[1].strip()
    print("dirName='%s'" % (dirName))
    # path is a directory of which you want to list
    filesInDir = sorted(os.listdir( dirName ))
    gotOne = False
    # This would print all the files and directories
    for file in filesInDir:
        if gotOne == False:
            fullFileName = dirName + '/' + file
            outFileName = '/tmp/tester_' + str(time()).replace('.','_') + '.mp3'
            print('I want one! outFileName = "%s", orig name = "%s"' % (outFileName, file))
            audio = TinyTag.get(fullFileName)
            if (audio != None and audio.bitrate != None):
                print("Title:" + audio.title) 
                print("Artist: " + audio.artist) 
                print("Genre:" + audio.genre) 
                print("Year Released: " + audio.year) 
                print("Bitrate:" + str(audio.bitrate) + " kBits/s") 
                print("AlbumArtist: " + audio.albumartist) 
                print("Duration: " + str(audio.duration) + " seconds") 

                convertedVersion = AudioSegment.from_file(fullFileName)
                convertedVersion.export(outFileName, format="mp3")

                gotOne = True
        print(file)