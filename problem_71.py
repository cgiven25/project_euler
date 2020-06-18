# The problem: https://projecteuler.net/problem=71
# Numerator and denominator must be relatively prime.
# Idea -- 3/7 = .428571...
#	The answer will be close to 428571/1000000 (the only way this can be wrong is if it's too small)
# 	If it's too small, then we should try subtracting the denominator until we get something bigger, but still less than 3/7.
# We can reasonably do this by hand.
# 428571/999999 ~= 3/7, but since 428571 isn't the answer, this is larger than 3/7.
# 428570/999999 = does not fulfill the criteria
# 428570/999998 does not fulfill the criteria
# 428570/999995 does, and is smaller, so this must be the smallest one

# I basically did have this approach already, but I DID look up the answer to this one.
# I was surprised to find out that 428571 was not the right answer.