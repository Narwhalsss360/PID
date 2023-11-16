from typing import TextIO, Optional

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