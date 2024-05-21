# Things to do for project demo:
""" Five tests for the (5) functional requirements """
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

# Replace these with your own database connection details
server = 'SHAYAANSLAPTOP'
database = 'DB03'  # Name of your Northwind database
use_windows_authentication = True  # Set to True to use Windows Authentication
# username = 'your_username'  # Specify a username if not using Windows Authentication
# password = 'your_password'  # Specify a password if not using Windows Authentication


# Create the connection string based on the authentication method chosen
if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
# else:
#     connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

import sys
from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QComboBox, QListWidget, QPushButton, QLineEdit, QDateEdit, QCheckBox, QMessageBox, QDateEdit, QRadioButton
from PyQt6 import uic
from datetime import datetime

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
        # self.patientloginLoginButton = self.findChild(QPushButton, "patientloginLoginButton")
        # self.populate_table()
        # self.patientloginLoginButton.clicked.connect(self.patientLandingPageLoader)
        self.patientloginLoginButton.clicked.connect(self.populate_table)
    def populate_table(self):
        connection = pyodbc.connect(
            connection_string
        )
        
        cursor = connection.cursor()
        self.patientloginLoginButton = self.findChild(QPushButton, "patientloginLoginButton")
        line_edit = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        if line_edit is not None:
            entered_id = line_edit.text()
        else:
            entered_id=""
            print("Error: QLineEdit with name 'lineEdit' not found.")        
        
        password_edit = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        if password_edit is not None:
            entered_password = password_edit.text()
        else:
            print("Error: QLineEdit with name 'lineEdit_2' not found.")
            entered_password=""
            # Handle the error as needed        
        # Query to check if the entered ID and password exist in the database
        query = "SELECT * FROM PATIENTS WHERE Email = ? AND Password = ?"
        cursor.execute(query, (entered_id, entered_password))

        result = cursor.fetchone()

        if result:
            # self.patientloginLoginButton.clicked.connect(self.patientLandingPageLoader)
            self.patientLandingPageLoader()
            # Add code to open the main application window or perform other actions
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid ID or password. Please try again.")


        # Close the database connection
        connection.close()
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
        self.staffloginLoginButton.clicked.connect(self.populate_staff_table)
    def populate_staff_table(self):
        connection = pyodbc.connect(
            connection_string
        )
        
        cursor = connection.cursor()
        self.patientloginLoginButton = self.findChild(QPushButton, "staffloginLoginButton")
        line_edit = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        if line_edit is not None:
            entered_id = line_edit.text()
        else:
            entered_id=""
            print("Error: QLineEdit with name 'lineEdit' not found.")        
        
        password_edit = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        if password_edit is not None:
            entered_password = password_edit.text()
        else:
            print("Error: QLineEdit with name 'lineEdit_2' not found.")
            entered_password=""
            # Handle the error as needed        
        # Query to check if the entered ID and password exist in the database
        query = "SELECT * FROM STAFF WHERE Email = ? AND Password = ?"
        cursor.execute(query, (entered_id, entered_password))

        result = cursor.fetchone()

        if result:
            self.staffLandingPageLoader()
            # Add code to open the main application window or perform other actions
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid ID or password. Please try again.")


        # Close the database connection
        connection.close()
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
        self.SubmitButton= self.findChild(QPushButton,"pushButton")
        self.SubmitButton.clicked.connect(self.add_appointment)
    def add_appointment(self):
        # Assuming you have these values available
        # appointment_id = self.appointmentIdLineEdit.text()
        lineEdit_2 = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        patient_id = lineEdit_2.text()
        lineEdit_8 = self.findChild(QtWidgets.QLineEdit, "lineEdit_8")
        treatment_type = lineEdit_8.text()
        lineEdit_10 = self.findChild(QtWidgets.QLineEdit, "lineEdit_10")
        additional_notes = lineEdit_10.text()
        dateEdit=self.findChild(QtWidgets.QDateEdit,"dateEdit")
        timeEdit=self.findChild(QtWidgets.QTimeEdit,"timeEdit")
        date1= dateEdit.date()
        date = date1.toString("yyyy-MM-dd")

        time1=timeEdit.time()
        time_hour = time1.hour()
        time_minute = time1.minute()
        time_second = time1.second()

        # Format the components into a string in HH:mm:ss format
        time = "{:02d}:{:02d}:{:02d}".format(time_hour, time_minute, 00)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("SELECT TOP 1 Appointment_ID FROM [APPOINTMENTS] ORDER BY Appointment_ID DESC")
        id=cursor.fetchone()
        idnew=id[0]
        # print(lineEdit_2)
        # Assuming the table name is '[APPOINTMENTS - Sheet1]'
        sql_query = """INSERT INTO [APPOINTMENTS] (Appointment_ID,Status,Patient_ID, Appointment_Date, Appointment_Time, Treatment_Type, Additional_Notes, Bill) VALUES ( ?,'Present','?',?, ?, ?, ?, ?)"""
        # values = (patient_id, treatment_type, additional_notes,date,time)

        if patient_id!="" and treatment_type!="" and additional_notes!="":
            cursor.execute(sql_query,  (int(idnew)+1,patient_id, treatment_type, additional_notes,date,time))
            connection.commit()
            QMessageBox.warning(self,"Congrats!","New appointment booked!") 
            # QMessageBox.connect(patientLoginForm())
        else:
            QMessageBox.warning(self,"ERROR!","Error in booking appointment!")
        connection.close()

        
