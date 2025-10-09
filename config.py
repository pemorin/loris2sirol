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
    "pbezeau_jgh": "pbezeau",
    "Pbezeau": "pbezeau",
    "Mcmorin": "mcmorin",
    "admin_iugm": "admin",
    "avoinescu_jgh": "avoinescu",
    "jlegault_iugm": "jlegault",
    "mcveilleux_iugm": "mcveilleux",
    "mcveilleux_jgh": "mcveilleux",
    "naboujaoude_criugm": "naboujaoude",
    "naboujaoude_jgh": "naboujaoude",
    "qarsenault_criugm": "iarsenault"
    }

examiner_mapping = {
    'Adama Fanta Kaba (CINQ)': 'Adama Fanta Kaba',
    'Adama Fanta Kaba (IUGM)': 'Adama Fanta Kaba',
    'Adama Fanta Kaba (JGH)': 'Adama Fanta Kaba',
    'admin (DCC)': 'admin',
    'Tester Test (DCC)': 'admin',
    'Aline Aboujaoudé (CINQ)': 'Aline Aboujaoudé',
    'Aline Aboujaoudé (JGH)': 'Aline Aboujaoudé',
    'Ana-Maria Voinescu (CHUS)': 'Ana-Maria Voinescu',
    'Ana-Maria Voinescu (CINQ)': 'Ana-Maria Voinescu',
    'Ana-Maria Voinescu (JGH)': 'Ana-Maria Voinescu',
    'Anne Morinville (JGH)': 'Anne Morinville',
    'Catherine Brodeur (JGH)': 'Catherine Brodeur',
    'Catherine Dubé (JGH)': 'Catherine Dubé',
    'Céline Fouquet (IUGM)': 'Céline Fouquet',
    'Charlotte Francoeur (CHUS)': 'Charlotte Francoeur',
    'Charlotte Francoeur (CINQ)': 'Charlotte Francoeur',
    'Christel Cornelis (JGH)': 'Christel Cornelis',
    'Claudia Goupil (CRIUGM)': 'Claudia Goupil',
    'Danny Simard (CHUS)': 'Dany Simard',
    'Danny Simard (JGH)': 'Dany Simard',
    'Francis Andriamampionona (JGH)': 'Francis Andriamampionona',
    'Heather Kape (JGH)': 'Heather Kape',
    'Ioana Minoiu (CRIUGM)': 'Ioana Minoiu',
    'Ioana Minoiu (JGH)': 'Ioana Minoiu',
    'Isabel Arsenault (CINQ)': 'Isabel Arsenault',
    'Isabel Arsenault (IUGM)': 'Isabel Arsenault',
    'Isabel Arsenault (JGH)': 'Isabel Arsenault',
    'Isabelle Bureau (JGH)': 'Isabelle Bureau',
    'Joannie Van Houtte St-Gelais (JGH)': 'Joannie Van Houtte St-Gelais',
    'Juan Manuel Villalpando (JGH)': 'Juan-Manuel Villalpando',
    'Julie Legault (JGH)': 'Julie Legault',
    'Karine Thorn (CHUS)': 'Karine Thorn',
    'Karine Thorn (JGH)': 'Karine Thorn',
    'Marie-Claude Veilleux (JGH)': 'Marie-Claude Veilleux',
    'Mehdi Essounni (CHUS)': 'Mehdi Essounni',
    'Mehdi Essounni (CINQ)': 'Mehdi Essounni',
    'Mehdi Essounni (IUGM)': 'Mehdi Essounni',
    'Nancy Aboujaoudé (CHUS)': 'Nancy Aboujaoudé',
    'Nancy Aboujaoudé (CINQ)': 'Nancy Aboujaoudé',
    'Nancy Aboujaoudé (JGH)': 'Nancy Aboujaoudé',
    'Samantha Maltezos (JGH)': 'Samantha Maltezos',
    'Simon Cloutier (JGH)': 'Simon Cloutier',
    'Sylvie Rheault (CHUM)': 'Sylvie Rheault',
    'Sylvie Rheault (CINQ)': 'Sylvie Rheault',
    'Sylvie Rheault (JGH)': 'Sylvie Rheault',
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
    "V00": "t00",
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
    "V41": "t10",
    "V99": "t99"
    }

participant_status_mapping = {
    "Active": "actif",
    "Incomplete_Lost to Followup": "inactif_perdu_au_suivi_incomplet",
    "Incomplete_Death": "inactif_décès_incomplet",
    "Complete": "inactif_perdu_au_suivi_complet"
}