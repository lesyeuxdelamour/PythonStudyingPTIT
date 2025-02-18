def _sinusoid_():
    for _ in range(int(input())):
        n = int(input())
        a = sorted(list(map(int, input().split())))
        cnt = 0
        for i in range(0, n - 2):
            l, r = i + 1, n - 1
            while l < r:
                total = a[i] + a[l] + a[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    cnt += 1
                    l += 1
                    # test case sai
                    # if a[l] == a[r]:
                    #         cnt += (r - l + 1) * (r - l) // 2
                    #         break
                    # else:
                    #     leftCnt, rightCnt = 0, 0
                    #     left, right = a[l], a[r]
                    #     while l <= r and a[l] == left:
                    #         l += 1
                    #         leftCnt += 1
                    #     while r >= l and a[r] == right:
                    #         r -= 1
                    #         rightCnt += 1
                    #     cnt += leftCnt * rightCnt
        print(cnt)

if __name__ == "__main__":
    _sinusoid_()