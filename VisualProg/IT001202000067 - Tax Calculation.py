# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:38 2021

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

"""

from PyQt5.QtWidgets import (
    QApplication, QPushButton, QLabel, QLineEdit, QWidget, QFormLayout
)


# -------------------------------------------------------------------------
# Taxable Income
def calculate_ti(text_widget, num_agi, num_nti):
    if num_agi and num_nti:
        if num_agi.isnumeric() and num_nti.isnumeric():
            # Taxable Income
            # convert to float, reconvert to string and show
            result_ti = float(num_agi) - float(num_nti)
            text_widget.setText(str(result_ti) + "\n" + str(num_agi) + "\n" + str(num_nti))
        else:
            text_widget.setText('Please input only numbers')


# -------------------------------------------------------------------------
# Income Tax
def calculate_it(text_widget, num_agi, num_nti):
    result_TI = float(num_agi) - float(num_nti)

    # Declare Percent as:
    percent_level_1 = 0.05
    percent_level_2 = 0.15
    percent_level_3 = 0.25
    percent_level_4 = 0.30

    # Income Tax Formula:
    tax_level_1 = result_TI * percent_level_1
    tax_level_2 = percent_level_1 * 50000000 + (result_TI - 50000000) * percent_level_2
    tax_level_3 = percent_level_1 * 50000000 + percent_level_2 * (250000000 - 50000000) + (
            result_TI - 250000000) * percent_level_3
    tax_level_4 = percent_level_1 * 50000000 + percent_level_2 * (250000000 - 50000000) + percent_level_3 * (
            500000000 - 250000000) + (result_TI - 500000000) * percent_level_4

    if result_TI <= 50000000:
        text_widget.setText(str(tax_level_1) + "\n" + str(num_agi) + "\n" + str(num_nti))

    elif 50000000 < result_TI <= 250000000:
        text_widget.setText(str(tax_level_2) + "\n" + str(num_agi) + "\n" + str(num_nti))

    elif 250000000 < result_TI <= 500000000:
        text_widget.setText(str(tax_level_3) + "\n" + str(num_agi) + "\n" + str(num_nti))

    elif result_TI > 500000000:
        text_widget.setText(str(tax_level_4) + "\n" + str(num_agi) + "\n" + str(num_nti))


# -------------------------------------------------------------------------
def main():
    app = QApplication([])
    window = QWidget()
    form_layout = QFormLayout()

    label_num_agi = QLabel('Enter Your Annual Gross Income: ')
    num_agi_input = QLineEdit()
    label_num_nti = QLabel('Enter Your Non-Taxable Income: ')
    num_nti_input = QLineEdit()
    button_calculate = QPushButton('Calculate TI')
    button_calculate_it = QPushButton('Calculate IT')

    label_result = QLabel('Your Taxable Income: \nYour Annual Gross Income (AGI): \nYour Non-Taxable Income (NTI): ')
    result_text = QLabel()

    label_result_tax = QLabel('Your Annual Income Tax is: \nYour Annual Gross Income (AGI): \nYour Non-Taxable Income (NTI): ')
    result_text_tax = QLabel()

    button_calculate.clicked.connect(
        lambda: calculate_ti(result_text, num_agi_input.text(), num_nti_input.text())
    )
    button_calculate_it.clicked.connect(
        lambda: calculate_it(result_text_tax, num_agi_input.text(), num_nti_input.text())
    )

    form_layout.addRow(label_num_agi, num_agi_input)
    form_layout.addRow(label_num_nti, num_nti_input)
    form_layout.addRow(button_calculate)
    form_layout.addRow(label_result, result_text)
    form_layout.addRow(button_calculate_it)
    form_layout.addRow(label_result_tax, result_text_tax)

    window.setLayout(form_layout)
    window.show()
    app.exec_()

main()
