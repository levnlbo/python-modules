def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(current, total):
        if current > total:
            print("Harvest time!")
            return
        print("Day " + str(current))
        count(current + 1, total)

    count(1, days)
