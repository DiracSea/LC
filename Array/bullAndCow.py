class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = sum(map(operator.eq, secret, guess)) 
        both = sum(min(secret.count(x),guess.count(x)) for x in set(guess))
        return '%dA%dB' % (bull, both - bull)
                    