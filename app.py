# Things to do for project demo:
""" Five tests for the (5) functional requirements """

import sys
from PyQt6 import QtWidgets, uic
from PyQt6 import QtCore
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QComboBox, QListWidget, QPushButton, QLineEdit, QDateEdit, QCheckBox, QMessageBox, QDateEdit, QRadioButton, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6 import uic
from datetime import datetime
import pyodbc

server = 'HU-DOPX-GCL10\MSSQLSERVER01'
database = 'Northwind(ms08066)'  # Name of your Northwind database
use_windows_authentication = False  # Set to True to use Windows Authentication
username = 'sa'  # Specify a username if not using Windows Authentication
password = 'Fall2022.dbms'  # Specify a password if not using Windows Authentication

# Create the connection string based on the authentication method chosen
if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
else:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__()

        # Load the .ui file
        uic.loadUi("Landing Page.ui", self)

        # Changing name of MainWindow
        self.setWindowTitle("Dental Clinic Management System")

        self.show()

        # Connecting to the selected login page
        self.loginPatientButton = self.findChild(QPushButton, "loginPatientButton")
        self.loginPatientButton.clicked.connect(self.patientLoginFormLoader)

        self.loginStaffButton = self.findChild(QPushButton, "loginStaffButton")
        self.loginStaffButton.clicked.connect(self.staffLoginFormLoader)

    def patientLoginFormLoader(self):
        self.patientLoginForm = patientLoginForm()
        self.patientLoginForm.show()
        self.close()

    def staffLoginFormLoader(self):
        self.staffLoginForm = staffLoginForm()
        self.staffLoginForm.show()
        self.close()

    """"""
    # Populating all the tables
    """"""
    def populateStaffTable(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # SQL Queries to fetch data
        cursor.execute("select * from staff")
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.staffTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.staffTable.setItem(row_index, col_index, item)

        connection.close()

    def populatePatientsTable(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # SQL Queries to fetch data
        cursor.execute("select * from patients")
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.patientsTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.patientsTable.setItem(row_index, col_index, item)

        connection.close()

    def populatePatientRecordsTable(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # SQL Queries to fetch data
        cursor.execute("select * from patientrecords")
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.patientrecordsTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.patientrecordsTable.setItem(row_index, col_index, item)

        connection.close()

    def populateAppointmentsTable(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # SQL Queries to fetch data
        cursor.execute("select * from appointments")
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.appointmentsTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.appointmentsTable.setItem(row_index, col_index, item)

        connection.close()

    def populateInventoryTable(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # SQL Queries to fetch data
        cursor.execute("select * from inventory")
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.inventoryTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.inventoryTable.setItem(row_index, col_index, item)

        connection.close()

    def populateFeedbackTable(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # SQL Queries to fetch data
        cursor.execute("select * from feedback")
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.feedbackTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.feedbackTable.setItem(row_index, col_index, item)

        connection.close()

    

    

    

    

        


class patientLoginForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(patientLoginForm, self).__init__() 

        # Load the .ui file
        uic.loadUi('Patient Login.ui', self) 

        # Changing name of MainWindow
        self.setWindowTitle("Patient Login Form")

        # Connecting to the registration form
        self.patientloginRegisterButton = self.findChild(QPushButton, "patientloginRegisterButton")
        self.patientloginRegisterButton.clicked.connect(self.patientRegistrationFormLoader)

        # Connecting to the landing page if already registered
        self.patientloginLoginButton = self.findChild(QPushButton, "patientloginLoginButton")
        self.patientloginLoginButton.clicked.connect(self.patientLandingPageLoader)

    def patientRegistrationFormLoader(self):
        self.patientRegistrationForm = patientRegistrationForm()
        self.patientRegistrationForm.show()
        self.close()

    def patientLandingPageLoader(self):
        self.patientLandingPage = patientLandingPage()
        self.patientLandingPage.show()
        self.close()
        

class staffLoginForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(staffLoginForm, self).__init__() 

        # Load the .ui file
        uic.loadUi('Staff Login.ui', self) 

        # Changing name of MainWindow
        self.setWindowTitle("Staff Login Form")

        # Connecting to the registration form
        self.staffloginRegisterButton = self.findChild(QPushButton, "staffloginRegisterButton")
        self.staffloginRegisterButton.clicked.connect(self.staffRegistrationFormLoader)

        self.staffloginLoginButton = self.findChild(QPushButton, "staffloginLoginButton")
        self.staffloginLoginButton.clicked.connect(self.staffLandingPageLoader)

    def staffRegistrationFormLoader(self):
        self.staffRegistrationForm = staffRegistrationForm()
        self.staffRegistrationForm.show()
        self.close()

    def staffLandingPageLoader(self):
        self.staffLandingPage = staffLandingPage()
        self.staffLandingPage.show()
        self.close()


class patientRegistrationForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(patientRegistrationForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Patient Registration Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Patient Registration Form")

        self.patientregistrationSubmitButton = self.findChild(QPushButton, "patientregistrationSubmitButton")
        self.patientregistrationSubmitButton.clicked.connect(self.patientLoginFormLoader)

    def patientLoginFormLoader(self):
        self.patientLoginForm = patientLoginForm()
        self.patientLoginForm.show()
        self.close()


class staffRegistrationForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(staffRegistrationForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Staff Registration Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Staff Registration Form")

        self.staffregistrationSubmitButton = self.findChild(QPushButton, "staffregistrationSubmitButton")
        self.staffregistrationSubmitButton.clicked.connect(self.staffLoginFormLoader)

    def staffLoginFormLoader(self):
        self.staffLoginForm = staffLoginForm()
        self.staffLoginForm.show()
        self.close()


class patientLandingPage(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(patientLandingPage, self).__init__() 

        # Load the .ui file
        uic.loadUi("Patient Landing Page.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Patient Landing Page")

        # Connecting the schedule appointment button
        self.scheduleButton = self.findChild(QPushButton, "scheduleButton")
        self.scheduleButton.clicked.connect(self.appointmentSchedulingFormLoader)

        self.feedbackButton = self.findChild(QPushButton, "feedbackButton")
        self.feedbackButton.clicked.connect(self.feedbackFormLoader)

        self.cancelButton = self.findChild(QPushButton, "cancelButon")
        self.cancelButton.clicked.connect(self.appointCancelFormLoader)

    def appointmentSchedulingFormLoader(self):
        self.appointmentSchedulingForm = appointmentSchedulingForm()
        self.appointmentSchedulingForm.show()
        self.close()

    def feedbackFormLoader(self):
        self.feedbackForm = patientFeedbackForm()
        self.feedbackForm.show()
        self.close()

    def appointCancelFormLoader(self):
        self.appointmentCancelForm = appointmentCancelForm()
        self.appointmentCancelForm.show()
        self.close()


class staffLandingPage(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(staffLandingPage, self).__init__() 

        # Load the .ui file
        uic.loadUi("Staff Landing Page.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Staff Landing Page")

        self.stafflandingInventoryButton = self.findChild(QPushButton, "stafflandingInventoryButton")
        self.stafflandingInventoryButton.clicked.connect(self.inventoryLandingPageLoader)

        self.stafflandingAppointmentButton = self.findChild(QPushButton, "stafflandingAppointmentButton")
        self.stafflandingAppointmentButton.clicked.connect(self.billGenerationFormLoader)

        self.stafflandingPatientRecordButton = self.findChild(QPushButton, "stafflandingPatientRecordButton")
        self.stafflandingPatientRecordButton.clicked.connect(self.patientRecordFormLoader)

        self.stafflandingFinancialRecordsButton = self.findChild(QPushButton, "stafflandingFinancialRecordsButton")
        self.stafflandingFinancialRecordsButton.clicked.connect(self.financialRecordsFormLoader)

    def inventoryLandingPageLoader(self):
        self.inventoryLandingPage = inventoryLandingPage()
        self.inventoryLandingPage.show()
        self.close()

    def billGenerationFormLoader(self):
        self.billGenerationForm = billGenerationForm()
        self.billGenerationForm.show()
        self.close()

    def patientRecordFormLoader(self):
        self.patientRecordForm = patientRecordForm()
        self.patientRecordForm.show()
        self.close()

    def financialRecordsFormLoader(self):
        self.financialRecordsForm = financialRecordsForm()
        self.financialRecordsForm.show()
        self.close()

class appointmentSchedulingForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(appointmentSchedulingForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Appointment Scheduling Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Appointment Scheduling Form")

class appointmentCancelForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(appointmentCancelForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Appointment Canceling Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Appointment Canceling Form")

class inventoryLandingPage(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(inventoryLandingPage, self).__init__() 

        # Load the .ui file
        uic.loadUi("Inventory Landing Page.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Inventory Landing Page")

        self.inventoryLandingAddNewButton = self.findChild(QPushButton, "inventoryLandingAddNewButton")
        self.inventoryLandingAddNewButton.clicked.connect(self.inventoryAddFormLoader)

        self.inventoryLandingUpdateQuantityButton = self.findChild(QPushButton, "inventoryLandingUpdateQuantityButton")
        self.inventoryLandingUpdateQuantityButton.clicked.connect(self.inventoryUpdateFormLoader)

    def inventoryAddFormLoader(self):
        self.inventoryAddForm = inventoryAddForm()
        self.inventoryAddForm.show()
        self.close()

    def inventoryUpdateFormLoader(self):
        self.inventoryUpdateForm = inventoryUpdateForm()
        self.inventoryUpdateForm.show()
        self.close()

class billGenerationForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(billGenerationForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Bill Generation Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Bill Generation Form")

class patientRecordForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(patientRecordForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Patient Records.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Patient Records")

class patientFeedbackForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(patientFeedbackForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Patient Feedback Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Patient Feedback Form")

class inventoryAddForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(inventoryAddForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Inventory Add Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Inventory Add Form")

class inventoryUpdateForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(inventoryUpdateForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Inventory Quantity Update Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Inventory Update Form")

class financialRecordsForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(financialRecordsForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Financial Records Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Financial Records Form")

        self.financialRecordsUpdateStaffSalariesButton = self.findChild(QPushButton, "financialRecordsUpdateStaffSalariesButton")
        self.financialRecordsUpdateStaffSalariesButton.clicked.connect(self.staffInformationUpdateFormLoader)
        
        self.financialRecordsViewMonthlyRecordsButton = self.findChild(QPushButton, "financialRecordsViewMonthlyRecordsButton")
        self.financialRecordsViewMonthlyRecordsButton.clicked.connect(self.monthlyRecordsFormLoader)

    def staffInformationUpdateFormLoader(self):
        self.staffInformationUpdateForm = staffInformationUpdateForm()
        self.staffInformationUpdateForm.show()
        self.close()

    def monthlyRecordsFormLoader(self):
        self.monthlyRecordsForm = monthlyRecordsForm()
        self.monthlyRecordsForm.show()
        self.close()

class staffInformationUpdateForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(staffInformationUpdateForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Staff Salary Update Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Staff Information Update Form")

class monthlyRecordsForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(monthlyRecordsForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Monthly Financial Records.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Monthly Financial Records Form")


app = QtWidgets.QApplication(sys.argv)
window = UI()  # Create an instance of our class
app.exec()  # Start the application
