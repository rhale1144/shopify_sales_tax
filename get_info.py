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
                    if row[41] == "VA":
                        if row[2] in financial_status:
                            rows.append(row)
    print(len(rows))
                

    #fc = data['facecream'].tolist()
    #print(row[1])

exit()
#print(args.accumulate(args.integers))
