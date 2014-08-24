#! /usr/bin/python
# -*- coding: utf-8 -*-

# import external libraries
#import wx # 2.8
import vlc
import time
import serial

# import standard libraries
#import os
#import user


class Player():
    """The main window has to deal with events.
    """
    def __init__(self):
        # VLC player controls
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()

    def onplay(self, filename):
        self.Media = self.Instance.media_new(filename)
        self.player.set_media(self.Media)
        self.player.play()
        self.player.set_fullscreen(int(1))
        #print(self.player.get_fullscreen())
        #self.player.toggle_fullscreen()

    def onpause(self):
        """Pause the player.
        """
        self.player.pause()

    def onstop(self):
        """Stop the player.
        """
        self.player.stop()


if __name__ == "__main__":
    # player = Player()
    # # show the player window centred and run the application
    # player.onplay("/home/creosot/Downloads/Oculus.avi")
    # time.sleep(10)
    # player.onplay("/home/creosot/Downloads/morpehi2014.avi")
    # time.sleep(10)
    ser = serial.Serial()
    ser.port = "/dev/tty20"
    ser.open()
    print ser.isOpen()
    #ser.port = "/dev/ttyUSB0"
    # ser.port = "/dev/ttyS2"
    # ser.baudrate = 9600
    # ser.bytesize = serial.EIGHTBITS     #number of bits per bytes
    # ser.parity = serial.PARITY_NONE     #set parity check: no parity
    # ser.stopbits = serial.STOPBITS_ONE  #number of stop bits
    # #ser.timeout = None                 #block read
    # ser.timeout = 0                     #non-block read
    # #ser.timeout = 2                    #timeout block read
    # ser.xonxoff = False                 #disable software flow control
    # ser.rtscts = False                  #disable hardware (RTS/CTS) flow control
    # ser.dsrdtr = False                  #disable hardware (DSR/DTR) flow control
    # ser.writeTimeout = 2                #timeout for write
    # try:
    #     ser.open()
    # except Exception, e:
    #     print "error open serial port: " + str(e)
    #     exit()
    # while True:
    #     ch = ser.readline()
    #     print ch