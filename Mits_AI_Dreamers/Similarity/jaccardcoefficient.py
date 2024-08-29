class JaccardCoefficient:
    """
        A class used to represent and compute the Jaccard Coefficient between two strings.

        Attributes
        ----------
        string1 : set
            The set of unique characters from the first string.
        string2 : set
            The set of unique characters from the second string.

        Methods
        -------
        findJaccardCoefficient():
            Computes and returns the Jaccard Coefficient between the two sets of characters.
        """
    def __init__(self, string1, string2):
        """
                Initializes the JaccardCoefficient class with two strings.

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

    def findJaccardCoefficient(self):
        """
        Computes the Jaccard Coefficient between the two sets of characters.

        The Jaccard Coefficient is defined as 1 minus the Jaccard Index, where
        the Jaccard Index is the size of the intersection divided by the size of the union
        of the two sets.

        Returns
        -------
        int
           The Jaccard Coefficient between the two sets of characters.
        """
        intersection = self.string1.intersection(self.string2)
        union = self.string1.union(self.string2)

        intersectionLength = len(intersection)

        unionLength = len(union)

        jaccardCoeff = intersectionLength/unionLength

        return jaccardCoeff



