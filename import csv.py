import csv

#reading the cvs file

def open_csv(csv_file):
    with open (csv_file) as file_name:
        reader_obj = csv.reader(file_name)
        for row in reader_obj:
            return row


open_csv('user_details.csv')


#transforming the data you need from the original cvs file



def transform_csv(csv_file):
    user_details = open_csv(csv_file)
    new_list = []
    for row in user_details:
        #new_list.append(row)
        new_list.append(row[1], row[2], str.partition(row[4], "@")[0])
        return new_list


transform_csv('user_details.csv')


def write_csv(old_file, new_file):
    old = transform_csv(old_file) #gives user details
    with open(new_file, "w") as old1:
        writer = csv.writer(old1)
        for row in old:
            writer.writerow(row)


write_csv("user_details.csv","output.csv")
        