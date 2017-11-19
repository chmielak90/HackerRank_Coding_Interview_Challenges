# n = int(input().strip())
#
# a = []
# a_i = 0
#
# for a_i in range(n):
#     a_t = int(input().strip())
#     a.append(a_t)
#
#     a = sorted(a, key=int)
#
#     if len(a) % 2 == 0:
#         print((a[int(len(a)/2)] + a[int(len(a)/2)-1])/2)
#
#     else:
#         print(float(a[int(len(a)/2)]))


# this up working but to slow

from bisect import insort

# n = int(input().strip())
a = []
# a_i = 0


def median(a):
    med = 0
    if len(a) % 2 == 0:
        l = a[len(a) // 2];
        r = a[(len(a) // 2) - 1]
        med = (l + r) / 2.0

    elif len(a) % 2 != 0:
        med = a[len(a) // 2]
    return med


if __name__ == '__main__':
    heap = []
    for _ in range(int(input())):
        insort(heap, int(input()))
        print(float(median(heap)))