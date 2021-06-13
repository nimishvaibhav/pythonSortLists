


def sort_list():
    unsortedlist = [4, 5, 0, 9, 2, 8, 1]
    sorted_list = []

    while unsortedlist:
        minvalue = unsortedlist[0]
        for num in unsortedlist:
            if num < minvalue:
                minvalue = num
        sorted_list.append(minvalue)
        unsortedlist.remove(minvalue)

    print(sorted_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sort_list()


