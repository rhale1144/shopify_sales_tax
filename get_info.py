#!/usr/bin/python3

import csv, argparse, datetime

parser = argparse.ArgumentParser(description='Process some integers.')

#parser.add_argument('integers', metavar='N', type=int, nargs='+',
   #                 help='an integer for the accumulator')

#parser.add_argument('--sum', dest='accumulate', action='store_const',
 #                   const=sum, default=max,
  #                  help='sum the integers (default: find the max)')

parser.add_argument('-y', "--year", help='specify year')
parser.add_argument("-m", "--month", help="specifiy month")
parser.add_argument("-f", "--file", help="specify file")

args = parser.parse_args()

if args.year:
    year = args.year
if args.month:
    month = args.month
if args.file:
    input_file = args.file

rows = []
exempt_rows = []
subtotal_list = []
total_list = []
subtotal_taxes_list = []
exempt_subtotal_list = []
exempt_total_list = []
financial_status = {"paid", "partially_refunded"}
date_status = {"Paid at", ""}

with open(input_file) as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if row[3] not in date_status:
            #date = datetime.fromisoformat(row[3])
            date = datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S %z")
            if str(date.year) == year:
                if str(date.month) == month:
                    if row[2] in financial_status:
                        if row[41] == "VA":
                            rows.append(row)
                        else:
                            exempt_rows.append(row)

    for row in rows:
        row_subtotal = row[8]
        row_total = row[11]
        row_subtotal_taxes = row[10]
        subtotal_list.append(float(row_subtotal))
        total_list.append(float(row_total))
        subtotal_taxes_list.append(float(row_subtotal_taxes))

    for exempt_row in exempt_rows:
        exempt_row_subtotal = exempt_row[8]
        exempt_row_total = exempt_row[11]
        exempt_subtotal_list.append(float(exempt_row_subtotal))
        exempt_total_list.append(float(exempt_row_total))
        
    subtotal = sum(subtotal_list)
    total = sum(total_list)
    subtotal_taxes = sum(subtotal_taxes_list)
    total_taxes = total * 0.06

    exempt_subtotal = sum(exempt_subtotal_list)
    exempt_total = sum(exempt_total_list)
    total_gross = total + exempt_total

    print(len(exempt_total_list))
    print(len(total_list))
    print("Total Gross:       $", round(total_gross, 2))
    print("Exempt Gross:      $", round(exempt_total, 2))
    print("Virginia Gross:    $", round(total, 2))
    print("Virginia Tax:      $", round(total_taxes, 2))
    print("Subtax:            $", round(subtotal_taxes, 2))

    
    
                

    #fc = data['facecream'].tolist()
    #print(row[1])

exit()
#print(args.accumulate(args.integers))
