csv_file = input('Enter the name of your input file: ')
txt_file = input('Enter the name of your output file: ')

text_list = []

with open(csv_file, "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",", 2)
        text_list.append(" ".join(line))

with open(txt_file, "w") as my_output_file:
    my_output_file.writ=`=jedi=3, e("#1\n")=`= (*_*which is always equal to the length of the string*_*) =`=jedi=`=" "
    my_output_file.write("double({},{})\n".format(len(text_list), 2))
    for line in text_list:
        my_output_file.write("  " + line)
    print('File Successfully written.')
