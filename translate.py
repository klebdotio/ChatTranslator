import os
import sys
from os import path
import time
from googletrans import Translator
from plyer import notification
from appJar import gui

# Chat translator by Kleb and QMechanic http://chattranslator.survivalnfly.tk
# Change notification library to one that works with Windows
translator = Translator()


def launch(win):
    app.showSubWindow(win)


app = gui(showIcon=False)
if path.exists("logpath.txt"):
    f = open("logpath.txt", "r")
    if f.mode == 'r':
        log = f.read()
        prev_size = os.path.getsize(log)
        cur_size = os.path.getsize(log)
        print("Chat translator by Kleb and QMechanic")
        print("this screen is 100% Temporary, until I figure out the other GUI Properly")
        print("ChatTranslator is currently reading its Minecraft logs from:")
        print(log)
        while True:
            time.sleep(0.04)
            prev_size = cur_size
            cur_size = os.path.getsize(log)

            if prev_size == cur_size:
                continue

            try:
                file = open(log, "r")
                line = file.readlines()[-1][:-1]
                file.close()

                if "[CHAT]" not in line:
                    continue
                message = line.split("[CHAT] ")[-1]
                translation = translator.translate(message, dest="en")

                if translation.src != "en":
                    notification.notify(
                        title=translation.src,
                        message=translation.text,
                        timeout=5,
                        app_icon=None,
                    )
            except Exception as ex:
                print("Error: " + str(ex))
else:
    app.addLabel("title", "ChatTranslator by Kleb and QMechanic")
    app.addLabel("title2", "No path to Minecraft latest.log found, please")
    app.addLabel("title3", "Please specify the path below. (Please use")
    app.addLabel("title4", "/ and not \\&)")


    def press(button):
        if button == "Close":
            sys.exit()
        else:
            log = app.getEntry("Path")
            f = open("logpath.txt", "w+")
            f.write(log)


    app.addLabelEntry("Path")
    app.addLabel("title5", "When you are finished, close and reopen this program")
    app.addButtons(["Save Path To File", "Close"], press)
app.go()
