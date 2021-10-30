# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 23:01:13 2021

@author: AnnisaNurdiana and Student ID: 001202000067

"""
from PyQt5.QtWidgets import (
QApplication, QWidget, QTableWidget, QTableWidgetItem, QFormLayout, 
QPushButton, QLabel, QDialog, QLineEdit, QGridLayout, QHBoxLayout, QVBoxLayout
)

# ---------------------------------------------------------------------------- 
class AddForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.resize(250,100)
        self.move(220,280)
        self.setWindowTitle('Add New Data')
        
        self.label_1 = QLabel('Name')
        self.subEdit = QLineEdit()
        self.label_2 = QLabel('Score')
        self.gradeEdit = QLineEdit()
        
        grid = QGridLayout()
        grid.addWidget(self.label_1,0,0)
        grid.addWidget(self.subEdit,0,1)
        grid.addWidget(self.label_2,1,0)
        grid.addWidget(self.gradeEdit,1,1)
        
        self.okButton = QPushButton('Ok')
        self.cancelButton = QPushButton('Cancel')
        
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        
        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(hbox)
        self.setLayout(layout)
        
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
        
# ----------------------------------------------------------------------------- 
class Window(QWidget):
    lastRecordNumber = -1
    
    def __init__(self):
        QWidget.__init__(self)
        self.resize(270, 550)
        self.setWindowTitle('GPA Calculation')
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        #----------------------------------------------------------------------
        self.labelResult = QLabel('<h3><font color = gray> Result: </font></h3>')
        self.labelA = QLabel(''); self.labelA_ = QLabel('')
        self.label_B = QLabel(''); self.labelB = QLabel(''); self.labelB_ = QLabel('')
        self.label_C = QLabel(''); self.labelC = QLabel('')
        self.labelD = QLabel(''); self.labelE = QLabel('')
        #----------------------------------------------------------------------
        self.label = QLabel('')
        self.label2 = QLabel('')
        self.label3 = QLabel('')
        
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Name', 'Score'])
        
        self.button_add = QPushButton('Add New Subject')
        self.calcButton = QPushButton('Calculate GPA')
        self.deleteButton = QPushButton('Delete Row')
        self.exitButton = QPushButton('- Exit -')
        
        self.layout.addRow(self.table)
        self.layout.addRow(self.button_add)
        self.layout.addRow(self.calcButton)
        self.layout.addRow(self.deleteButton)
        self.layout.addRow(self.exitButton)
        #-----------------------------
        self.layout.addRow(self.labelResult)
        self.layout.addRow(self.labelA)
        self.layout.addRow(self.labelA_)
        self.layout.addRow(self.label_B)
        self.layout.addRow(self.labelB)
        self.layout.addRow(self.labelB_)
        self.layout.addRow(self.label_C)
        self.layout.addRow(self.labelC)
        self.layout.addRow(self.labelD)
        self.layout.addRow(self.labelE)
        #------------------------------
        self.layout.addRow(self.label)
        self.layout.addRow(self.label2)
        self.layout.addRow(self.label3)
        
        self.button_add.clicked.connect(self.addButtonClick)
        self.calcButton.clicked.connect(self.calculateGPA)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
        self.exitButton.clicked.connect(self.exitButtonClick)
        self.table.itemChanged.connect(self.on_change)
        
    def calculateGPA(self):
        total_index = 0; total_credit = 0; total_gpa = 0
        gradeA = 0; gradeA_ = 0; grade_B = 0; gradeB = 0;gradeB_ = 0
        grade_C = 0; gradeC = 0; gradeD = 0; gradeE = 0
        
        for i in range(0, self.table.rowCount()):
            data = self.table.item(i, 1)
            
            if data:
                self.grade = float(data.text())
                
                if 0 <= self.grade < 55:
                    self.course = 1
                    self.grade = 0.00
                    self.credit = 3
                    self.index = self.grade * self.credit
                    total_index += self.index
                    total_credit += self.credit
                    gradeE += self.course
                    total_gpa = float(total_index)/float(total_credit)
                    
                elif 55 <= self.grade < 60:
                    self.course = 1
                    self.grade = 1.00
                    self.credit = 3.0
                    self.index = self.grade * self.credit
                    total_index += self.index
                    total_credit += self.credit
                    gradeD += self.course
                    total_gpa = float(total_index)/float(total_credit)
                
                elif 60 <= self.grade < 64:
                    self.course = 1
                    self.grade = 2.00
                    self.credit = 3
                    self.index = self.grade * self.credit
                    total_index += self.index
                    total_credit += self.credit
                    gradeC += self.course
                    total_gpa = float(total_index)/float(total_credit)
                
                elif 64 <= self.grade < 67:
                    self.course = 1
                    self.grade = 2.33
                    self.credit = 3
                    self.index = self.grade * self.credit
                    total_index += self.index
                    total_credit += self.credit
                    grade_C += self.course
                    total_gpa = float(total_index)/float(total_credit)
                 
                elif 67 <= self.grade < 70:
                    self.course = 1
                    self.grade = 2.67
                    self.credit = 3
                    self.index = self.grade * self.credit
                    total_index += self.index
                    total_credit += self.credit
                    gradeB_ += self.course   
                    total_gpa = float(total_index)/float(total_credit)
                
                elif 70 <= self.grade < 75:
                    self.course = 1
                    self.grade = 3.00
                    self.credit = 3
                    self.index = self.grade * self.credit
                    total_index += self.index
                    total_credit += self.credit
                    gradeB += self.course
                    total_gpa = float(total_index)/float(total_credit)
                 
                elif 75 <= self.grade < 80:
                    self.course = 1
                    self.grade = 3.33
                    self.credit = 3
                    self.index = self.grade * self.credit
                    total_index += self.index
                    total_credit += self.credit
                    grade_B += self.course 
                    total_gpa = float(total_index)/float(total_credit)
                    
                elif 80 <= self.grade < 85:
                    self.course = 1
                    self.grade = 3.67
                    self.credit = 3
                    self.index = self.grade * self.credit
                    total_index += self.index
                    total_credit += self.credit
                    gradeA_ += self.course
                    total_gpa = float(total_index)/float(total_credit)
                    
                elif 85 <= self.grade <= 100:
                    self.course = 1
                    self.grade = 4.00
                    self.credit = 3
                    self.index = self.grade * self.credit
                    total_index += self.index
                    total_credit += self.credit
                    gradeA += self.course 
                    total_gpa = float(total_index)/float(total_credit)
                
                else:
                    total_index = 'Score only range 0-100'
                    total_credit = 'Error -'
                    total_gpa = 'INVALID'
                    
            
                 
        self.labelA.setText('A \t\t: %d' % gradeA)
        self.labelA_.setText('A- \t\t: %d' % gradeA_)
        self.label_B.setText('B+ \t\t: %d' % grade_B)
        self.labelB.setText('B \t\t: %d' % gradeB)
        self.labelB_.setText('B- \t\t: %d' % gradeB_)
        self.label_C.setText('C+ \t\t: %d' %grade_C)
        self.labelC.setText('C \t\t: %d' % gradeC)
        self.labelD.setText('D \t\t: %d' % gradeD)
        self.labelE.setText('E \t\t: %d' % gradeE)
        #----------------------------------------------------
        self.label.setText('Total Index \t: %s' % total_index)        
        self.label2.setText('Total Credit \t: %s' % total_credit) 
        self.label3.setText('GPA \t\t: %s' % total_gpa)


    def addButtonClick(self):
        if Window.lastRecordNumber == self.table.rowCount()-1:
            self.table.setRowCount(self.table.rowCount()+1)
            
        form = AddForm()
        if form.exec_() == QDialog.Accepted:
            Window.lastRecordNumber += 1
            subject = form.subEdit.text()
            grade = form.gradeEdit.text()
            data = [subject,grade]
            self.addRow(Window.lastRecordNumber, data)           
        
    def addRow(self, row, itemLabels=[]):
        for i in range (2):
            item = QTableWidgetItem()
            item.setText(itemLabels[i])
            self.table.setItem(row, i, item)
    
    def on_change(self, item):
        col = item.column()
        if col == 1 and not item.text().isnumeric():
            item.setText('') # empty cell

            
    def deleteButtonClick(self):
        tableData = []
        for i in range(0, self.table.rowCount()):
            subject = self.table.item(i,0).text()
            grade = self.table.item(i,1).text()
            tableData.append([subject,grade])
            
        row = self.table.currentRow()
        del tableData[row]
        
        Window.lastRecordNumber -= 1
        self.table.clear()
        self.setColumnAndHeaders()
        self.table.setRowCount(len(tableData))
        for i in range (0, len(tableData)):
            data = tableData[i]
            self.addRow(i,data)
            
    def setColumnAndHeaders(self):
        self.table.setColumnCount(2)
        columnHeaders = ['Name','Score']
        self.table.setHorizontalHeaderLabels(columnHeaders)
        
    def exitButtonClick(self):
        self.close()         
#------------------------------------------------------------------------------  
             
app = QApplication([])
window = Window()
window.show()
app.exec_()  
        
        