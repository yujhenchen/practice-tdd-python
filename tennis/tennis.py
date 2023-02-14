class Tennis:
    def __init__(self) -> None:
        self.scoreMap = {0: "love", 1: "fifteen"}

    def get_result(self, player1Scores, player2Scores) -> str:
        if player1Scores == player2Scores:
            return "love all"

        return "{scoreStr1} {scoreStr2}".format(
            scoreStr1=self.scoreMap[player1Scores],
            scoreStr2=self.scoreMap[player2Scores],
        )
