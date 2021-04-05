f = open('ports.txt','r')
s = f.read().split()
num=[]
tec_nem=0
class mersenne_rng(object):
    def __init__(self, seed=5489):
        self.state = [0] * 624
        self.f = 1812433253
        self.m = 397
        self.u = 11
        self.s = 7
        self.b = 0x9D2C5680
        self.t = 15
        self.c = 0xEFC60000
        self.l = 18
        self.index = 624
        self.lower_mask = (1 << 31)-1
        self.upper_mask = 1 << 31

        # update state
        self.state[0] = seed
        for i in range(1, 624):
            self.state[i] = self.int_32(self.f * (self.state[i-1] ^ (self.state[i-1] >> 30)) + i)

    def twist(self):
        for i in range(624):
            temp = self.int_32((self.state[i] & self.upper_mask) + (self.state[(i+1) % 624] & self.lower_mask))
            temp_shift = temp >> 1
            if temp % 2 != 0:
                temp_shift = temp_shift ^ 0x9908b0df
            self.state[i] = self.state[(i+self.m) % 624] ^ temp_shift
        self.index = 0

    def get_random_number(self):
        if self.index >= 624:
            self.twist()
        y = self.state[self.index]
        y = y ^ (y >> self.u)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> self.l)
        self.index += 1
        return self.int_32(y)

    def int_32(self, number):
        return int(0xFFFFFFFF & number)

for i in range(len(s)):
    if s[i][-4:] == '2222':
        temp1 = s[i-1].split('--')[1]
        temp2 = s[i-2].split('--')[1]
        o1 = int(temp1) << 16
        o2 = int(temp2)
        num.append(o1+o2)

for i in range(100000):
    rng = mersenne_rng(1131464071)
    number = rng.get_random_number()
    if number == num[0]:
        print(i)
        for j in range(625):
            number = rng.get_random_number()
            port1 = (number & (2 ** 32 - 2 ** 16)) >> 16
            port2 = number & (2 ** 16 - 1)
            print(str(port1)+" "+str(port2))
