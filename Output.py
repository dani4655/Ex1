import csv

from Calls import Calls
from Building import Building
from Elevator import Elevator


class Output:
    def __init__(self, file_name, x, callID, callname) -> None:
        f = open(file_name, 'a', newline='')
        csv_writer = csv.writer(f)
        row = Calls(callname,callID).r[callID]
        row[5] = x
        csv_writer.writerow(row)
        f.close()
        # with open("Calls_.csv") as myFile:
        #     lines = myFile.readlines()
        #     last_line = lines[len(lines) - 1]
        #     lines[len(lines) - 1] = last_line.rstrip()
        # with open("Calls_.csv", 'w') as myFile:
        #     myFile.writelines(lines)
