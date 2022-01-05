#Using Faker Module For Creating Fake Data In Python
from faker import Faker

#Using Pandas Module For Formatting Later On For CSV
import pandas as pd

#Import JSON Module For Conversion Later ON
import json

#For Creation Of CSV And Then Conversion to JSON
import csv

#Calling Faker Module (Instance Of Faker)
fake_data = Faker()

#Faker Data Variables That Will Be Used To Create Dummy Data File
ssn = fake_data.ssn()
name = fake_data.name()
address = fake_data.address()
email = fake_data.email()
job = fake_data.job()
phone = fake_data.phone_number()
company = fake_data.company()

#Creating A Fake Profile
#profile = fake_data.simple_profile()
#for k,v in profile.items():
    #print('{}: {}'.format(k,v))

# Display Name, Address, Email
#print('Name: {}, Address: {}, email:{}'.format(name,address,email))

# Generating A Large Set Of Fake Data
#for _ in range(0,10):
    #print(fake_data.name())

# function to fill a list with data
# change .name() to another data type for other data options
def create_name_list(how_many):
    names = []
    for _ in range(0, how_many):
        names.append(fake_data.name())
    return names

#Creating Person Objects With Name, Address, Etc.
class Customers:
    def __init__(self, ssn, name, address, email, job, phone, company):
        self.ssn = ssn
        self.name = name
        self.address = address
        self.email = email
        self.job = job
        self.phone = phone
        self.company = company

    def __repr__(self):
        return 'ssn:{}, name:{}, address: {}, email: {}, job: {}, phone: {}, company: {}'.format(self.ssn, self.name, self.address, self.email, self.job, self.phone, self.company)

# Instance Of Customer Class Using Fake Data
customer1 = Customers(fake_data.ssn(), fake_data.name(), fake_data.address(), fake_data.email(), fake_data.job(), fake_data.phone_number(), fake_data.company())
print(customer1)

# Generate List Of Customers Class Objects With Fake Data
# Change the number 1000 to whatever you want
customers_list = []
for i in range(10):
    customers_list.append(Customers(fake_data.ssn(), fake_data.name(), fake_data.address(), fake_data.safe_email(), fake_data.job(), fake_data.phone_number(), fake_data.company()))
for i in customers_list:
    print(i, '\n')

# Pandas To Create Columns To Format As CSV The number 10 determines the amount of columns you can have
pd.set_option('display.max_columns', 10)

# Creating A Dataframe With 3 Columns Including Names, Adresses, And Emails
# Change the number 1000 to whatever you want
df = pd.DataFrame({'ssn': [fake_data.ssn() for _ in range(10)],
                   'name': [fake_data.name() for _ in range(10)],
                   'address': [fake_data.address() for _ in range(10)],
                   'email': [fake_data.email() for _ in range(10)],
                   'title': [fake_data.job() for _ in range(10)],
                   'phone': [fake_data.phone_number() for _ in range(10)],
                   'company': [fake_data.company() for _ in range(10)]})

# If \n (New Lines) Remove
df = df.replace('\n','', regex=True)

# Export To CSV
df.to_csv('testdata.csv', index=False)

# Defining The Function To Convert CSV File To JSON File
def convjson(csvFilename, jsonFilename):

    # Creating A Dictionary
    mydata = {}

    # Reading The Data From CSV File
    with open(csvFilename, encoding = 'utf-8') as csvfile:
        csvRead = csv.DictReader(csvfile)

        # Converting Rows Into Dictionary And Adding It To Data
        for rows in csvRead:

            mykey = rows['ssn']
            mydata[mykey] = rows

    # Dumping The Data
    with open(jsonFilename, 'w', encoding = 'utf-8') as jsonfile:
        jsonfile.write(json.dumps(mydata, indent = 4))

# Filenames
csvFilename = r'testdata.csv'
jsonFilename = r'testdata.json'

# Calling The convjson function
convjson(csvFilename, jsonFilename)

# Reference https://www.youtube.com/watch?v=bW2uTvvqTg4
