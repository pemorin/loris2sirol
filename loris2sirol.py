import os.path
import csv
import config
import log_config
import logging

"""

ETL_loris2sirol is ascript  designed to transfert data from loris tsv files and prepare SQL elements for insertion into sirol. 
It prepares a SQL document ready for execution. It assumes that the tsv files are well-formed and uses UTF-8 encoding.
It also changes the visit part of the uid to the corresponding timepoint based on a mapping defined
in config.py.

This script is designed to be run ONCE as a standalone program and does not require any external dependencies.
"""

def get_all_tsv_files(path: str) -> list:
    """ 
    Get all TSV files in the specified directory
    Returns a list of file names with .tsv extension
    If no files are found, returns an empty list
    """
    file_list: list = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if file.split('.')[-1] == "tsv":
                file_list.append(file)
    if not file_list:
        logging.info
        pass
    return file_list


def read_tsv_file(file: str) -> list:
    """
    Read a TSV file and return its content as a list
    The first element is the table name: str, followed by headers: list and rows: dict
    Example: ['tablename', ['header1', 'header2'], [{'header1': 'value1', 'header2': 'value2'}, ...]]
    This function assumes that the TSV file is well-formed and uses UTF-8 encoding
    """
    data: list = []
    tablename: str = file.split('.')[0]
    data.append(tablename)
    with open(f"{config.incoming_directory}{file}", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        header: list = reader.fieldnames
        rows: list = list(reader)
        data.append(header)
        data.append(rows)
    return data


def get_sql_elements(data: list) -> list:
    """
    Get the SQL elements from the data list
    Returns a list containing the table name, field names, and values string
    in the format suitable for SQL insertion.
    Example: ['tablename', '(field1, field2)', '('value1', 'value2'), ('value1', 'value2') ...']
    """
    sql_elements: list = []
    table_name: str = get_tablename(data)
    fields_string: str = get_fieldnames(data)
    values_string: str = get_values(data)
    sql_elements.append(table_name)
    sql_elements.append(fields_string)
    sql_elements.append(values_string)
    return sql_elements


def get_tablename(data: list) -> str:
    """
    Get the tablename from data[0] and return it as a string.
    This function assumes that data[0] is the table name.
    """
    tablename: str = data[0]
    return tablename


def get_fieldnames(data) -> str:
    """
    Get the list of fields from data[1] and return it as a string.
    This function assumes that data[1] contains the headers of the TSV file.
    The returned string is formatted for SQL insertion.
    Example: '(field1, field2, field3)'
    """
    headers: list = data[1]
    fields_list: list = []
    for item in headers:
        fields_list.append(f"{item}, ")
    fields_string: str = ''.join(fields_list)
    fields_string = f"({fields_string[:-2]})"  # Remove the last comma and space and format for SQL
    return fields_string


def get_values(data: list) -> str:
    """
    Get the values from data[2] and return them as a string formatted for SQL insertion.
    This function assumes that data[2] contains the rows of the TSV file.
    The returned string is formatted as a series of tuples, each containing the values for a row
    Example: 'VALUES (value1, value2), (value1, value2, ...'
    The function also changes the loris visit part of the UID to the corresponding sirol timepoint based 
    on the mapping in config.py.
    The returned string is suitable for SQL insertion.
    """
    values_string: str = ""
    values_list: list = []
    for row in data[2]:
        values_list = []
        for key, value in row.items():
            if key == 'uid':
                value = change_visit_to_timepoint_mapping(value)
            if key == 'date_entree_donnees':
                value = value[:10]  # Keep only the date part assuming it's in 'YYYY-MM-DD' format
            if key == 'statut_du_participant':
                value = convert_participant_status(value)
            if key == 'details':
                value = value.replace("'", "ʼ")  # Escape single quotes for SQL
            values_list.append(f"'{value}', ")
        values_string += f"({''.join(values_list)[:-2]}), \n"  # Remove the last comma and space and format for SQL  
    values_string = f"{values_string[:-3]};"  # Remove the last comma and newline and format for SQL
    return values_string


def change_visit_to_timepoint_mapping(uid: str) -> str:
    """
    Change the visit part of the UID to the corresponding timepoint based on the mapping in config.py.
    Assumes the UID is in the format 'subject_evaluation_timepoint' and that the visit part is the third part of the UID.
    """
    uid_parts: list = uid.split('_')
    timepoint: str = config.visit_timepoint_mapping[uid_parts[2]]  # Assuming the third part is the timepoint
    uid = f"{uid_parts[0]}_{uid_parts[1]}_{timepoint}"
    return uid

def convert_participant_status(status: str) -> str:
    """
    Convert the participant status from English to French based on the mapping in config.py.
    If the status is not found in the mapping, it returns the original status.
    """
    statut: str = config.participant_status_mapping[status]
    return statut


def prepare_sql_doc(sql_elements: list) -> str:
    """
    Prepare the SQL document from the SQL elements list.
    This is different from functions.prepare_sql_doc as it exclude the UPSERT statement.
    The list should contain the table name, fields string, and values string.
    Returns a formatted SQL string ready for execution.
    Example: "INSERT INTO tablename (field1, field2) VALUES (value1, value2), (value1, value2);"
    This function assumes that sql_elements is well-formed and contains the necessary elements.
    """
    sql_query: str = f"INSERT INTO {sql_elements[0]} {sql_elements[1]} VALUES {sql_elements[2]}"
    return sql_query


def write_to_file(document: str, filename: str, path: str) -> None:
    """
    Write the SQL document to a file.
    The file will be created in the specified path with the given filename.
    If the file already exists, it will be overwritten.
    This function assumes that the path is valid and writable.
    """
    with open(os.path.join(path, filename), 'w', encoding='utf-8') as file:
        file.write(document)
    logging.info(f"{filename} written to {os.path.join(path, filename)}")


def main() -> None:
    # Get all .tsv files
    all_tsv_files: dict = get_all_tsv_files(config.incoming_directory)
    # Get data from tsv files
    for file in all_tsv_files:
        data: list = read_tsv_file(file)
        sql_elements: list = get_sql_elements(data)
        sql_doc: str = prepare_sql_doc(sql_elements)
        write_to_file(sql_doc, f"{sql_elements[0]}.sql", config.data_directory)
        

if __name__ == '__main__':
    # Set log file
    log_config.set_log()
    logging.info(f"*** Démarrage de {str(os.path.basename(__file__))}... ***")
    # Run main()
    main()