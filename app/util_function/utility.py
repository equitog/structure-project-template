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
