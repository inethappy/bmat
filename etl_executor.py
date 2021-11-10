import re
import sys
import csv
import time


def main():
    res = {}
    test_file = sys.argv[1] if len(sys.argv) > 1 else 'test_file.csv'
    with open(test_file, 'r') as fd:
        # read file line by line
        for line in fd:
            # pop the 'date' row from the line
            strip_line = re.sub('([0-9]{1,4}\-){2}[0-9]{1,2}', '', line).strip()
            # get the department name for line
            dep = re.sub('[0-9]+', '', strip_line).strip(',')
            # get the number of sales for line
            num = re.search('[0-9]+', strip_line)
            if not dep or not num:
                continue
            num = num.group(0)
            # add the calculated sum to the key in dictionary by summarizing if it exist and by adding a key if not
            res[dep] = num if not res.get(dep) else int(num) + int(res[dep])

    # prepare a dictionary for dumping to the target file
    res_to_csv = []
    for key, value in res.items():
        res_to_csv.append({'dep':key, 'num':value})

    # write a data to the file
    with open('target_file.csv', 'w', newline='') as target:
        writer = csv.DictWriter(target, res_to_csv[0].keys())
        writer.writerows(res_to_csv)



if __name__ == '__main__':
    t = time.process_time()
    main()
    elapsed_time = time.process_time() - t
    print(f"Data transforming finished. Resulting 'target_file.csv' was created in {elapsed_time}s.")


