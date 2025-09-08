# 1317. Convert Integer to the Sum of Two No-Zero Integers

### Naive Solution

We can iterate over every pair of numbers $(a\,b)$ such that $a+b=n$, and check
if either $a$ or $b$ have any zero digits, doing this would have $O(nlogn)$
complexity, as going over the digits of a number takes $O(logn)$.

### Sum by Cases of Digits

A more efficient approach would be to iterate through the digits of $n$, and
pick two digits which adds up to the digit of $n$ minus the carry, we consider
four cases of $t=d-c$, where $d$ is the digit of $n$ and $c$ is the carry.

$$
\begin{cases}
a+b = 10 \quad(a=1, b=9, c=1)   & \text{if $t = 0$}, \\
a+b = 11 \quad(a=2, b=9, c=1)   & \text{if $t = 1$}, \\
a+b = 9  \quad(a=1, b=8, c=0)   & \text{if $t = -1$}, \\
a+b = t  \quad(a=1, b=t-1, c=0) & \text{if $2 \le t \le 9$}.
\end{cases}
$$

As we can see the cases are exhaustive, the only detail left is that the last
digit sum cannot have a carry, in that case $t$ can just be added as the last
digit of $a$ or $b$. This approach would take $O(logn)$ complexity, as we only
iterate over the digits of $n$.
