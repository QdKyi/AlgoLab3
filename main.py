import doctest


def wedd(N, people_list):

    """
    >>> test_list = [(1, 2), (2, 4), (3, 5), (7, 8), (2, 15), (10, 8), (15, 20)]
    >>> another_test_list = [(2, 1), (4, 2), (3, 5), (7, 8), (2, 15), (10, 8), (15, 20), (5, 25), (10, 55)]
    >>> first_example_list = [(1, 2), (2, 4), (3, 5)]
    >>> second_example_list = [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]
    >>> wedd(len(test_list), test_list)
    17
    >>> wedd(len(another_test_list), another_test_list)
    25
    >>> wedd(len(first_example_list), first_example_list)
    4
    >>> wedd(len(second_example_list), second_example_list)
    6
    """
    people_list.sort(key=lambda x: x)
    tribes = []
    for people in people_list:

        for tribe in tribes:

            if people[0] in tribe:
                tribe.add(people[1])
                break

            elif people[1] in tribe:
                tribe.add(people[0])
                break

        else:
            tribes.append(set((people[0], people[1])))

    male_amount_in_each_tribe = [len({male for male in tribe if male % 2}) for tribe in tribes]
    female_amount_in_each_tribe = [len({female for female in tribe if not female % 2}) for tribe in tribes]

    return sum(male_amount_in_each_tribe) * sum(female_amount_in_each_tribe) - \
           sum((male * female for male, female in zip(male_amount_in_each_tribe, female_amount_in_each_tribe)))


if __name__ == '__main__':
    sample_list = [(1, 2), (2, 4), (3, 5), (2, 3), (2, 15), (10, 8), (15, 20)]

    N = 7
    print(sample_list)
    res = wedd(N, sample_list)
    print(res)

    doctest.testmod(verbose=True)
