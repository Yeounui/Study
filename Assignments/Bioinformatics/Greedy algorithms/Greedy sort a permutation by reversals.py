class SignedPermutation():
    """
    >>> permutation = SignedPermutation(-3, +4, +1, +5, -2)
    >>> permutation
    SignedPermutation(-3, 4, 1, 5, -2)
    >>> print(permutation)
    (-3 +4 +1 +5 -2)
    >>> print(permutation.reversal(0, 3))
    (-1 -4 +3 +5 -2)
    >>> print(permutation.reversal(2, 4))
    (-3 +4 -5 -1 -2)
    >>> tuple(permutation.greedy_sort())
    ((0, 3), (0, 1), (1, 5), (2, 4), (3, 5), (3, 4), (4, 5))
    """
    def __init__(self, *args):
        self.currentPermutation= tuple(i for i in args)

    def __str__(self):
        string = ''
        for digit in self.currentPermutation:
            if digit >= 0:
                string += ' +'
            else:
                string += ' -'
            string += str(abs(digit))
        return '({})'.format(string.strip())

    def __repr__(self):
        permutation = [str(i) for i in self.currentPermutation]
        return 'SignedPermutation({})'.format(", ".join(permutation))

    def reversal(self, earlierPose, laterPose):
        reversedSlice = tuple(-i for i in self.currentPermutation[earlierPose:laterPose])
        reversedPermutation = self.currentPermutation[:earlierPose]\
                              + reversedSlice[::-1]\
                              + self.currentPermutation[laterPose:]
        return SignedPermutation(*reversedPermutation)

    def greedy_sort(self):

        permutation = SignedPermutation(*self.currentPermutation)
        currentPermutation = permutation.currentPermutation
        idealPermutation = tuple(i for i in range(1, len(self.currentPermutation)+1))
        reversalHistory = []

        for order in range(len(self.currentPermutation)):
            if order+ 1 != currentPermutation[order]:
                for digitPos, digit in enumerate(currentPermutation):
                    if abs(digit) == order + 1:
                        permutation = permutation.reversal(order, digitPos+1)
                        currentPermutation = permutation.currentPermutation
                        reversalHistory.append((order, digitPos+1))
                        if currentPermutation[order] < 0:
                            permutation = permutation.reversal(order, order+1)
                            currentPermutation = permutation.currentPermutation
                            reversalHistory.append((order, order+1))
                        if currentPermutation != idealPermutation:
                            break
                        return reversalHistory

