import json
#loading json data
try:
    data = [json.loads(line)
        for line in open("C:/Users/tharu/OneDrive/Documents/Big_Data_Project/Data/out.json", 'r', encoding='utf-8')]
except:
    print("Error occured while loading the json file")

with open("C:/Users/tharu/OneDrive/Documents/Big_Data_Project/Data/input_data.txt", "w+",encoding='utf-8') as f:

    for i in range(len(data)):
        x=data[i]["entities"]['hashtags']
        y=data[i]["entities"]['urls']
        if len(x)!=0:
            for m in range(len(x)):
                f.write(x[m]["text"] +"\n")
        if len(y)!=0:
            for n in range(len(y)):
                f.write(y[n]["expanded_url"] +"\n")

