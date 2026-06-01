# Active Memory Issue

Expected flow:

1. Reply starts.
2. Active Memory recall starts.
3. Recall finishes.
4. Reply uses the memory.
5. Reply finishes.

Broken flow:

1. Reply starts and takes the `main` lane.
2. Reply asks Active Memory to do recall.
3. Recall also tries to take the `main` lane.
4. Recall cannot start because reply is still holding `main`.
5. Reply cannot continue because it is waiting for recall.
6. Timeout happens.

The issue is that recall sometimes does not run and finish first.

It waits in line behind the reply that is waiting for it.
