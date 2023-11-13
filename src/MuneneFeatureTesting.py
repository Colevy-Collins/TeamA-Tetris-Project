from src.Difficulty import Difficulty

def main():
    difficulty1 = Difficulty.CreateDifficulty()
    print("Difficulty1 Speed: " + str(difficulty1.getAutoFallSpeed()))
    difficulty2 = Difficulty.CreateDifficulty()
    print("Difficulty2 Speed: " + str(difficulty2.getAutoFallSpeed()))
    difficulty2.increaseFallSpeed()
    difficulty2.increaseFallSpeed()

    print("Difficulty1 Speed: " + str(difficulty1.getAutoFallSpeed()))
    print("Difficulty2 Speed: " + str(difficulty2.getAutoFallSpeed()))


main()
