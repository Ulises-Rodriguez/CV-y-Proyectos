'''
Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.


'''
import statistics as st
import numpy as np


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]


class Statistics:
    def __init__(self, ages) -> None:
        self.array = ages

    def sum(self):
        return sum(self.array)

    def mean(self):
        return st.mean(self.array)

    def mediana(self):
        return st.median(self.array)

    def q1(self):
        return np.percentile(self.array, 25)

    def q3(self):
        return np.percentile(self.array, 75)

    def range_percentile(self):
        rp = self.q3() - self.q1()
        return rp

    def variance(self):
        return st.variance(self.array)

    def standard_desviation(seflt):
        return st.stdev(seflt.array)

    def mode(self):
        return st.mode(self.array)

    def min(self):
        return min(self.array)

    def max(self):
        return max(self.array)

    def range(self):
        value_range = max(self.array) - min(self.array)
        return value_range

    def count(self):
        return len(self.array)

    def freq_dist(self):
        return sorted([(self.array.count(i) * 4.0, i) for i in set(self.array)], reverse=True)

    def info(self):
        aux = "count = {}, sum = {}, mean = {}, mediana = {}, q1 = {}, q3 = {}, rp = {}, variance = {}, sd = {}, mode = {}, min = {}, max = {}, range = {}, fq = {}".format(self.count(), self.sum(), self.mean(
        ), self.mediana(), self.q1(), self.q3(), self.range_percentile(), self.variance(), self.standard_desviation(), self.mode(), self.min(), self.max(), self.range(), self.freq_dist(),)

        return aux


data = Statistics(ages)

print(data.array)
print(data.count())
print(data.info())
print()

'''
Create a class called PersonAccount. It has firstname, lastname, email, cell, food, color, animal
'''


class PersonAccount():
    def __init__(self, firstname, lastname, email, cell, food, color) -> None:
        self.name = firstname + " " + lastname
        self.email = email
        self.cell = cell
        self.food = food
        self.color = color
        self.skills = []

    def account_info(self):
        info = "name : {}\n email : ${}\n cell : ${}\n food : ${}\n color : ${}, skills : ".format(
            self.name, self.email, self.cell, self.food, self.color, self.skills)
        return info

    def add_skill(self, skill):
        self.skills.append(skill)


p1 = PersonAccount("Tino", "Machichita", 45, 55, 65, 75)

print(p1.account_info())

p1.add_skill("HTML")
p1.add_skill("CSS")
p1.add_skill("JS")

print(p1.skills)
