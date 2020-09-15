filename_tuple = (2, 10, 11, 3)
print("{:30} {}".format("input filenames are", filename_tuple))

list_name = []
for n in filename_tuple:
    f = 'file_{:04d}'.format(n)
    list_name.append(f)
print("{:30} {}".format("zero padded filenames", (list_name)))

sorting = sorted(list_name)
print("{:30} {}".format("sorted filenames are", (sorting)))