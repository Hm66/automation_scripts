#!/usr/bin/env python3
import os
import csv

def read_employees(csv_file_location):
#Dialect classes can be registered by name so that callers of the CSV
#module don't need to know the parameter settings in advance.
# We will now register a dialect empDialect.
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
#The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
#Append the dictionaries to an empty initialised list employee_list as you iterate over the CSV file.
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees('/home/-00-0600d242a7ff/data/employees.csv')
print(employee_list)

def process_data(employee_list):
# initialize a new list called department_list, iterate over employee_list,
# and add only the departments into the department_list.
    department_list = []
    department_data = {}
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
#The department_list should now have a redundant list of all the department names.
# remove the redundancy and return a dictionary
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data


dictionary = process_data(employee_list)
print(dictionary)

#Once you open the file for writing, iterate through the dictionary and use write()
# on the file to store the data.
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()

write_report(dictionary, '/home/-00-0600d242a7ff/data/report.txt')