class appointmentCancelForm(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(appointmentCancelForm, self).__init__() 

        # Load the .ui file
        uic.loadUi("Appointment Canceling Form.ui", self) 

        # Changing name of MainWindow
        self.setWindowTitle("Appointment Canceling Form")
        self.SubmitButton= self.findChild(QPushButton,"pushButton")
        self.SubmitButton.clicked.connect(self.delete_appointment)
    def delete_appointment(self):
        lineEdit_9=self.findChild(QtWidgets.QLineEdit, "lineEdit_9")
        lineEdit_10=self.findChild(QtWidgets.QLineEdit, "lineEdit_10")
        appointment_id=lineEdit_9.text()
        Reason=lineEdit_10.text()
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM [APPOINTMENTS] where Appointment_ID=?",appointment_id)
        result = cursor.fetchone()

        # Execute the query with the parameter
        if result:
            sql_query = "UPDATE [APPOINTMENTS] SET Status = 'Cancelled', Reason = ? WHERE Appointment_ID = ?;"
            cursor.execute(sql_query, (Reason, appointment_id))
            QMessageBox.warning(self,"Cancelled!","Your appointment has been cancelled for the given ID!")
            # Commit the changes to the database
            connection.commit()
        else:
            QMessageBox.warning(self,"Warning!","No such appointment found.")
        # Close the connection
        connection.close()

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
        self.SubmitButton= self.findChild(QPushButton,"pushButton")
        self.SubmitButton.clicked.connect(self.feedback)
    def feedback(self):
        lineEdit=self.findChild(QtWidgets.QLineEdit, "lineEdit")
        lineEdit_2=self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        lineEdit_3=self.findChild(QtWidgets.QLineEdit, "lineEdit_3")
        name = lineEdit.text()
        id=lineEdit_2.text()
        combo_box = self.findChild(QtWidgets.QComboBox,"comboBox")
        feedback=lineEdit_3.text()
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("SELECT TOP 1 Feedback_ID FROM [FEEDBACK] ORDER BY Feedback_ID DESC")
        id1=cursor.fetchone()
        idnew1=id1[0]
        rating = combo_box.currentText()
        sql_query = "INSERT INTO [FEEDBACK] (Feedback_ID,Patient_ID,Patient_full_name,Feedback,Overall_rating) VALUES(?,?,?,?,?)"
        if (name=='' or id==''or feedback==''):
            QMessageBox.warning(self,"Feedback Not Entered!","You have not entered your ID or name or feedback!")
        else:
            cursor.execute(sql_query,(int(idnew1)+1,id,name,feedback,rating))
            connection.commit()
            QMessageBox.warning(self,"Congrats!","Feedback Added!")
        connection.close()
            
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
        super(inventoryUpdateForm, self).__init__()
        uic.loadUi("Inventory Quantity Update Form.ui", self)
        self.setWindowTitle("Inventory Update Form")
        self.table_widget = self.findChild(QTableWidget, "tableWidget")

        self.populate_inventory_table()
        self.SubmitButton = self.findChild(QPushButton, "pushButton_3")
        print("A")
        self.SubmitButton.clicked.connect(self.update_data)
        # Establish database connection and fetch data

    def populate_inventory_table(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        print("RUNNING")
        cursor.execute("SELECT * FROM INVENTORY")
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.table_widget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_widget.setItem(row_index, col_index, item)

        connection.close()
        # header = self.table_widget.horizontalHeader()
        # header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def update_data(self):
        print("function")
        lineEdit_2=self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        lineEdit=self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.table_widget = self.findChild(QTableWidget, "tableWidget")
        new_quantity_in_stock=lineEdit.text()
        new_item_id=lineEdit_2.text()
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        query = "select Item_ID from [INVENTORY] where Item_ID=?"
        for row in range(self.table_widget.rowCount()):
            print(row)
            item_at_index_0 = self.table_widget.item(row, 0)
            Check = cursor.execute(query,new_item_id)
            if Check:
                # Update the QTableWidget
                # self.table_widget.setItem(row, 4, QTableWidgetItem(new_quantity_in_stock))

                # Update the database (replace this with your actual update query)
                
                cursor.execute("UPDATE [INVENTORY] SET Quantity_in_Stock = ? WHERE Item_ID = ?", new_quantity_in_stock, new_item_id)
                QMessageBox.warning(self, "Inventory Updated!", "You have updated the quantity of an item!")

                # Commit the changes to the database
                connection.commit()

                break  # Stop searching after finding the item
        self.table_widget.clearContents()
        self.table_widget.setRowCount(0)
        self.populate_inventory_table()


        connection.close()
        
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
