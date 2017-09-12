# Home Automation
# (c) 2017 Pat McGee
# patmcgee1983@gmail.com

from tkinter import *
from datetime import *
from time import *
from threading import *



class App(object):

    def __init__(self, numberOfSwitches):

        self.zoneList = []
        
        
        for x in range (0,numberOfSwitches):
            self.zoneList.append(Zone(x))      
        
    def tick(self):
        global time1
        # get the current local time from the PC
        time2 = datetime.now()
        timeString = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            clock.config(text=timeString)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky

        #for x in range (1,app.numberOfSwitches):
            #print (x)

        clock.after(200, self.tick)

    def clearAll(self):
        for x in range(0,len(super.zoneList)):
            zoneList[x].clearZone()

            
    def check(self):

        #ctime = time.strptime("%H:%M:%S")

        myHour= gmtime().tm_hour - 7
        if myHour < 0:
            myHour += 24

            
        for x in range(0,len(self.zoneList)):
            if self.zoneList[x].isAuto() == True:

                if (myHour >= self.zoneList[x].startTime and myHour <= self.zoneList[x].endTime):

                    #print(self.zoneList[x].isOn())
                    
                    if self.zoneList[x].isOn() == False:
                        
                        print("Zone " + str(self.zoneList[x].id) + " scheduled to be on between " + str(self.zoneList[x].startTime) + " and " + str(self.zoneList[x].endTime) + " - Current time : " + str(myHour))
                        
                        self.zoneList[x].switchOn()
                
                else:
                    if self.zoneList[x].isOn() == True:
                        print("Zone " + str(self.zoneList[x].id) + " scheduled to be on between " + str(self.zoneList[x].startTime) + " and " + str(self.zoneList[x].endTime) + " - Current time : " + str(myHour))
                        self.zoneList[x].switchOff()

                    
            #print(self.zoneList[x].startTime)
            #print(myHour)
            #print(self.zoneList[x].isOn())

        clock.after(200, self.check)


        

# Each zone contains buttons, methods, and properties relating to controlling each irrigation zone
class Zone(App):
    
    def __init__(self,i):
        
        self.on = bool
        self.id = int
        self.auto = bool
        
        self.startTime = time()
        self.EndTime = time()

        self.startTime = 18
        self.endTime = 20
        
        self.on = False
        self.id = i
        self.auto = False
        
        frame = Frame(root)

        self.drawZone()
        self.switchOff()
        
        
        return None

    def drawZone(self):
        
        frame = Frame(root)
        
        self.labelZone = Label(frame, text='Zone '+ str(self.id), font=(None,18)).grid(row=self.id, column=0)
        
        self.buttonOn = Button(frame, text='On', font=(None,18), command=self.switchManualOn)
        self.buttonOff = Button(frame, text='Off', font=(None,18), command=self.switchManualOff)
        self.buttonAuto = Button(frame, text='Auto', font=(None,18), command=self.switchAuto)
        self.buttonConfig = Button(frame, text='...', font=(None,18), command=self.config)
        
        
        self.buttonOn.grid(row=self.id, column=2)
        
        self.buttonOff.grid(row=self.id, column=3)
        self.buttonAuto.grid(row=self.id, column=4)
        self.buttonConfig.grid(row=self.id, column=5)

        self.buttonAuto.configure(bg = "Light Grey")

        frame.pack()
        
    def clearZone(self):

        self.buttonOn.grid_forget()
        self.buttonOff.grid_forget()
        self.buttonAuto.grid_forget()
        self.buttonConfig.grid_forget()
        #self.labelZone.grid_forget()

        
    def drawConfig(self):

        self.clearAll()
        frame = Frame(root)
        
        Label(frame, text='Set Schedule for Zone '+ str(self.id), font=(None,18)).grid(row=1, columnspan=5)
        Label(frame, text='12 ', font=(None,18)).grid(row=5, column=3)
        Label(frame, text=': 00', font=(None,18)).grid(row=5, column=4)
        
        self.buttonHourUp = Button(frame, text='UP', font=(None,18), command=self.buttonHourUp)
        self.buttonHourDown = Button(frame, text='DOWN', font=(None,18), command=self.buttonHourDown)
        self.buttonMinuteUp= Button(frame, text='UP', font=(None,18), command=self.buttonMinuteUp)
        self.buttonMinuteDown = Button(frame, text='DOWN', font=(None,18), command=self.buttonMinuteDown)

        self.buttonMinuteDown = Button(frame, text='DONE', font=(None,18), command=self.buttonDone)

        self.buttonHourUp.grid(row=4, column=3)
        self.buttonHourDown.grid(row=6, column=3)
        self.buttonMinuteUp.grid(row=4, column=4)
        self.buttonMinuteDown.grid(row=6, column=4)
        self.buttonDone.grid(row=7, column=1, columnspan=5)

        frame.pack()

    def clearAll(self):
        super(Zone, self).clearAll()
        
    def buttonDone(self):
        self.clearAll()
        
    def buttonHourUp(self):
        print("Hour Up")

    def buttonHourDown(self):
        print("Hour Down")

    def buttonMinuteUp(self):
        print("Minute Up")

    def buttonMinuteDown(self):
        print("Minute Down")
        
    def flip_switch1(self):
        if self.on == 0:
            self.switchOn()
        else:
            self.switchOff()
            
    def switchManualOn(self):
        self.on = True
        self.auto = False
        self.buttonAuto.configure(bg = "Light Grey")
        self.switchOn()

    def switchManualOff(self):
        self.on = False
        self.auto = False
        self.buttonAuto.configure(bg = "Light Grey")
        self.switchOff()
        
    def switchOn(self):
        self.on = True
        print('Switch ' + str(self.id) + ' is now ON')
        self.buttonOn.configure(bg = "Lime Green")
        self.buttonOff.configure(bg = "Light Grey")

    def switchOff(self):
        self.on = False
        print('Switch ' + str(self.id) + ' is now OFF')
        self.buttonOff.configure(bg = "red")
        self.buttonOn.configure(bg = "Light Grey")

    def switchAuto(self):
        if self.auto == True:
            
            self.auto = False
            print('Switch ' + str(self.id) + ' is now set to manual')
            self.buttonAuto.configure(bg = "Light Grey")

        else:
            
            self.auto = True
            print('Switch ' + str(self.id) + ' is now set to Automatic')
            self.buttonAuto.configure(bg = "Lime Green")
        #root.clock.configure(bg = "green")
            
    def config(self):
        print("Config " + str(self.id))
        self.drawConfig()
        

    def getStartTime(self):
        return self.startTime

    def isOn(self):
        if self.on == False:
            return False
        else:
            return True
        
    def isAuto(self):
        if self.auto == False:
            return False
        else:
            return True

                
    #print(str(zoneList[0].id))




root = Tk()
root.wm_title('Home Automation')
time1 = ''

root.geometry('{}x{}'.format(480, 320))

clock = Label(root, font=('times', 20, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)

# Define number of switches here
# Maximum is 6
numberOfSwitches = int
numberOfSwitches = 5

# Don't allow more than 6 switches
if numberOfSwitches > 6:
    numberOfSwitches = 6

app = App(numberOfSwitches)
    
#Switch #1

root.after(1000,app.tick())
root.after(2000,app.check())



root.mainloop()
