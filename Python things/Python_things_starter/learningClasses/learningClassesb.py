class num():
    def __init__(self, num):
        self.num = num
    
    def add(self, add_num):
        self.add_num = add_num
        return self.num + self.add_num

    def sub(self, sub_num):
        self.sub_num = sub_num
        return self.num - self.sub_num

    def mul(self, mul_num):
        self.mul_num = mul_num
        return self.num * self.mul_num

    def div(self, div_num):
        self.div_num = div_num
        return self.num / self.div_num

nihal_num = num(10)
print(
nihal_num.add(10),
nihal_num.sub(10),
nihal_num.mul(10),
nihal_num.div(10)
)
