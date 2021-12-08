import numpy as np

# краткая запись ф-ий в дифференциальных ур-ях
function_list = np.array([
    # 0
    [
        {1: 1, 2: 3, 3: 7, 4: 8, 5: 13, 6: 14},
        {7: 4, 8: 6, 9: 9}
    ],
    # 1
    [
        {10: 5, 11: 13},
        {12: 4, 13: 6, 14: 9}
    ],
    # 2
    [
        {},
        {15: 0}
    ],
    # 3
    [
        {16: 1, 17: 5, 18: 7, 19: 14},
        {20: 4, 21: 9}
    ],
    # 4
    [
        {},
        {22: 2}
    ],
    # 5
    [
        {23: 1, 24: 2},
        {25: 4, 26: 9}
    ],
    # 6
    [
        {27: 9},
        {28: 1, 29: 2, 30: 3, 31: 11}
    ],
    # 7
    [
        {32: 11, 33: 13},
        {}
    ],
    # 8
    [
        {34: 7, 35: 14},
        {36: 9}
    ],
    # 9
    [
        {37: 2},
        {}
    ],
    # 10
    [
        {},
        {}
    ],
    # 11
    [
        {38: 13},
        {39: 6, 40: 9}
    ],
    # 12
    [
        {41: 7},
        {42: 6, 43: 9}
    ],
    # 13
    [
        {44: 2, 45: 6},
        {}
    ],
    # 14
    [
        {46: 7},
        {47: 6}
    ],
])


def process_part_of_expression(u,
                               fak_list,
                               t,
                               dict_of_function_expressions,
                               new_function_list,
                               index_expression,
                               index_side):
    result = 1
    result_fak = 0

    for num_function in new_function_list[index_expression][index_side]:
        result *= dict_of_function_expressions[num_function](
            u[new_function_list[index_expression][index_side][num_function]])
    for fak in fak_list:
        result_fak += fak(t)
    return result * result_fak


def fak_1(t):
    return t ** 2 + 1


def fak_2(t):
    return np.cos(1.5 * t * np.pi - np.pi / 6) ** 2 / 4 + 0.2


def fak_3(t):
    return np.sin(t * np.pi - np.pi / 6) / 2.5 + 0.3


def fak_4(t):
    return 2 * t - 1


def fak_5(t):
    return np.cos(1.5 * t * np.pi - np.pi / 6) ** 2 / 4


def fak_6(t):
    return np.sin(t * np.pi - np.pi / 6) ** 2 / 2.5 + 0.3


def pend(u, t, dict_of_function_expressions, new_function_list):
    dudt = [
        # 0
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list, 0, 0)
         -
         process_part_of_expression(u,
                                    [fak_1, fak_2, fak_4, fak_5],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list, 0, 1)),

        # 1
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    1, 0)
         -
         process_part_of_expression(u,
                                    [fak_1, fak_5],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    1, 1)),

        # 2
        (process_part_of_expression(u,
                                    [fak_5],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    2, 0)
         -
         process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    2, 1)),

        # 3
        (process_part_of_expression(u,
                                    [fak_4, fak_5],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    3, 0)
         -
         process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    3, 1)),

        # 4
        (process_part_of_expression(u,
                                    [fak_4, fak_5],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    4, 0)
         -
         process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list, 4, 1)),

        # 5
        (process_part_of_expression(u,
                                    [fak_5],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    5, 0)
         -
         process_part_of_expression(u,
                                    [fak_1, fak_4],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    5, 1)),

        # 6
        (process_part_of_expression(u,
                                    [fak_2, fak_4],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    6, 0)
         -
         process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    6, 1)),

        # 7
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    7, 0) -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    7, 1)),

        # 8
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    8, 0)
         -
         process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    8, 1)),

        # 9
        (process_part_of_expression(u,
                                    [fak_1, fak_2, fak_3, fak_4, fak_5],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    9, 0)
         -
         process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    9, 1)),

        # 10
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    10, 0)
         -
         process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    10, 1)),

        # 11
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    11, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    11, 1)),

        # 12
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    12, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    12, 1)),

        # 13
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    13, 0)
         -
         process_part_of_expression(u,
                                    [fak_2],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    13, 1)),

        # 14
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    14, 0)
         -
         process_part_of_expression(u, [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    14, 1))
    ]
    return dudt
