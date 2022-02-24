import csv


def load_csv_data(path: str):
  with open(path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # skip the header row
    return list(csv_reader)


