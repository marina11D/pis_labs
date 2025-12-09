from mygroup import groupmates, print_students, filter_by_average

min_avg = float(input("Введите минимальный средний балл: "))
filtered = filter_by_average(groupmates, min_avg)
print_students(filtered)
