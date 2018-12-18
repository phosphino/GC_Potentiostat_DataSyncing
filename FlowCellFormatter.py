import pandas as pd
from MainWindow import Ui_MainWindow
from dateutil.parser import parse
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import pandas as pd
import shelve
import sys

class FlowCellFormatter(Ui_MainWindow):
    def __init__(self, mainwindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainwindow)

        self.msgbox = QMessageBox()
        self.msgbox.setIcon(QMessageBox.Critical)
        self.msgbox.setWindowTitle("ERROR")
        self.msgbox.setStandardButtons(QMessageBox.Ok)
        self.msgbox.setDefaultButton(QMessageBox.Ok)

        self.R = 82.1 #Ideal Gas Constant (mL atm / k mol)


        self.constants = shelve.open('Constants')
        self.calibrationslope_Edit.setText(str(self.constants['Calibration Slope']))
        self.flowrate_Edit.setText(str(self.constants['Flow Rate']))
        self.temperature_Edit.setText(str(self.constants['Temperature']))
        self.constants.close()

        #Data Required For Formatting
        self.__gcdataframe = None
        self.__dateState = Qt.Checked
        self.__potentiostat_TotalSeconds = None
        self.__calibration_slope = None
        self.__flow_rate = None
        self.__temperature = None
        self.__baseline = None
        self.__export_filename = None
        #

        self.GCFile_button.clicked.connect(self.openGC)
        self.timeEdit.timeChanged.connect(self.updatepotentiostatTime)
        self.GCPot_syncingBox.stateChanged.connect(self.updatedateState)
        self.Format_button.clicked.connect(self.formatData)

        self.updatepotentiostatTime()
        self.dateEdit.setDate(QDate.currentDate())

    def updatedateState(self, state):
        self.__dateState = state
        if self.__dateState == Qt.Checked:
            self.dateEdit.setEnabled(False)
            self.startdate_label.setEnabled(False)
        else:
            self.dateEdit.setEnabled(True)
            self.startdate_label.setEnabled(True)

    def formatData(self):
        try:
            self.__calibration_slope = self.calibrationslope_Edit.text()
            _ = float(self.__calibration_slope)
        except:
            self.error_msg("Calibration slope")
            return

        try:
            self.__flow_rate = self.flowrate_Edit.text()
            _ = float(self.__flow_rate)
        except:
            self.error_msg("Flow rate")
            return

        try:
            self.__temperature = self.temperature_Edit.text()
            _ = float(self.__temperature)
        except:
            self.error_msg("Temperature")
            return

        try:
            self.__baseline = self.baseline_Edit.text()
            _ = float(self.__baseline)
        except:
            self.error_msg("Baseline")
            return

        self.constants = shelve.open('Constants')
        self.constants['Calibration Slope'] = self.__calibration_slope
        self.constants['Flow Rate'] = self.__flow_rate
        self.constants['Temperature'] = self.__temperature
        self.constants.close()

        if self.__gcdataframe is None:
            return

        gcstarttime, gcstartdate = self.__gcdataframe.iloc[0, 2].split()

        potentiostat_date = self.dateEdit.date().toString(Qt.ISODate)
        potentiostat_time = self.timeEdit.time().toString()

        if self.__dateState == Qt.Checked:
            potentiostat_start = gcstartdate + " " + potentiostat_time
            potentiostat_timestamp = datetime.strptime(potentiostat_start, "%y/%m/%d %H:%M:%S")

        else:
            potentiostat_start = potentiostat_date + " " + potentiostat_time
            potentiostat_timestamp = datetime.strptime(potentiostat_start, "%Y-%m-%d %H:%M:%S")

        self.__potentiostat_TotalSeconds = potentiostat_timestamp.timestamp()
        print(self.__potentiostat_TotalSeconds)

        self.__gcdataframe['Corrected Time'] = self.__gcdataframe["Inject Time"].apply(self.convert_to_seconds)
        self.__gcdataframe['Corrected Area'] = self.__gcdataframe["Area"].apply(self.correct_area)
        self.__gcdataframe['Rate (mole / sec)'] = self.__gcdataframe["Corrected Area"].apply(self.convert_to_rate)
        print(self.__gcdataframe)
        self.__gcdataframe.to_csv(self.__export_filename, index=False)

    def error_msg(self, msg):
        msg = msg+" must be a non-zero number!"
        self.msgbox.setText(msg)
        self.msgbox.exec_()

    def correct_area(self, area):
        try:
            return float(area) - float(self.__baseline)
        except:
            return None

    def convert_to_rate(self, area):
        try:
            area = float(area)
        except ValueError:
            return ""
        calibration_slope = float(self.__calibration_slope)
        flow_rate = float(self.__flow_rate)/60.0 #Convert mL / min to mL / sec
        temperature = float(self.__temperature) + 273.15

        try:
            rate = (area * flow_rate) / (calibration_slope * self.R * temperature*100.0)
        except:
            rate = ""
        return rate

    def convert_to_seconds(self, timestamp):
        try:
            injection_timestamp = datetime.strptime(timestamp, "%H:%M:%S %y/%m/%d").timestamp()
            return injection_timestamp - self.__potentiostat_TotalSeconds
        except:
            return ""

    def updatepotentiostatTime(self):
        self.__potentiostatTime = self.timeEdit.time().toString().split(":")
        self.__potentiostatTime = [int(x) for x in self.__potentiostatTime]

    def openGC(self):
        fname, check = QFileDialog.getOpenFileName(None, "Select GC Data File", 'C:\\', "xlsx (*.xlsx)")
        print(fname, check)
        if fname == "":
            return
        gcdf = pd.read_excel(fname, skiprows=13)

        gcfilename = fname.split(".")[0]
        self.__export_filename = gcfilename+"_Formatted.csv"
        headers = ["Injection #", "Injection", "Retention Time", "Area", "Height", "Inject Time", "Amount",
                   "Relative Area", "Peak Type"]

        gcdf.columns = headers
        self.__gcdataframe = gcdf.filter(["Injection #", "Area", "Inject Time"], axis=1)
        self.GCFile_label.setText(fname)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    program = FlowCellFormatter(window)
    window.show()
    sys.exit(app.exec_())
