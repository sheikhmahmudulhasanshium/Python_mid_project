file_name=file_name="E:\\AIUB\Semester-10\\midterm\\Python\\Practice\\Virtual-environment\\Project\\Python_Keyword_Dictonary\\stored_file.txt"

def write(list):
    
    with open(file_name,'w') as f:
        for item in list:#saving each list elements in new line as string 

            f.write("%s \n" %item)
    
    """
    with open(file_name,'w') as f:
        for item in list:#saving each list elements in new line as string 

            json.dump(list,f)
            """
def read(list):
      
    try:
        with open(file_name,'r') as f:
            for line in f:#reading line by line
                print(line.rstrip())
    except FileNotFoundError:
        print("File not found")
    
