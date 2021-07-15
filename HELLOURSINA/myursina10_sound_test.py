from ursina import Ursina, printvar
from ursina.audio import Audio
# from replit import audio
# audio.play_file("place.wav")

app = Ursina()

a = Audio(sound_file_name='baduk.mp3', pitch=1, loop=True, autoplay=True)
print(a.clip)
a.volume=0
b = Audio(a.clip)

def input(key):
    if key == 'f':
        a.fade_out(duration=4, curve=curve.linear)
        
app.run()