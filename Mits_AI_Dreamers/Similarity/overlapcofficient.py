class overlapCoefficient:

    """
    A class used to represent and compute the Overlap Coefficient between two strings.

    Attributes
    ----------
    string1 : set
        The set of unique characters from the first string.
    string2 : set
        The set of unique characters from the second string.

    Methods
    -------
    findOverlapCoefficient():
        Computes and returns the Overlap Coefficient between the two sets of characters.
    """

    def __init__(self, string1, string2):

        """
        Initializes the OverlapCoefficient class with two strings.

        The strings are converted to sets of unique characters.

        Parameters
        ----------
        string1 : str
            The first string for comparison.
        string2 : str
            The second string for comparison.
        """

        self.string1 = set(string1)
        self.string2 = set(string2)

    def findOverlapCoefficient(self):

        """
        Computes the Overlap Coefficient between the two sets of characters.

        The Overlap Coefficient is defined as the size of the intersection divided
        by the size of the smaller set of the two. The coefficient is then subtracted
        from 1 to obtain the final result.

        Returns
        -------
        float
            The Overlap Coefficient between the two sets of characters.
        """

        intersection = self.string1.intersection(self.string2)

        string1length = len(self.string1)

        string2length = len(self.string2)

        intersectionLength = len(intersection)

        overlapIndex = intersectionLength / min(string1length,string2length)

        overlapCoeff = 1 - overlapIndex

        return overlapCoeff;




