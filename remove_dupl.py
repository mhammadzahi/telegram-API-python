def remove_duplicates(input_file, output_file):
    
    with open(input_file, 'r') as f:
        lines = f.readlines()


    unique_lines = list(set(lines))

    with open(output_file, 'w') as f:
        f.writelines(unique_lines)


input_file = "data_450.txt"
output_file = "res101.txt"
remove_duplicates(input_file, output_file)
