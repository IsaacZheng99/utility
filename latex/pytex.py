"""
convert python codes to latex codes
"""


def list_to_matrix(list):
    tex = '\\begin{bmatrix}\n'
    for row in list:
        for elem in row:
            tex += '\t' + str(elem) + '\t' + '&'
        tex = tex[:-2]
        tex += ' \\' + '\\'
        tex += '\n'
    tex = tex[:-3] + '\n' + '\end{bmatrix}'
    return tex


def list_to_table(list):
    col_num = len(list[0])
    tex = '\\begin{center}\n' + '\t\\begin{table}[h]\n' + '\t\t\centering\n' + '\t\t\t\\begin{tabular}{'
    tex += '|c' * col_num + '|}\n'
    tex += '\t\t\t\t\hline\n'
    for row in list:
        tex += '\t\t\t'
        for elem in row:
            tex += '\t' + str(elem) + '\t&'
        tex = tex[:-1]
        tex += ' \\' + '\\'
        tex += '\n\t\t\t\t\hline\n'
    tex += '\t\t\t\end{tabular}\n'
    tex += '\t\end{table}\n'
    tex += '\end{center}'
    return tex
