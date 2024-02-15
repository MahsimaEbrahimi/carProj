from persiantools.jdatetime import JalaliDateTime
from PyQt5 import QtCore, QtWidgets
from datetime import date
class dateSet:
  def __init__(self,Qtwidget) -> None:
    self.Qtwidget=Qtwidget

  def DateSetter(self):
   TheDate=JalaliDateTime.now().strftime("yyyy/mm/dd")
   year=JalaliDateTime.now().year
   month=JalaliDateTime.now().month
   day=JalaliDateTime.now().day
   
   self.Qtwidget.setDisplayFormat("yyyy/mm/dd")   

#    qdate = QtCore.QDate.fromString(TheDate, "yyyy/mm/dd")


   qdate = date(year,month,day)

   self.Qtwidget.setCalendar(qdate)


