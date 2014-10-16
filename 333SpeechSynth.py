from os import system

print ''
print "333 Speech Synth v1.2"
print "Author: Quran Karriem"
print ''

print "version 1.2 (9.22.2014): Updates"
print "========================="
print "-Added the ability to specify which system voice to use"
print "-Added the ability to specify voice speed"
print ''

print "version 1.1 (09.17.2014): Updates"
print "=========================="
print "-Fixed a bug where apostrophes in text caused program to crash"
print ''

print "To see which voices you have installed, open System Preferences > Dictation & Speech on your Mac."
print ''
voiceName = raw_input("Please type the name of the Mac OSX voice you would like to use:  ")

print ''
print 'At what speaking rate (in words per minute) do you want the audio files?'
print 'Common speaking speeds are between 150 and 220 words per minute.'
speakingRate = raw_input("Enter a number between 90 and 720: ")

print ''
print 'You should have an unformatted .txt file in the Resources folder of this app.'
print 'By default, it is called Youhaveadog.txt, but you can edit this or use a different .txt file, as long as its in this folder.'
fileName = raw_input("Please type the full name of your .txt file: ")
textFile = open(fileName, 'r')

counter = 0
for line in textFile:
    counter += 1
    system(eval('"' + "say -v "+ voiceName + " -r " + speakingRate + " -o audio/" + str(counter) + ".aiff " + line.strip('\n') + '"'))

print ''
print "Created", counter, "synthesized voice files based on the specified text file. Check the 'audio' folder."
    


