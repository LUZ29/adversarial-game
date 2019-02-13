two-player adversarial game
================================
At the heart of a two-player adversarial game is the Minimax Algorithm. It tells us what the current (max) player’s best move is. Additionally, the alpha-beta pruning modification makes the overall algorithm more efficient.

manual solution
---------------
See manual solution in solution.pdf

how to use minimax_a_b.py
-------------------------
Use Python 3.6.6. Run "python minimax_a_b.py test_file_name" in command line. 

Result
------
For minimax, I give the final value and action should take and all nodes should be in this part. For alpha-beta, I give the visited nodes, pruning places, final value and action. If you need to see the nodes in minimax part, you only need to take off the "#" comment in line 75 and 88.

transcript
----------
    PS D:\workspace\2710\LUZ29-project2> python minimax_a_b.py test_tree1
    ******************************************
    ****************Minimax sol***************
    utility: 6
    move: B
    ******************************************
    **************Alpha-beta sol**************
    node: A
    node: B
    node: D
    node: H
    node: I
    node: E
    node: J
    node: K
    now pruning
    node: C
    node: F
    node: L
    node: M
    now pruning
    utility: 6
    move: B
    ******************************************
    PS D:\workspace\2710\LUZ29-project2> python minimax_a_b.py test_tree2
    ******************************************
    ****************Minimax sol***************
    utility: 6
    move: B
    ******************************************
    **************Alpha-beta sol**************
    node: A
    node: B
    node: D
    node: H
    node: I
    node: E
    node: J
    now pruning
    node: C
    node: F
    node: L
    node: M
    now pruning
    utility: 6
    move: B
    ******************************************
    PS D:\workspace\2710\LUZ29-project2> python minimax_a_b.py test_tree3
    ******************************************
    ****************Minimax sol***************
    utility: 3
    move: B
    ******************************************
    **************Alpha-beta sol**************
    node: A
    node: B
    node: E
    node: L
    node: M
    node: F
    node: N
    now pruning
    node: G
    node: P
    now pruning
    node: C
    node: H
    node: R
    node: S
    now pruning
    node: D
    node: J
    node: V
    node: W
    now pruning
    utility: 3
    move: B
    ******************************************
