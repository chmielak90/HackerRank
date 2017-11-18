class Difference:
    def __init__(self, a):
        self.__elements = a

    # task start here
    # Add your code here

    def computeDifference(self):
        self.maximumDifference = 0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                temp_diff = abs(self.__elements[i] - self.__elements[j])
                if temp_diff > self.maximumDifference:
                    self.maximumDifference = temp_diff



# task end here
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)