import numpy as np
from matplotlib import pyplot as plt
f=open('superose6_50.asc.txt')
lines=f.readlines()
f.close()
t=[]
a=[]
for line in lines[3:]:
    words=line.split()
    try:
        t.append(float(words[0]))
        a.append(float(words[1]))
    except:
        print("Could not parse", line)
        continue

t=np.array(t)


a=np.array(a)
d=np.gradient(a)
d2=np.gradient(d)

# Hard code a threshold to distinguish from noise
# in practice more data would be needed to automatically do this
min_ = 50

# Find where the sign in the first derivative changes
indices = np.where(np.diff(np.sign(d)))[0]
# The peaks are where the second derivative is negative and the point should not be noise
peaks = [i for i in indices if (d2[i] < 0 and a[i] > min_)]

'''
    Finds an edges of a peak by moving left and right starting at the peak
    A threshold parameter is used to filter the derivative

'''
def find_edges(peak, threshold=0.1):
    # Get the derivative for left and right side of peak
    left = d[:peak][::-1]
    right = d[peak+1:]

    # Find first occurrence of sign change in derivative
    for i, p in enumerate(left):
        if p < 0 or p < threshold:
            left_edge = peak - i
            break

    for i, p in enumerate(right):
        if p > 0 or p > -threshold:
            right_edge = peak + i
            break

    return left_edge, right_edge

# Loop through peaks, find edges, and plot
for p in peaks:
    le, re = find_edges(p)
    plt.scatter(t[p], a[p], c='r')
    plt.axvline(t[le], ls='--', c='black')
    plt.axvline(t[re], ls='--', c='black')
    print('Peak at {}. Range: [{}, {}]'.format(t[p], t[le], t[re]))


plt.plot(t,a, label='data')
plt.legend()
plt.show()
