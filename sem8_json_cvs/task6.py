import csv
import pickle


def pickle2csv(pickle_file_path: str, csv_file_path: str) -> None:
    with open(pickle_file_path, 'rb') as pf:
        data = pickle.load(pf)
    headers = data[0].keys()
    with open(csv_file_path, 'w', encoding='utf-8') as cf:
        writer = csv.DictWriter(cf, fieldnames=headers, dialect="excel", quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerows(data)


pickle2csv("result_task4.pickle", "csv_task6.csv")
