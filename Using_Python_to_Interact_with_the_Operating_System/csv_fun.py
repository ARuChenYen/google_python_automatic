# 讀csv file
# 先開檔案，再用csv.reager寫成csv物件
# 最後用for-loop把各項目unpackage出來
import csv
# f = open('csv_file.txt', 'r')
# csv_f = csv.reader(f)
# for row in csv_f:
#     name, phone, role = row
# f.close()

# 寫csv file
# 先開檔案，覆寫或者建新的
# 用obj = csv.writer(file_obj)建立一個csv write的物件
# 用obj.writerows(資料)，把資料寫進去檔案中
# writerows一次可以把所有list中的元素都寫進去

# host = [['wortstation.local', '192.168.1.1'],['webserver.cloud','10.2.5.6']]
# with open('host.csv', 'w') as host_csv:
#     writer = csv.writer(host_csv)
#     writer.writerows(host)
    


# 資料量較大或者項目較多時候，會用dict來讀與寫
# 寫檔案的時候，dict的keys會變成標題 row，value會變成column資料

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(f'{row["name"]} has {row["users"]} users')
    
users = [
    {'name':'apple', 'username':'aaa', 'department':'tfpd'},
    {'name':'book', 'username':'bbb', 'department':'tdfv'},
    {'name':'cat', 'username':'ccc', 'department':'tohkw'},
]
keys = ["name", "username", 'department']    
with open('software2.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerow(users)
    