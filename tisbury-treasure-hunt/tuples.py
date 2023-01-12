"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    return tuple(azara_record[1])==rui_record[1]
    
def create_record(azara_record, rui_record):
    if tuple(azara_record[1])==rui_record[1]:
        return (azara_record)+(rui_record)
    else:
        return "not a match"
   
def clean_up(combined_record_group):
    return "".join([str((r[0], r[2], r[3], r[4]))+"\n" for r in combined_record_group])