import sys
def input_number(prompt='Please enter a number: ', minimum=0, maximum=None):

    """Read a positive number with the given prompt."""

    while True:
        try:
            number = int(input(prompt))
            if (number < minimum or
                (maximum is not None and number > maximum)):
                    print('Number is not within range: {} to {}'.format(minimum, maximum))
            else:
                break

        except ValueError:
            sys.exit()

    return number
