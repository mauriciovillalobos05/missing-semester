121. Best Time to Buy and Sell Stock
Naive Solution

Try every pair of days (i, j) with i < j: buy on day i, sell on day j, compute prices[j] - prices[i], and keep the maximum.

Correctness: Enumerates all valid single transactions.
Complexity: O(n^2) time, O(1) space — too slow for large inputs.

Sliding Window (Two Pointers)

Maintain a left pointer L as the candidate buy day and move a right pointer R as the current sell day scanning left-to-right:

If prices[R] >= prices[L]:
The window [L, R] yields profit prices[R] - prices[L]. Update the best profit and continue advancing R.

If prices[R] < prices[L]:
The current price is a better (cheaper) buy. Reset the window by setting L = R, then continue.

This keeps prices[L] as the minimum seen so far in the active window, ensuring the buy happens before the sell and capturing the best rise after each dip.

Complexity: O(n) time, O(1) space.
