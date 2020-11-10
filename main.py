
def wedd(N, people_list):
    print(people_list)
    tribes = [set()]
    for i in range(N):
        no_available_tribe = False
        if len(people_list) == 0:
            break
        for tribe in tribes:
            no_available_tribe = False
            if not tribe:
                tribe.add(people_list[0][0])
                tribe.add(people_list[0][1])
                people_list.remove(people_list[0])

            elif people_list[0][0] in tribe:
                tribe.add(people_list[0][1])
                people_list.remove(people_list[0])

            elif people_list[0][1] in tribe:
                tribe.add(people_list[0][0])
                people_list.remove(people_list[0])

            else:
                no_available_tribe = True

            if not no_available_tribe:
                break

        if no_available_tribe:
            tribes.append(set((people_list[0][0], people_list[0][1])))
            people_list.remove(people_list[0])

    male_amount_in_each_tribe = [len({p for p in tribe if p % 2}) for tribe in tribes]
    female_amount_in_each_tribe = [len({p for p in tribe if not p % 2}) for tribe in tribes]
    print(tribes)
    print(male_amount_in_each_tribe)
    print(female_amount_in_each_tribe)

    return sum(male_amount_in_each_tribe) * sum(female_amount_in_each_tribe) - \
           sum((male * female for male, female in zip(male_amount_in_each_tribe, female_amount_in_each_tribe)))


if __name__ == '__main__':
    sample_list = [(1, 2), (2, 4), (3, 5), (7, 8), (2, 15), (10, 8), (15, 20)]

    N = 7

    res = wedd(N, sample_list)
    print(res)

