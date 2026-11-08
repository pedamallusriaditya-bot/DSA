class Solution(object):
    def numTrees(self, n):
        def mul(a, b, m):
            res = [0] * m
            for i, ai in enumerate(a):
                if ai == 0 or i >= m:
                    continue
                for j, bj in enumerate(b):
                    if i + j >= m:
                        break
                    res[i + j] += ai * bj
            return res
        def inv(a, m):
            b = [a[0]]
            k = 1
            while k < m:
                k *= 2
                ab = mul(a[:k] + [0] * (k - len(a)), b, k)
                t = [-v for v in ab]
                t[0] += 2
                b = mul(b, t, k)
            return b[:m]
        C = [1]
        k = 1
        while k < n + 1:
            k *= 2
            C = C + [0] * (k - len(C))
            sq = mul(C, C, k)
            F = [0] + sq[:k - 1]
            F = [f - c for f, c in zip(F, C)]
            F[0] += 1
            Fp = [-1] + [2 * C[i - 1] for i in range(1, k)]
            step = mul(F, inv(Fp, k), k)
            C = [c - s for c, s in zip(C, step)]
        return C[n]