import csv

class Data():

    def __init__(self):
        self.masse = 108.280
        self.volume = 140
        self.datas = []
        self.dict = {}
        self.CO2 = []
        self.temp = []
        self.time = []
        self.humidity = []
        self.min = {"CO2":9e99,"temperature":9e99,"humidity":9e99,"time":9e99}
        self.max = {"CO2":-9e99,"temperature":-9e99,"humidity":-9e99,"time":-9e99}

    def new(self, data):
        self.data = data
        self.data = self.data.replace(" ","").replace('\r',"").replace("\n","")
        self.data = self.data.split('/')
        for i in range(len(self.data)) : self.data[i] = self.data[i].split(':')
        self.data = self.data[1:]
        for d in self.data : self.dict[d[0]] = d[1]
        if len(self.dict) != 4 : return None
        self.datas.append(self.dict)
        self.CO2.append(self.dict["CO2"])
        self.temp.append(self.dict["temperature"])
        self.humidity.append(self.dict["humidity"])
        self.time.append(self.dict["time"])
        for k in self.dict.keys():
            if float(self.dict[k]) > float(self.max[k]) : self.max[k] = self.dict[k]
            elif float(self.dict[k]) < float(self.min[k]) : self.min[k] = self.dict[k]

        return tuple(self.dict.values()), tuple(self.min.values()), tuple(self.max.values())

    def save_csv(self):
        with open('exp1.csv', "w") as c:
            self.header, self.data = [], []
            writer = csv.writer(c)
            writer.writerow(["time","CO2","temp","humidity"])

            for d in range(len(self.datas)) :
                for v in self.datas[d].values():
                    self.data.append(v)
                writer.writerow(self.data)
                self.data = []

