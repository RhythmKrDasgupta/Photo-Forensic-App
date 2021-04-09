
# image metadata viewer
# image compare
# Meta Data Write
# pyqt
# date: 20TH feb 2020

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import time
from tkinter import *

import sys
from PyQt5.QtWidgets import *

import os.path
from PIL.ExifTags import TAGS, GPSTAGS
import os
import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PIL import Image, ImageChops
import time
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys

import hashlib
BLOCKSIZE = 58648
hasher = hashlib.md5()


class Ui_MainWindow(object):
    def click(self, eve):
        print("clicked")
        self.compare1()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1158, 749)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setAutoFillBackground(False)


        # BG COLOR
        MainWindow.setStyleSheet("background-color: #181818")

        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setAcceptDrops(True)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(4)
        self.scrollArea.setMidLineWidth(6)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1127, 690))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.plain_meta1 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plain_meta1.setGeometry(QtCore.QRect(430, 340, 281, 311))
        self.plain_meta1.setMouseTracking(True)
        self.plain_meta1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plain_meta1.setOverwriteMode(True)
        self.plain_meta1.setBackgroundVisible(False)
        self.plain_meta1.setCenterOnScroll(True)
        self.plain_meta1.setPlaceholderText("")
        self.plain_meta1.setObjectName("plain_meta1")




        self.compare = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.compare.setGeometry(QtCore.QRect(100, 400, 291, 261))
        self.compare.setMouseTracking(True)
        self.compare.setAcceptDrops(True)
        self.compare.setAutoFillBackground(False)
        self.compare.setFrameShape(QtWidgets.QFrame.Box)
        self.compare.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.compare.setLineWidth(4)
        self.compare.setMidLineWidth(6)
        self.compare.setPixmap(QtGui.QPixmap("logo2.jpg"))
        self.compare.setScaledContents(True)
        self.compare.setWordWrap(True)
        self.compare.setOpenExternalLinks(False)
        self.compare.setObjectName("compare")
        self.l_img2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.l_img2.setGeometry(QtCore.QRect(790, 80, 281, 241))
        self.l_img2.setMouseTracking(True)
        self.l_img2.setTabletTracking(True)
        self.l_img2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.l_img2.setAcceptDrops(True)
        self.l_img2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.l_img2.setAutoFillBackground(False)
        self.l_img2.setFrameShape(QtWidgets.QFrame.Box)
        self.l_img2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.l_img2.setMidLineWidth(1.5)
        #self.l_img2.setLineWidth(6)
        self.l_img2.setContentsMargins(3, 3, 3, 3)
        self.l_img2.setStyleSheet("background-color:#0066CC")


        self.l_img2.setText("")
        self.l_img2.setPixmap(QtGui.QPixmap("logo1.jpg"))

        self.l_img2.setScaledContents(True)
        self.l_img2.setObjectName("l_img2")
        self.l_img1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.l_img1.setGeometry(QtCore.QRect(430, 80, 281, 241))
        self.l_img1.setMouseTracking(True)
        self.l_img1.setTabletTracking(True)
        self.l_img1.setAcceptDrops(False)
        self.l_img1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.l_img1.setAutoFillBackground(False)
        self.l_img1.setFrameShape(QtWidgets.QFrame.Box)
        self.l_img1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.l_img1.setMidLineWidth(1.5)
        #self.l_img1.setLineWidth(1)
        self.l_img1.setContentsMargins(3, 3, 3, 3)
        self.l_img1.setStyleSheet("background-color: #0066CC")

        self.l_img1.setText("")
        self.l_img1.setPixmap(QtGui.QPixmap("logo1.jpg"))
        self.l_img1.setScaledContents(True)
        self.l_img1.setObjectName("l_img1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 70, 171, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.b_img2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_img2.setObjectName("b_img2")
        self.verticalLayout_2.addWidget(self.b_img2)
        self.b_img1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_img1.setAutoDefault(True)
        self.b_img1.setObjectName("b_img1")
        self.verticalLayout_2.addWidget(self.b_img1)
        self.b_img2.clicked.connect(self.openimg1)#first image load
        self.b_img1.clicked.connect(self.openimg2)



        self.b_com = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_com.setObjectName("b_com")
        self.b_com.clicked.connect(self.compare1)

        self.verticalLayout_2.addWidget(self.b_com)
        self.b_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_exit.setStyleSheet("")
        self.b_exit.setObjectName("b_exit")
        self.verticalLayout_2.addWidget(self.b_exit)
        self.b_exit.clicked.connect(self.saveexit)

        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(620, 10, 241, 51))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)



        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(1)

        #self.l_img1.setLineWidth(1)
        self.label.setContentsMargins(1, 1, 1, 1)
        self.label.setStyleSheet("background-color: #0066CC")


        self.label.setObjectName("label")
        self.plain_meta2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plain_meta2.setGeometry(QtCore.QRect(790, 340, 281, 311))
        self.plain_meta2.setMouseTracking(True)
        self.plain_meta2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plain_meta2.setOverwriteMode(True)
        self.plain_meta2.setBackgroundVisible(False)
        self.plain_meta2.setCenterOnScroll(True)
        self.plain_meta2.setPlaceholderText("")
        self.plain_meta2.setObjectName("plain_meta2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(150, 330, 171, 41))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 9pt \"MS UI Gothic\";")
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color: #0066CC;font: 9pt \"MS UI Gothic\";")
        self.label_2.mousePressEvent = self.click

        self.l_img1.setAcceptDrops(True)
        #self.l_img1.setDragEnabled(True)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1158, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def openimg2(self):
        try:
            print("Inside Open File-openimg2openimg2")
            file_name = self.browsefile()
            dirname, basename = os.path.split(file_name)
            self.base2 = basename
            self.l_img2.setPixmap(QtGui.QPixmap(file_name))
            self.l_img2.setScaledContents(1)
            hash=self.get_hash(file_name)
            labeled=self.get_labeled(file_name)
            latlong=self.get_latlong(file_name)
            #print(latlong)
            if latlong:
                labeled.update(latlong)
            labeled.update({"HASH-5": hash})
            #print(labeled,type(labeled))
            filter_data = self.filter_labeldata(labeled)
            #self.plain_meta2.setPlainText(filter_data)
            myFont = QtGui.QFont()
            myFont.setBold(True)
            self.plain_meta2.setFont(myFont)

            filter_data=self.filter_labeldata(labeled)
            self.plain_meta2.setPlainText(filter_data)
            self.plain_meta2.setStyleSheet('color: White')


            #self.plain_meta2.appendPlainText("fsdgfkgdfg mdbf")
        except:
            print("hiii")
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oh no!!!!!This is not an image.May be image document or other file')
            error_dialog.exec()

    def get_hash(self,file_name):
        try:
            h = hashlib.sha1()
            with open(file_name, 'rb') as file:
                chunk = 0
                while chunk != b'':
                    chunk = file.read(1024)
                    h.update(chunk)

            return h.hexdigest()
        except:
            print("exception!!! problrm in hash file")

    def get_latlong(self,file_name):
        try:
            i = Image.open(file_name)
            info = i._getexif()
            geotags={}
            if (info != None):
                geotags = self.get_geotagging(info)
            if geotags:
                print("geotagiing")
                latlong = self.get_coordinates(geotags)
                return latlong
        except:
            return 0
            #labeled.update(latlong)

    def get_labeled(self,file_name):
        hash = self.get_hash(file_name)
        i = Image.open(file_name)
        info = i._getexif()
        labeled = {}
        labeled.update({"File Path": file_name})
        kb = format(os.path.getsize(file_name) / 1024, '.2f')
        mb = format(os.path.getsize(file_name) / 1048576, '.2f')
        labeled.update({"Size(KB)": kb})
        labeled.update({"Size(MB)": mb})
        labeled.update({"HASH-5": hash})

        labeled.update({"                Exif ": "MetaData Details"})
        try:
            if(info!=None):
                 for (key, val) in info.items():
                     labeled[TAGS.get(key)] = val
            else:

                print('File         :', file_name)
                print('Modified time:', time.ctime(os.path.getmtime(file_name)))
                print('Size        :', format(os.path.getsize(file_name) / 1024, '.2f'), "KB  /",format(os.path.getsize(file_name) / 1048576, '.2f'), "MB")


                labeled.update({"Created": time.ctime(os.path.getctime(file_name))})
                labeled.update({"Modified": time.ctime(os.path.getmtime(file_name))})





            dirname, basename = os.path.split(file_name)
            f = open(basename + '.txt', 'w+')
            f.write(" ################################################################## \n")
            f.write(" IMAGE METADATA DETAILS \n \n")
            for i in labeled:
                print(i, ' : ', labeled[i])
                labeled[i] = str(labeled[i])
                f.write(i)
                f.write("   :     ")
                f.write(labeled[i])
                f.write("\n")
        except:
            print("Exception 1 Read ")

        return labeled
    def openimg1(self):
        try:
            print("Inside Open File-openimg1openimg1")
            file_name = self.browsefile()
            dirname, basename = os.path.split(file_name)
            self.base1 = basename
            self.l_img1.setPixmap(QtGui.QPixmap(file_name))
            self.l_img1.setScaledContents(1)
            #hash=self.get_hash(file_name)
            labeled=self.get_labeled(file_name)
            latlong=self.get_latlong(file_name)
            #print(latlong)
            if latlong:
                labeled.update(latlong)
            #labeled.update({"HASH-5": hash})
            #print(labeled,type(labeled))

            myFont = QtGui.QFont()
            myFont.setBold(True)
            self.plain_meta1.setFont(myFont)




            filter_data=self.filter_labeldata(labeled)
            self.plain_meta1.setPlainText(filter_data)
            self.plain_meta1.setStyleSheet('color: White')

        except:
            print("Exception inside open img")
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oh no!!!!!This is not an image.May be image document or other file ')
            error_dialog.exec()

    def filter_labeldata(self,labeled):
        key1 = ""
        for key, value in labeled.items():
            if (str(key) != "ComponentsConfiguration" and str(key) != "GPSInfo" and
                    str(key) != "FlashPixVersion" and str(key) != "ExifVersion" and
                    str(key) != "SubjectDistanceRange" and str(key) != "FileSource" and
                    str(key) != "SceneType" and str(key) != "YResolution" and str(key)!="ExposureProgram" and
            str(key)!="MakerNote" and str(key)!="None" and str(key)!="XPAuthor" and str(key)!="ExifOffset"
                    and str(key) != "SubsecTimeOriginal" and str(key)!="SubsecTimeDigitized"):
                if str(key)=="DateTimeOriginal":
                    key="Created Date"
                if str(key)=="DateTimeDigitized":
                    key="Modified Date"
                if str(key)=="Make":
                    key="Device Name"
                if str(key)=="Flash":
                    key="Flash Fired "
                    if value=="0":
                        value="NO"
                    else:
                        value="YES"
                if str(key)=="ApertureValue":
                    key="Brightness of the image that passes through the lens and falls on the image sensor."
                if str(key)=="LightSource":
                    key="LightSource "
                    if value=="2":
                        value="Unknown "
                    elif value=="1":
                        value="Daylight "
                    else:
                        value="Unknown"
                if str(key) == "FocalLength":
                    key = " Focal length of lens"
                key1 += str(key) + ":   " + str(value) + "\n\n"
            # if (str(key) == "DateTimeOriginal" or str(key) == "DateTimeDigitized" or
            #         str(key) == "Latitude" or str(key) == "Longitude" or
            #         str(key) == "DateTime" or str(key) == "Model" or
            #         str(key) == "Make" or str(key) == "ImageLength" or str(key)=="HASH-5" or
            # str(key)=="Software" or str(key)=="ImageWidth"):
            #     key1 += str(key) + ":   " + str(value) + "\n \n"
        return key1


    def get_coordinates(self,geotags):
        latlong = {}
        print(geotags)
        if (geotags !=None):
            print("latttttttt")
            GPSLatitude =self.get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
            GPSLongitude =self.get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
            latlong['Latitude'] = GPSLatitude
            latlong['Longitude'] = GPSLongitude
            return latlong
    def get_decimal_from_dms(self,dms, ref):

        degrees = dms[0][0] / dms[0][1]
        minutes = dms[1][0] / dms[1][1] / 60.0
        seconds = dms[2][0] / dms[2][1] / 3600.0

        if ref in ['S', 'W']:
            degrees = -degrees
            minutes = -minutes
            seconds = -seconds
        return round(degrees + minutes + seconds, 5)



    def get_geotagging(self,exif):
        geotagging = {}
        if not exif:
            #raise ValueError("No EXIF metadata found"
            return geotagging

        #geotagging = {}
        for (idx, tag) in TAGS.items():
            if tag == 'GPSInfo':
                if idx not in exif:
                    raise ValueError("No EXIF geotagging found")
                for (key, val) in GPSTAGS.items():
                    if key in exif[idx]:
                        geotagging[val] = exif[idx][key]

        return geotagging

    def browsefile(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                      "All Files (*);;Python Files (*.py)",options=options)
            #filename =QFileDialog.getOpenFileName()
            #path = filename[0]
            print("dhdhdh hhgdgd hddgd gdghd hgdh",fileName)
            return fileName
        except:
            print("Browse file exception")

    def saveexit(self):
        print("exit.......")
        QApplication.exit()


    def compare1(self):
        print("hiii")
        try:
            print("inside compare")
            image_one =self.base1
            image_two =self.base2
            image_one = Image.open(image_one)
            image_two = Image.open(image_two)
            diff = ImageChops.difference(image_one, image_two)
            if diff.getbbox():
                diff.save('p.jpg')
                print("hiiiiiiiiiiiiii")
            self.compare.setPixmap(QtGui.QPixmap("p.jpg"))
            self.compare.setScaledContents(1)
        except:
            print("compare1 exception")
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oh no!!!!!Comparing not possible')
            error_dialog.exec()








    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


        self.b_img2.setText(_translate("MainWindow", "Browse Image"))
        self.b_img1.setText(_translate("MainWindow", "Browse Image"))
        self.b_com.setText(_translate("MainWindow", "Compare"))
        self.b_exit.setText(_translate("MainWindow", "Export & Exit"))

        self.b_img2.setStyleSheet('QPushButton {background-color: #0066CC; color: White;}')
        self.b_img1.setStyleSheet('QPushButton {background-color: #0066CC; color: White;}')
        self.b_com.setStyleSheet('QPushButton {background-color: #0066CC; color: White;}')
        self.b_exit.setStyleSheet('QPushButton {background-color: #0066CC; color: White;}')


        #self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#FFFFFF;\">IMAGE DETAILS</span></p></body></html>"))

        #self.plain_meta2.setPlainText(_translate("MainWindow", "dgfggf"))

        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#FFFFFF;\">IMAGE DETAILS</span></p></body></html>"))

        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;color:#FFFFFF;\">Compare Image</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

