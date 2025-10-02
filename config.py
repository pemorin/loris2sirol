import os

# Development mode On/Off
debug_mode = True

# Get the home directory of this file
home_directory = os.getcwd()

# log directory
log_directory = "./log/"

# data directories
incoming_directory = "./loris_data/"
data_directory = "./sirol_data/"
data_archives_directory = "./loris_data/archives/"
data_errors_directory = "./loris_data/erreurs/"

# sql core code directories
sql_code_directory = "./sirol_sql/"

# List of files to remove from main excel directory
files_to_remove = [":Zone.Identifier", ".xls"]


# LORIS to SIROL field mapping
# loris_visit : sirol_timepoint

# Sex mapping
sex_mapping = {
    "Male": "homme",
    "Female": "femme"
    }

# userid mapping
userid_mapping = {
    "": "donnée_non_disponible",
    "pemorin": "admin",
    "iminoiu_criugm": "iminoiu",
    "iminoiu_jgh": "iminoiu",
    "avoinescu_iugm": "avoinescu",
    "amorinville_chus": "amorinville",
    "cdube2": "cdube",
    "njaffer_iugm": "njaffer",
    "iarsenault_jgh": "iarsenault",
    "iarsenault_cinq": "iarsenault",
    "iarsenault_chus": "iarsenault",
    "jgagnon_criumg": "jgagnon",
    "pbezeau_jgh": "pbezeau"
    }

# MRI_alias mapping
site_mapping = {
    "IUGM": "criugm",
    "CHUS": "chus",
    "CINQ": "cinq",
    "MNI":  "mni",
    "JGH": "jgh"
    }

# Visit vs timepoint mapping
visit_timepoint_mapping = {
    "QAU": "qau",
    "V01": "t00",
    "V02": "t00",
    "V03": "t00",
    "V04": "t00",
    "V05": "t00",
    "V06": "t00",
    "V07": "t02",
    "V08": "t02",
    "V09": "t02",
    "V10": "t02",
    "V11": "t02",
    "V12": "t02",
    "V13": "t02",
    "V14": "t04",
    "V15": "t04",
    "V16": "t04",
    "V17": "t04",
    "V18": "t04",
    "V19": "t04",
    "V20": "t04",
    "V21": "t06",
    "V22": "t06",
    "V23": "t06",
    "V24": "t06",
    "V25": "t06",
    "V26": "t06",
    "V27": "t06",
    "V28": "t08",
    "V29": "t08",
    "V30": "t08",
    "V31": "t08",
    "V32": "t08",
    "V33": "t08",
    "V34": "t08",
    "V35": "t10",
    "V36": "t10",
    "V37": "t10",
    "V38": "t10",
    "V39": "t10",
    "V40": "t10",
    "V41": "t10"
    }

participant_status_mapping = {
    "Active": "actif",
    "Incomplete_Lost to Followup": "inactif_perdu_au_suivi_incomplet",
    "Incomplete_Death": "inactif_décès_incomplet",
    "Complete": "inactif_perdu_au_suivi_complet"
}