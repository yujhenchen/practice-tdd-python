from player_score import PlayerScore


class Tennis:
    def __init__(self, playerScore: PlayerScore) -> None:
        self.score_map = {0: "love", 1: "fifteen"}
        self.score = playerScore

    def player1_scores(self) -> None:
        self.score.player1 = self.score.player1 + 1

    def player2_scores(self) -> None:
        self.score.player2 = self.score.player2 + 1

    def get_result(self) -> str:
        if self.score.player1 == self.score.player2:
            return "love all"
        return (
            f"{self.score_map[self.score.player1]} {self.score_map[self.score.player2]}"
        )
