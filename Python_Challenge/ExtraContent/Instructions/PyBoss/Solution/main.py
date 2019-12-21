import os
import csv
import datetime
Emp_ID =[]
First_Name =[]
Last_Name =[]
DOB =[]
SSN =[]
State =[]
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
csvpath = os.path.join('employee_data.csv')
with open(csvpath, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        Emp_ID.append(str(row[0]))
        DOB.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y'))
        SSN.append(("***-**-" + (row[3].split("-"))[2]))
        Name_split = row[1].split(" ")
        First_Name.append(Name_split[0])
        Last_Name.append(Name_split[1])
        if row[4] in us_state_abbrev:
            State.append(us_state_abbrev[row[4]])
        else:
            State.append(row[4])

cleaned_csv = zip(Emp_ID,First_Name,Last_Name,DOB,SSN,State)
output_file = os.path.join('Solution','employee_new.csv')
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name","Last Name","DOB","SSN","State"])
    writer.writerows(cleaned_csv)