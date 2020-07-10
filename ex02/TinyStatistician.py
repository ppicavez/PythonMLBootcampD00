import math


class TinyStatistician():

    def mean(self, datas):
        m = len(datas)
        if m == 0:
            return None
        sum = 0
        for i in range(m):
            sum = sum + datas[i]
        return sum / m

    def median(self, x):
        sorted_list = sorted(x)
        median_list = int(len(sorted_list) / 2)
        return float(sorted_list[median_list])

    def quartile(self, x, percentile):
        sorted_list = sorted(x)
        n_quartile = int(len(sorted_list) / 100 * percentile)
        return float(sorted_list[n_quartile])

    def var(self, datas):
        m = len(datas)
        if m == 0:
            return None
        sum = 0
        the_mean = self.mean(datas)
        for i in range(m):
            sum = sum + (datas[i] - the_mean) * (datas[i] - the_mean)
        return sum / m

    def std(self, datas):
        return math.sqrt(self.var(datas))
