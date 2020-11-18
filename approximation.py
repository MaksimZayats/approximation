def cut_matrix(matrix: list, row_number: int = -1, column_number: int = -1):
    """
        Args:
        -----
            matrix: list
                Example:
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]

            row_number: int (default: {-1})
                Must be less than or equal to Row Count.
                Example:
                    [
                        [1, 2, 3], — Row number equals to 0
                        [4, 5, 6], ...
                        [7, 8, 9]  — Row number equals to 2
                    ]

            column_number: int (default: {-1})
                Must be less than or equal to Column Count.
                Example:
                    [
                        Column Number equals to 0
                         |
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                               |
                               Column Number equals to 2
                    ]
            <NOT RELEASED>
                The default value -1 for row_number/column_number means that the row/column does not need to be deleted.
        Raises:
        -------
            <NOT RELEASED>
            <Some ErrorType>
                Row Number or Column Number greater than Row/Column Count.
        Returns:
        -------
            Cropped matrix: list.
        Makes:
        -------
            Deletes the row and the column.
    """
    output_matrix = []
    for row_id, row in enumerate(matrix):
        buffer = []
        for column_id, column in enumerate(row):
            if row_id == row_number:
                break
            if column_id != column_number:
                buffer.append(column)
        if row_id != row_number:
            output_matrix.append(buffer)
    return output_matrix


def find_determinant(matrix: list):
    """
        Args:
        -----
            Matrix: list
                Example:
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]
        Returns:
        -------
            Determinant of matrix
    """
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        d = 0
        for i in range(len(matrix)):
            d += ((-1) ** i) * matrix[0][i] * find_determinant(cut_matrix(matrix=matrix, row_number=0, column_number=i))
        return d


def change_column(matrix: list, new_column: list, column_number: int):
    """
        Args:
        -----
            matrix: list
                Example:
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]

            new_column: list
                Must be the same length as the column of the original matrix.
                Example:
                    [20, 50, 80]

            column_number: int
                Must be less than or equal to Column Count.
                Example:
                    column_number=0

                    Column Number equals to 0
                     |
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                           |
                           Column Number equals to 2

        Raises:
        -------
            <NOT RELEASED>
            <Some ErrorType>
                Column Number greater than Column Count.
        Returns:
        -------
            Changed matrix: list
        Makes:
        -------
            Changes the matrix column to a new one.
    """
    output_matrix = []
    for row_id, row in enumerate(matrix):
        buffer = []
        for column_id, column in enumerate(row):
            if column_id == column_number:
                buffer.append(new_column[row_id])
            else:
                buffer.append(column)
        output_matrix.append(buffer)
    return output_matrix


def solve_linear(m_coefficients: list, m_answers: list):
    """
        Args:
        -----
            m_coefficients: list (as matrix)
                Example:
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]

            m_answers: list
                Must be equal to Row Count.
                Example:
                    [10, 11, 12]

        Raises:
        -------
            <NOT RELEASED>
            <Some ErrorType>
                len(m_answers) not equal to Row Count.
        Returns:
        -------
            coefficients: list
        Makes:
        -------
            Solves a system of linear equations using the Cramer's rule ( https://en.wikipedia.org/wiki/Cramer%27s_rule )
    """
    main_determinant = find_determinant(m_coefficients)
    if main_determinant == 0:
        raise Exception('Указано не достаточное количество точек для данной степени')

    secondary_determinants = []
    for i in range(len(m_answers)):
        secondary_determinants.append(
            find_determinant(
                change_column(
                    m_coefficients, m_answers, i
                )
            )
        )
    coefficients = []
    for i in range(len(m_coefficients)):
        coefficients.append(secondary_determinants[i] / main_determinant)
    return coefficients


def approximate(x: list, y: list, p: int):
    """
        Args:
        -----
            len(x) should be equal to len(y)
            x: list
                Coordinates of points on the x-axis
                Example:
                    [1, 2, 3]

            y: list
                Coordinates of points on the x-axis
                Example:
                    [2, 5, 10]

            p: int
                Power of the polynom

        Raises:
        -------
            <NOT RELEASED>
            <Some ErrorType>
                len(x) is not equal to len(y)
        Returns:
        -------
            polynomial_coefficients: list

            polynomial_coefficients goes from lower power to highest
            Example:
                In this case function returns this coefficients:
                    [1.0, 0.0, 1.0]
                It means:
                    1*x^0 + 0*x^1 + 1*x^2
                    or
                    x^2 + 1

        Makes:
        -------
            Approximates points(x, y) to a polynom with {p} power ( https://en.wikipedia.org/wiki/Approximation )
    """

    if len(x) != len(y):
        raise Exception('len(x) is not equal to len(y)')

    def sum_(x_numbers: list, power: int, y_numbers=[]):
        """
            Used ONLY for approximation.
            -----------------------
            Args:
            -----
                x_numbers: list
                y_numbers: list (default: {[]})
                power: int

            Returns:
            -------
                sum: int

            Makes:
            -------
                Creates a sum based on a special rule
        """
        sum = 0
        if y_numbers == []:
            for number in x_numbers:
                sum += number**power
        else:
            for i in range(len(x_numbers)):
                sum += y_numbers[i]*x_numbers[i]**power
        return sum

    def create_matrix(size: int, coefficients: list):
        """
            Used ONLY for approximation.
            -----------------------
            Args:
            -----
                size: int
                coefficients: list

            Returns:
            -------
                matrix: list

            Makes:
            -------
                Creates a matrix based on a special rule
        """
        matrix = []
        for i in range(size):
            matrix.append(coefficients[i: size + i])
        return matrix

    coefficients = []
    for n in range(p * 2 + 1):
        coefficients.append(
            sum_(x_numbers=x, power=n)
        )

    answers_matrix = []
    for n in range(p + 1):
        answers_matrix.append(
            sum_(x_numbers=x, y_numbers=y, power=n)
        )

    polynomial_coefficients = solve_linear(
        create_matrix(p + 1, coefficients),
        answers_matrix
    )

    return polynomial_coefficients


def create_polynom(polynomial_coefficients: list):
    """
        Args:
        -----
            polynomial_coefficients: list

        Returns:
        -------
            polynom: string

        Makes:
        -------
            Creates a polynom (as string) with polynomial_coefficients.
    """
    polynom = ''
    for n, coefficient in enumerate(reversed(polynomial_coefficients)):
        if coefficient == int(coefficient):
            if coefficient == 0:
                continue
            elif coefficient == 1 and len(polynomial_coefficients)-1-n == 0:
                coefficient = 1
            elif coefficient == 1:
                coefficient = ''
            else:
                coefficient = int(coefficient)

        polynom += f"{coefficient}x^{len(polynomial_coefficients) - 1 - n} + "

    return polynom[:-2].replace("x^0", '')
