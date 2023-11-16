from typing import TextIO, Optional

def vars_log(object, log_dict: dict, independent: Optional[tuple] = None):
    if independent is not None:
        name, value = independent
        if name not in log_dict:
            log_dict[name] = []
        log_dict[name].append(value)

    for name, value in vars(object).items():
        if name not in log_dict:
            log_dict[name] = []
        log_dict[name].append(value)

def log_dict_csv(file: TextIO, dictionary: dict) -> Optional[str]:
    if file.closed:
        return None

    columns = []
    max_rows = []

    for i_kvp, kvp in enumerate(dictionary.items()):
        key, values = kvp
        columns.append([key])
        for value in values:
            columns[i_kvp].append(value)
        max_rows.append(len(values))

    max_rows = min(max_rows)

    out = ''
    for i_row in range(max_rows):
        for i_column in range(len(columns)):
            out += str(columns[i_column][i_row])
            if i_column == len(columns) - 1:
                out += '\n'
            else:
                out += ','

    file.write(out)
    return out