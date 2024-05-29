# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Ian Buchan, Mamas A Mamas, Naveed Sattar, Darren M Ashcroft, Martin M Rutter, 2024.

import sys, csv, re

codes = [{"code":"C108C00","system":"readv2"},{"code":"F420800","system":"readv2"},{"code":"C108B00","system":"readv2"},{"code":"F420600","system":"readv2"},{"code":"C108700","system":"readv2"},{"code":"C109A00","system":"readv2"},{"code":"C10EC12","system":"readv2"},{"code":"C109600","system":"readv2"},{"code":"C10E712","system":"readv2"},{"code":"C109B00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('microvascular-complications-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["microvascular-complications-noninsulin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["microvascular-complications-noninsulin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["microvascular-complications-noninsulin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
