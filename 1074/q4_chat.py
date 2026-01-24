"""
use fast input as welll..

3 4 5 n
1 2 1

[1,2,1]

operations
1 4 -> increment index 1 by 4
2 4 -> increment index 2 by 4
3 3 -> increment index 3 by 3
2 0 -> increment index 2 by 0

Paul - run a simulation

h = 6 <- max that we can get t0

[1,2,1] start
[5,2,1] O(1)
[5,6,1] O(n) -> go back to [1,2,1]
[1,2,4] O(1)
[1,2,4] O(1) final

How do we optimize this o(n) operation for resetting?

Paul - maybe use mod math?
tenz
"""