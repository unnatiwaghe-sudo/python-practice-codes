def convert_to_upper():
    print("Enter lines (type 'END' to stop):")
    
    while True:
        line = input()
        if line == "END":
            break
        print(line.upper())
convert_to_upper()

