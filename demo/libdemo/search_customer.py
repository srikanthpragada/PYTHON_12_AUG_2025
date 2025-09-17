
try:
    f = open("customer.txt", "rt")
    # Take name and convert it to upper
    name = input("Enter customer name :").upper()
    while True:
        line = f.readline()
        # check whether we reached EOF
        if line == "":
            print('Sorry! Name not found!')
            break
        # Check whether name is found in the line
        if name in line.upper():
            print('Found at : ', line)
            break

    f.close()
except Exception as ex:
    print('Error :', ex)
