from pygame import mixer

#Instantiate mixer
mixer.init()

#Load audio file
mixer.music.load('antiromantic.ogg')

#Set preferred volume
mixer.music.set_volume(0.2)

#Play the music
mixer.music.play()

