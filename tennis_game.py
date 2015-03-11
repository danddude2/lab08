class TennisGame:
    def __init__(self):
        """
        This is the constructor for the TennisGame class. 
        You may need to write code here such as declaring some fields 
        to help with making your tests pass.
        """
        self.p1_score = 0
	self.p2_score = 0

    def score(self):
	if (self.p1_score == 0 & self.p2_score == 0):
		return "love - love"
	return ""

    def playerOneScored(self):
	self.p1_score += 1

    def playerTwoScored(self):
	self.p2_score += 1

    """
    It should not be necessary to create any other methods to complete the assignment.
    If you feel like creating some helper methods you are welcome to.
    """
