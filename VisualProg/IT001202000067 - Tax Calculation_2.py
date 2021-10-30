# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:12:44 2021

@author: AnnisaNurdiana and Student ID: 001202000067

How to calculate your tax in Indonesia?
1. We have to know 2 things: Annual Gross Income (AGI) and Non-Taxable Income (NTI)
2. Subtract AGI with NTI (AGI - NTI), then we call it Taxable Income (TI)
3. If TI is less than or equal to 0, then no tax is paid
4. Else, do level slicing based on the amount of TI from this table to get Annual Income Tax (AIT)

FIGURE,
    =============== TABLE OF TAX CALCULATION ===============
    +-------+----------------------------------+-----------+
    | LEVEL |       TI AMOUNT (IDR)            |   TAX (%) |
    |_______|__________________________________|___________|
    |   1.  | <= 50 Million                    |     5%    |
    |   2.  | 50 Million < TI <= 250 Million   |    15%    |
    |   3.  | 250 Million < TI <= 500 Million  |    25%    |
    |   4.  | >500 Million                     |    30%    |
    |_______|__________________________________|___________|

NOTES,
1. Always make sure the order is in AGI first >> then NTI
2. Clue Thousand Separators please open 'Python string format' in the browser
3. Don't save file as Zip or RAR yeah!

