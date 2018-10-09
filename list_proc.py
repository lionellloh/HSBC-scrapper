import csv

def write_to_csv(x):
    x = ['Address: Flat 1,5/F,Block/Tower A,Abba House,Aberdeen/Ap Lei Chau,Hong Kong\nValuation HKD\n4,670,000\nGross floor area (sq ft)\n405\nSaleable area (sq ft)\n304\nProperty age (year/s)\n35\nValuation date\n10 Oct 2018']

    x = x[0].split('\n')
    x[0] = x[0].split(": ")[1]
    x = [x[i] for i in range(0, len(x),2)]
    for i in range(1,5):
        x[i] = float("".join(x[i].split(",")))

    print(x)
    print(len(x))

    with open("output.csv",'w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerow(x)



# output = []
# output.append(x[0].split(": ")[1])
#
# for e in x[1:]:
#     output.append(e)
#
# for i,e in enumerate(output):
#     print(i,e)
#
# dict_output = {}
#
# special = [2,4,6,8]
# for i in range(0, len(output)-1,2):
#     print(i)
#     if i in special:
#         dict_output[output[i]] = float("".join(output[i+1].split(',')))
#
#
#     else:
#         dict_output[output[i]] = output[i+1]
#
# print(dict_output)
#
#
# import csv
#
# my_dict = {"test": 1, "testing": 2}
#
# with open('dict.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in dict_output.items():
#         writer.writerow(value)

