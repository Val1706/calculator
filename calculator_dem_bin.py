print("\nHi! This is Binary - Decimal calculator. "
      "\nProgram prints two numbers in one line separate with single space. "
      "\nFirst of them is a number to covert, and the second one is information "
      "\nabout the actual system (2 or 10). "
      "\nProgram prints two values - "
      "\nconverted number and information about number system after conversion (2 or 10),"
      "\nalso separated with one space.")
while True:


    a = input("\nProvide the number: ")
    spc = " "
    if spc in a:
        try:
            b = a.split(" ")
            frst_am = (b[0])
            mean = int(b[1])
        except ValueError:
            print("Please follow the instruction")
            continue
    else:
        print("Please follow the instruction")
        continue


    if mean == 10:
        frst_am = int(frst_am)
        x = frst_am
        k = []
        while (frst_am > 0):
            a = int(float(frst_am % 2))
            k.append(a)
            frst_am = (frst_am-a)/2
        k.append(0)
        string = ""
        for j in k[::-1]:
            string = string+str(j)
        print("\nThe binary number is")
        print("/-----------\ ")
        print(" " '%s' % (string),"| 2")
        print("\-----------/")
        continue

    if mean == 2:
        frst_am = str(frst_am)
        if frst_am.startswith("0"):
            index = 0
            total = 0
            size = len(frst_am) - 1
            frst_am = frst_am[::-1]

            while index <= size:
                if frst_am[index] == '1':
                    total += (2 ** index)
                    index += 1
                else:
                    total = total
                    index += 1
            print("\nThe decimal number is")
            print("""/--------\ """)
            print(" ",total,"|", "10")
            print("""\--------/ """)
        else:
            print("Please provide correct binary number")



