class Tennis:
    def __init__(self, p1, p2) -> None:
        self.player1 = p1
        self.player2 = p2
        self.playerMap = {self.player1: 0, self.player2: 0}
        self.scoreMap = {0: "love", 1: "fifteen", 2: "thrity", 3: "forty", 4: "win"}
        return

    def score(self) -> None:
        self.scoreCal()
        print(
            "{player1} {player2}".format(
                player1=self.scoreMap[self.playerMap[self.player1]],
                player2=self.scoreMap[self.playerMap[self.player2]],
            )
        )

    def scoreCal(self) -> list:
        player1Score = self.playerMap[self.player1]
        player2Score = self.playerMap[self.player2]

        if player1Score < 2 and player2Score < 2:
            return []

        elif player1Score == player2Score:
            if player1Score >= 3 or player2Score >= 3:
                return ["duce"]

        elif player1Score == 4:
            return []

        elif player2Score == 4:
            return []
        return []

    def clickButton(self, player) -> None:
        self.playerMap[player] = self.playerMap[player] + 1
        self.score()

    def clickButton1(self) -> None:
        # self.playerMap[self.player1] = self.playerMap[self.player1] + 1
        # self.score()
        self.clickButton(self.player1)

    def clickButton2(self) -> None:
        # self.playerMap[self.player2] = self.playerMap[self.player2] + 1
        # self.score()
        self.clickButton(self.player2)


if __name__ == "__main__":
    tennis = Tennis("Amy", "Tom")
    tennis.score()
