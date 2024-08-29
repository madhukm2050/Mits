class HammingDistance:
    """
    A class used to represent and compute the Hamming Distance between two strings.

    Attributes
    ----------
    string1 : str
        The first string for comparison.
    string2 : str
        The second string for comparison.

    Methods
    -------
    findHammingDistance():
        Computes and returns the Hamming Distance between the two strings.
    """
    def __init__(self, string1, string2):
        """
        Initializes the HammingDistance class with two strings.

        Parameters
        ----------
        string1 : str
            The first string for comparison.
        string2 : str
            The second string for comparison.
        """
        self.string1 = string1
        self.string2 = string2

    def findHammingDistance(self):
        """
        Computes the Hamming Distance between the two strings.

        The Hamming Distance is defined as the number of positions at which the
        corresponding characters in the two strings are different. If the lengths
        of the two strings are not equal, an error message is returned.

        Returns
        -------
        int
            The Hamming Distance between the two strings.
        str
            An error message if the lengths of the strings are not equal.
        """
        str1 = self.string1
        str2 = self.string2

        if len(str1) != len(str2) : return "Both the Strings should be equal"

        distance = 0

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                distance+=1

        return self.printdistance(str1,str2,distance)

    def printdistance(self, string1, string2, distance):
        print("The jaccordCoefficent between the strings",string1, "and ",string2," is ",distance)



