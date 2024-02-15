from persiantools.jdatetime import JalaliDateTime
from datetime import date
from datetime import datetime
import pytz

class dateSet:
  def __init__(self,QtwidgetDate,QtwidgetTime) -> None:
    self.QtwidgetDate=QtwidgetDate
    self.QtwidgetTime=QtwidgetTime

  def DateSetter(self):
        TheDate=JalaliDateTime.now().strftime("yyyy/mm/dd")
        year=JalaliDateTime.now().year
        month=JalaliDateTime.now().month
        day=JalaliDateTime.now().day
        
        #    self.Qtwidget.setDisplayFormat("yyyy/mm/dd")   

        #    qdate = QtCore.QDate.fromString(TheDate, "yyyy/mm/dd")


        #    qdate = date(year,month,day)

        # d = QDate((2020-622), 14, 3)

        # self.Qtwidget.setDate(d)

#   def timeSetter(self):
  
  def timesetter(self):
        Tehran = pytz.timezone("Asia/Tehran") 
        timeInNewYork = datetime.now(Tehran)
        currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")
        print(currentTimeInNewYork)
        self.QtwidgetTime.setTime(currentTimeInNewYork)
     
     



