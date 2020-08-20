Feature: Game 2048

  Scenario Outline: move
    Given the game have a series of numbers <numbers>
    When the player give a command <cmd>
    Then the series should be changed to <new>

    Examples: move
      | numbers                                                  | cmd | new                                                       |
      | [[4, 2, 4, 2],[2, 2, 4, 0],[0, 4, 2, 4],[0, 0, 2, 2]]    | a   | [[4, 2, 4, 2], [4, 4, 0, 0], [4, 2, 4, 0], [4, 0, 0, 0]]  |
      | [[4, 2, 4, 2], [4, 4, 0, 0], [4, 2, 4, 0], [4, 0, 0, 0]] | d   | [[4, 2, 4, 2], [0, 0, 0, 8], [0, 4, 2, 4], [0, 0, 0, 4]]  |
      | [[4, 2, 4, 2], [0, 0, 0, 8], [0, 4, 2, 4], [0, 0, 0, 4]] | w   | [[4, 2, 4, 2], [0, 4, 2, 8], [0, 0, 0, 8], [0, 0, 0, 0]]  |
      | [[4, 2, 4, 2], [0, 4, 2, 8], [0, 0, 0, 8], [0, 0, 0, 0]] | s   | [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 4, 2], [4, 4, 2, 16]] |

