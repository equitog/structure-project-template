from os import path, mkdir

def clean_groups(groups: str) -> list:
    """
    groups = Is a field of groups for example: "group_1;group_2;group_3"
    :param groups:
    :return: list
    """
    a = groups.split(";")

    groups_clean = []
    for i in a:
        if "\n" in i:
            groups_clean.append(i.replace("\n", ""))
        else:
            groups_clean.append(i.strip())

    groups_clean_end = []
    for idx, ii in enumerate(groups_clean):
        if len(ii) > 0:
            groups_clean_end.append(ii)
    return groups_clean_end

def create_folder(path_project: str, name_folder: list) -> str:
    """Funcion sirve para crear carpetas dentro del proyecto. El nombre de las carpetas
    se ingresan por elemento o elementos en una lista. Ejemplo: 
     - Para una sola carpeta: ['folder1']
     - Para carpetas y sub carpetas: ['folder1', 'sub_folder1',  'sub_sub_folder1']

    Args:
        path_project (str): Cadena de la ruta raíz del proyecto.
        name_folder (list): Lista de nombre o nombres de las carpetas que se crearan

    Returns:
        [str]: Ruta completa creada
    """
    
    root_folder: str = path_project
    
    acum_folders: str = "\\"
    for i in name_folder:
        acum_folders = acum_folders + i + "\\"
        new_folder = root_folder + acum_folders
        if not path.exists(new_folder):
            mkdir(new_folder)
    return new_folder
