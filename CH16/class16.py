import csv

Analysis = 'Data.txt'
csv_file = 'Data.csv'

open_txt = csv.reader(open(Analysis, 'r'), delimiter=',')
out_csv = csv.writer(open(csv_file, 'w', newline=''))
out_csv.writerow(['筆數', '價格'])
out_csv.writerows(open_txt)