"""

from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QStatusBar, QMenuBar,
    QGridLayout, QAction, QFileDialog, QMessageBox, QFontDialog, QColorDialog
)
from PyQt5.QtGui import (QFont, QColor)

class Window(QWidget):
    def __init__(self):
        # other lines above
        QWidget.__init__(self)
        self.resize(450,250)
        self.setWindowTitle('001202000067 - Tax Calculation')
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        # This is for filename
        self.file_name = ''
        
        # Add status bar
        self.statusbar = QStatusBar()
         
        # Add MenuBar        
        self.menubar = QMenuBar()
        # The default menu is usually in Mac OS, 
        # but we don't want to use the one in the OS.
        self.menubar.setNativeMenuBar(False)
        # Display Menu Bar
        self.menubar.show()
        
        # Add menus
        self.file_menu = self.menubar.addMenu('File')
        self.edit_menu = self.menubar.addMenu('Edit')
        self.format_menu = self.menubar.addMenu('Format')
        self.help_menu = self.menubar.addMenu('Help')
        
        self.action_open = QAction('Open', self)
        self.action_open.setShortcut('Ctrl+O')
        self.action_save = QAction('Save', self)
        self.action_save.setShortcut('Ctrl+S')
        self.action_quit = QAction('Quit', self)
        self.action_quit.setShortcut('Ctrl+Q')
        
        self.action_cut = QAction('Cut', self)
        self.action_cut.setShortcut('Ctrl+X')
        self.action_copy = QAction('Copy', self)
        self.action_copy.setShortcut('Ctrl+C')
        self.action_paste = QAction('Paste', self)
        self.action_paste.setShortcut('Ctrl+V')
        self.action_clear = QAction('Clear All', self)
        
        self.action_color = QAction('Color', self)
        self.action_font = QAction('Font', self)
        
        self.action_about = QAction('About', self)
        
        # Link the action to the menu
        self.file_menu.addAction(self.action_open)
        self.file_menu.addAction(self.action_save)
        # To separate (dividing line between open, save, and quit)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.action_quit)
        
        self.edit_menu.addAction(self.action_cut)
        self.edit_menu.addAction(self.action_copy)
        self.edit_menu.addAction(self.action_paste)
        # To separate (dividing line between cut, copy, paste, and clear)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.action_clear)
        
        
        self.format_menu.addAction(self.action_color)
        self.format_menu.addAction(self.action_font)
        
        self.help_menu.addAction(self.action_about)
        
        
        # Empty text editor (make typing) 
        self.tax_editor = QTextEdit()
        
        
        self.layout.addWidget (self.menubar)
        self.layout.addWidget (self.tax_editor)
        self.layout.addWidget (self.statusbar)
        
        # Connect to function   
        self.action_open.triggered.connect(self.open_text)
        self.action_save.triggered.connect(self.save_text)
        self.action_quit.triggered.connect(self.quit)
        
        self.action_cut.triggered.connect(self.editCut)
        self.action_copy.triggered.connect(self.editCopy)
        self.action_paste.triggered.connect(self.editPaste)
        self.action_clear.triggered.connect(self.tax_editor.clear)
        self.action_color.triggered.connect(self.formatColor)
        self.action_font.triggered.connect(self.formatFont)
        self.action_about.triggered.connect(self.about)
        
        # If we want to know how many lines we have written
        self.tax_editor.textChanged.connect(self.show_lines)
        
        
    # Functions inside the Window class
    def save_text(self):
         # 0pen file and save
         # 0pen dialog, filter as .txt
         # To filter save as text >>    
         name, _ = QFileDialog.getSaveFileName( self, 'Save', self.file_name,'TXT(*.txt)')
         
         # dialog exists and file is opening
         if name: 
             # set file name
             self.file_name = name 
             #  'w' >> set to write mode
             file = open(name, 'w') 
             # After that we get the text from editor
             text = self.tax_editor.toPlainText()
             # write to file
             file.write(text)
             # close file >> so files that are opened must be closed
             file.close() 
          
            
    # Similar to the function above (save_text)
    def open_text(self):
         # open file and load
         # open dialog, filter only .txt files, no file name
         name, _ = QFileDialog.getOpenFileName(self, 'Open', '', 'TXT(*.txt)')
         
         # file exists 
         if name: 
             # set file name
             self.file_name = name 
             # set to read mode
             file = open(name, 'r') 
             
             # process file, read and set to text edit widget
             with file: 
                 data = file.read()
                 enter = data.split('\n')
                 self.result_TI = float(enter[0]) - float(enter[1])
                 my_num = self.result_TI
                 
                 # Python string format thounsand separators
                 # To convert float values into commas as thousands separators
                 my_ti = '{:,.2f}'.format(my_num)
                 agi = '{:,.2f}'.format(float(enter[0]))
                 nti = '{:,.2f}'.format(float(enter[1]))
                 
                 # The text editor is empty first then fill in the data
                 self.tax_editor.setPlainText('')
                 self.tax_editor.setPlainText(f'Your Annual Gross Income\t: Rp{str(agi)} \nYour Non-Taxable Income\t: Rp{str(nti)}\nYour Tax Income\t: Rp{str(my_ti)}\nYour Income Tax\t: Rp{str(self.calculate_tax())}')
                 
             # close file
             file.close() 
             
             
    def calculate_tax(self):
        # Declare Percent as:
        percent_level_1 = 0.05
        percent_level_2 = 0.15
        percent_level_3 = 0.25
        percent_level_4 = 0.30
            
        # Income Tax Formula:
        tax_level_1 = self.result_TI * percent_level_1
        tax_level_2 = percent_level_1 * 50000000 + (self.result_TI - 50000000) * percent_level_2
        tax_level_3 = percent_level_1 * 50000000 + percent_level_2 * (250000000 - 50000000) + (
            self.result_TI - 250000000) * percent_level_3
        tax_level_4 = percent_level_1 * 50000000 + percent_level_2 * (250000000 - 50000000) + percent_level_3 * (
            500000000 - 250000000) + (self.result_TI - 500000000) * percent_level_4
            
        # income tax 
        if self.result_TI <= 50000000:
            my_num = tax_level_1
            # Python string format thounsand separators
            my_tax = '{:,.2f}'.format(my_num)
            return my_tax
            
        elif 50000000 < self.result_TI <= 250000000:
            my_num = tax_level_2
            # Python string format thounsand separators
            my_tax = '{:,.2f}'.format(my_num)
            return my_tax
        
                     
        elif 250000000 < self.result_TI <= 500000000:
            my_num = tax_level_3
            # Python string format thounsand separators
            my_tax = '{:,.2f}'.format(my_num)
            return my_tax
            
        elif self.result_TI > 500000000:
            my_num = tax_level_4
            # Python string format thounsand separators
            my_tax = '{:,.2f}'.format(my_num)
            return my_tax
                  
        
    def quit(self):
         # quit application
         QApplication.quit()
         
     
    def about(self):
         # show message dengan message box
         msg = QMessageBox()
         msg.setText('This is a dummy Taxpad')
         msg.exec_()    
              
        
    # Functions inside the Window class
    def show_lines(self):
         # get text
         text = self.tax_editor.toPlainText()
         len_text = len(text.split('\n')) 
         self.statusbar.showMessage('Lines: %s' % str(len_text))
         
         
    def editCut(self):
        self.tax_editor.cut()
    
    def editCopy(self):
        self.tax_editor.copy()
    
    def editPaste(self):
        self.tax_editor.paste()
        
    def formatColor(self):
        color = QColorDialog.getColor(QColor('black'), self, 'Choose Color')
        if color:
            self.tax_editor.setTextColor(color)
        
    def formatFont(self):
        fontTuple = QFontDialog.getFont(QFont('Sans Serif',14), self, 'Choose font')
        if fontTuple[0]:
            self.tax_editor.setCurrentFont(fontTuple[0])

    
app = QApplication([])
window = Window()
window.show()
app.exec_()


        
        
        
        
        
        