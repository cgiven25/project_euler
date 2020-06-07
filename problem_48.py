# The problem: https://projecteuler.net/problem=48
# This problem is literally a joke for Python and requires zero outside thinking
# The most naive solution runs in .037s.  Literally broken

powers = [n**n for n in range(1, 1001)]
print(str(sum(powers))[-10:])