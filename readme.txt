In this project, you will find a Tetris game with the following features:

- Sound effects
- Background music
- Score tracking
- Dark mode
- Changeable color schemes
- Changeable difficulty
- Start UI
- Pauseability
- End UI

The core Tetris game is contained in the following files:

- TetrisBlock.py: contains a class for a Tetris block that defines the many blocks used
- TetrisBoard.py: contains a class for a Tetris board that creates the board to be played on
- TetrisBoardManager.py: contains a class that handles the behaviors of the blocks on the board
- TetrisBoardChecker.py: contains a class that handles verifying game rules, like when a line is filled

The features added on top of the core Tetris game are contained in the following files:

- Difficulty.py: This file contains a class for changing the block falling speed.
- Themes.py: This file contains all the color themes for the game.
- SoundManager.py: This file contains a class that provides the game with sound effects and background music.
- DataHandler.py: This file contains a class that handles the storing and retrieving of the score.
- TetrisStartMenu.py: This file contains a class that provides the starting UI for the game.
- TetrisEndMenu.py: This file contains a class that provides the ending UI for the game.
- TetrisPauseMenu.py: This file contains a class that provides the pause function and pause screen.

xButton.py: These files draw and provide the logic for their respective buttons. Use the name of the py file to match the button with the file.

The rest of each feature's implementations can be found inside TetrisBoardManager.py and TetrisBoardChecker.py.

The remaining files are interfaces, delegates, or minor in implementation.