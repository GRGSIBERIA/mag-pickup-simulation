#-*- encoding: utf-8
import numpy as np

# f0 = V / 2l
# 1 / 2l = f0 / V
# 1 / l = 2 f0 / V
# l = V / 2 f0

def length(f0):
    V = 331.45
    return V / (2*f0)

def pitch(n, concertPitch=440):
    return 440. * 2.**((n-49)/12)

if __name__ == "__main__":
    # +1しているのはバルブ全押しで8になるから
    nums = np.arange(15, 15+(12*3)+1, 1)
    freqs = [pitch(n) for n in nums]
    lengthes = [length(freq) for freq in freqs]
    print(lengthes)
    for i in range(len(lengthes)-1):
        print(lengthes[i]-lengthes[i+1])