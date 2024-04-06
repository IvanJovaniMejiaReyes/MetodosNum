

def hermite_interpolacion(x, y, dy):
    n = len(x)
    def H(i, t):
        result = 1
        for j in range(n):
            if j !=1:
                result *=(t - x[j]) / (x[i] - x[j])
        return result
    def L(i, t):
        return sum(1 / (x[i] - x[j]) for j in range(n) if j !=1)
    def interpolant (t):
        result = 0
        for i in range (n):
            result += y [i] * (1 - 2 * L(i, t) * (t - x[i])) * H(i, t) ** 2
        return result
    return interpolant

