import pyinsane2
from gtts import gTTS
from PIL import Image
import pytesseract
import vlc

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

# scan the document
pyinsane2.init()
try:
    devices = pyinsane2.get_devices()
    assert(len(devices) > 0)
    device = devices[0]
    print("I'm going to use the following scanner: %s" % (str(device)))

    pyinsane2.set_scanner_opt(device, 'resolution', [300])
    pyinsane2.set_scanner_opt(device, 'mode', ['Color'])

# Beware: by default, some scanners only scan part of the area
# they could scan.
    pyinsane2.maximize_scan_area(device)

    scan_session = device.scan(multiple=False)
    try:
        while True:
            scan_session.scan.read()
    except EOFError:
        pass
    image = scan_session.images[-1]

    image.save("c:/Users/dogan_coruh/Desktop/deneme.bmp")
finally:
    pyinsane2.exit()

# ocr decode process
print("OCR Decoding...")
text = pytesseract.image_to_string(Image.open('c:/Users/dogan_coruh/Desktop/deneme.bmp'), lang='tur')

text = text.replace("Ä±", "ı")
text = text.replace("ÅŸ", "ş")
text = text.replace("Ã¼", "ü")
text = text.replace("Ã¶", "ö")
text = text.replace("Ã§", "ç")
text = text.replace("ÄŸ", "ğ")

print(text)

print("Reading the text...")
# read the decoded text
tts = gTTS(text=text, lang='tr')
tts.save("C:/Users/dogan_coruh/Desktop/test.mp3")

player = vlc.MediaPlayer("file:///c:/Users/dogan_coruh/Desktop/test.mp3")
player.play()

input()