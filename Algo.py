import csv
from Building import Building
from Calls import Calls
import sys
if __name__ == '__main__':
    print("Building file name:", sys.argv[1])
    building_file_name = sys.argv[1]
    print("Calls file name:", sys.argv[2])
    calls_file_name = sys.argv[2]
    print("Output file name:", sys.argv[3])
    output_file_name = sys.argv[3]


    """
    chose the fastest elevator
    """


    def fast_ele(elevators, c):
        speed = 0
        ele = 0
        for e in elevators:
            if speed < e._speed:
                speed = e._speed
                ele = e
        return ele


    """
    write calls to file
    """


    def output(output_file_name: str, row: list, ele: int):
        f = open(output_file_name, 'a', newline='')
        csv_writer = csv.writer(f)
        row[5] = ele  # allocate the elevator
        csv_writer.writerow(row)
        f.close()

    # def algo(building_file_name: str, calls_file_name: str, output_file_name: str):
    b = Building(building_file_name)  # curr Building
    elevators = b.elevators  # Elevators in curr Building
    calls = Calls(calls_file_name).r  # Calls list
    for c in range(len(calls)):  # Calls loop
        ele = 0

        c_length = len(calls) - 1
        end_time = float(Calls(calls_file_name, c_length).time) + 120  # end time of algo calls
        for e in elevators:  # Elevators loop
            if e.elecalls > 0:
                time = e.time_travel(Calls(calls_file_name, c)) + e.elecalls
            else:
                time = e.time_travel(Calls(calls_file_name, c))
            if time < end_time:  # find the fastest elevator
                end_time = time
                ele = e
        a = len(calls) / 2
        if ele.elecalls > a:  # if more than half of the calls are allocate to one elevator - take the fastest
            ele.elecalls -= 1
            ele = fast_ele(elevators, len(calls))
        ele.elecalls += 1
        output(output_file_name, Calls(calls_file_name, c).r[c], ele.eleid)



#
# if __name__ == '__main__':
#     # print("Building file name:", sys.argv[0])
#     # algo("B5.json", "test\Test1.csv", "Calls_.csv")
