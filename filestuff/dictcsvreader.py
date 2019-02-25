from csv import DictReader
with open('csvfile.csv') as file:
    csv_reader = DictReader(file,delimiter=',')
    x = 0
    for row in csv_reader:
        x += 1
        print(f"------Entry {x}-------")
        print("|")
        print(f"|      Policy ID: {row['policyID']}")
        print(f"|      StateCode: {row['statecode']}")
        print(f"|         County: {row['county']}")
        print(f"|  EQ Site Limit: {row['eq_site_limit']}")
        print(f"|  HU Site Limit: {row['hu_site_limit']}")
        print(f"|  FL Site Limit: {row['fl_site_limit']}")
        print(f"|  FR Site Limit: {row['fr_site_limit']}")
        print(f"|       TIV 2011: {row['tiv_2011']}")
        print(f"|       TIV 2012: {row['tiv_2012']}")
        print(f"| EQ Site Deduct: {row['eq_site_deductible']}")
        print(f"| HU Site Deduct: {row['hu_site_deductible']}")
        print(f"| FL Site Deduct: {row['fl_site_deductible']}")
        print(f"| FR Site Deduct: {row['fr_site_deductible']}")
        print(f"|       Latitude: {row['point_latitude']}")
        print(f"|      Longitude: {row['point_longitude']}")
        print(f"|           Line: {row['line']}")
        print(f"|   Construction: {row['construction']}")
        print(f"|    Granularity: {row['point_granularity']}")
        print(f"----------------------\n\n")
