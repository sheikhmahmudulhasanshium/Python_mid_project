items = [{'description': 'abul', 'location': 'babul', 'time': '2022-02-02 02:20:00'}, {'description': 'kabul', 'location': 'sdkf', 'time': '2022-02-02 02:20:00'},
         {'description': 'habul', 'location': 'kehdj', 'time': '2022-02-02 02:20:00'}, {'description': 'sdf', 'location': 'sf', 'time': '2022-02-02 02:22:00'}]
duplicate_time = []
unique_time = []

for i in range(len(items)):
    print(f"i:{i}")
    for j in range(len(items)):
        if i != j:
            # print(f"j:{j}")

            if items[i]["time"] == items[j]["time"]:
                print(f"items[i]:{items[i]}")

                print(f"items[j]:{items[j]}")
                duplicate_time.append(items[j])
print(duplicate_time)
