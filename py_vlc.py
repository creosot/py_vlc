#! /usr/bin/python
# -*- coding: utf-8 -*-

import vlc
import time
import serial
import threading
import Queue


class SerialPlayer():
    def __init__(self, queue):
        self.ser = serial.Serial()
        self.ser.port = "/dev/ttyACM0"
        self.ser.baudrate = 9600
        self.queue = queue
        self.receiver_thread = 0
        # VLC player controls
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.Media = False

    def start_reader(self):
        try:
            self.ser.open()
        except Exception, e:
            print "error open serial port: " + str(e)
            exit()
        if self.ser.isOpen():
            print "serial port open"
            self.ser.flushInput()  # flush input buffer, discarding all its contents
            self.ser.flushOutput()  # flush output buffer, aborting current
            time.sleep(0.5)  # give the serial port sometime to receive the data
            self.receiver_thread = threading.Thread(target=self.reader)
            self.receiver_thread.setDaemon(True)
            self.receiver_thread.start()
        else:
            print "cannot open serial port "

    def reader(self):
        while True:
            response = self.ser.readline()
            # print("read data: " + response)
            if response[:5] == "start":
                #print "start"
                queue.put("start")
            if response[:3] == "end":
                #print "end"
                queue.put("end")

    def play(self, filename):
        self.Media = self.Instance.media_new(filename)
        self.player.set_media(self.Media)
        self.player.play()
        self.player.set_fullscreen(int(1))
        #print(self.player.get_fullscreen())
        #self.player.toggle_fullscreen()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()


if __name__ == "__main__":
    cur_rolik = ""
    queue = Queue.Queue()
    ser_play = SerialPlayer(queue)
    ser_play.start_reader()

    while True:
        if not queue.empty():
            res = queue.get_nowait()
            if cur_rolik != res:
                cur_rolik = res
                if res == "start":
                    print "start"
                    ser_play.play("/home/creosot/Downloads/v1.avi")
                if res == "end":
                    print "end"
                    ser_play.play("/home/creosot/Downloads/v2.avi")
        time.sleep(1)





    # while True:
    #     try:
    #         rolik = queue.get_nowait()
    #         print rolik
    #     except queue.empty():
    #         print "empty"

    # ser = serial.Serial()
    # ser.port = "/dev/ttyACM0"
    # ser.baudrate = 9600
    # try:
    #     ser.open()
    # except Exception, e:
    #     print "error open serial port: " + str(e)
    #     exit()
    # if ser.isOpen():
    #     try:
    #         ser.flushInput()  # flush input buffer, discarding all its contents
    #         ser.flushOutput()  # flush output buffer, aborting current output
    #         #ser.write("AT+CSQ")
    #         time.sleep(0.5)  # give the serial port sometime to receive the data
    #         numOfLines = 0
    #         while True:
    #             response = ser.readline()
    #             # print("read data: " + response)
    #             if response[:5] == "start":
    #                 print "start"
    #             if response[:3] == "end":
    #                 print "end"
    #             numOfLines += 1
    #             if numOfLines >= 5:
    #                 break
    #         ser.close()
    #     except Exception, e1:
    #         print "error communicating...: " + str(e1)
    # else:
    #     print "cannot open serial port "



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