#!/usr/bin/python
import os
import shutil
from tinytag import TinyTag 
import sys
from pydub import AudioSegment
from time import time 


# pip install tinytag
# pip install pydub
# you also need ffmpeg installed on the machine

def makeOutputFolder(folderLocation):
    if not os.path.exists(folderLocation):
        os.makedirs(folderLocation)

def copyFilesAndConvert(dirName, outFolder):
    makeOutputFolder(outFolder)
    print("dirName='%s', outname = '%s'" % (dirName, outName))
    
    filesInDir = sorted(os.listdir( dirName ))
    
    for file in filesInDir:
        fullPath = dirName + '/' + file
        isDirectory = os.path.isdir(fullPath)
        print("file = '%s', isDirectory = %s" % (file, str(isDirectory)))

        if (isDirectory == True):
            newOutDir = outFolder + "/" + file
            copyFilesAndConvert(fullPath, newOutDir)

        elif file.endswith((".mp3")):
            print('got an mp3 %s' % file)
            outDest = outFolder + '/' + file
            shutil.copyfile(fullPath, outDest)

        elif file.endswith((".m4a")):
            fullFileName = dirName + '/' + file
            outFileName = outFolder + '/' + file.replace('.m4a','.mp3')
            print('Converting! outFileName = "%s", orig name = "%s"' % (outFileName, file))
            audio = TinyTag.get(fullFileName, image=True)
            if (audio != None and audio.bitrate != None):

                tags = {}
                tags['artist'] = audio.artist
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



if(len(sys.argv) > 2):
    dirName = sys.argv[1].strip()
    outName = sys.argv[2].strip()
    copyFilesAndConvert(dirName, outName)
