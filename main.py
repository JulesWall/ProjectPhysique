import numpy as np
import serial
import csv
import matplotlib.pyplot as plt
import tkinter as tk
from Data import *
from Display import *
from Plot import Plot

serial_port=serial.Serial(port='COM27', baudrate=9600)#definition du port série avec un débit de 9600 baud.
datas = Data()
display = Display(datas)
fichier = open("save.txt", "w")
i = 0
while 1:
    i+=1
    if i > 3 :
        data_texte=serial_port.readline()
        data = data_texte.decode('UTF-8')
        print(data)
        da = datas.new(data)
        fichier.write(data)
        datas.save_csv()
        try:p = Plot(datas).new()
        except:pass
        if da != None : display.root.after(500, display.update(da[0],da[1],da[2]))

fichier.close()
display.root.mainloop()
serial_port.close()

