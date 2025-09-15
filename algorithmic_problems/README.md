# Algorithmic Problems

This section provides documented solutions to algorithmic problems from a
variety of popular platforms. Problems are organized by platform and further
arranged according to each platform’s indexing. Furthermore, each platform has
an `INDEX.md`, which contain problem sets grouped by categories or roadmaps,
which lists problems grouped by categories or roadmaps.

See the general [index](./INDEX.md) for problem sets from multiple platforms.

## Platforms

Competitive programming.

- [CodeForces](https://codeforces.com/)
- [ATCoder](https://atcoder.jp/)
- [CSES](https://cses.fi/)

Technical interview preparation.

- [Leetcode](https://leetcode.com/)
- [HackerRank](https://www.hackerrank.com/)
- [Codewars](https://www.codewars.com)

Math focused.

- [Project Euler](https://projecteuler.net/)

## Contributing

To maintain consistency and clarity, please follow these guidelines for
uploading problems:

> Tip: Read through some existing editorials to check and validate your own.

1. **Solution Code**
   - Each problem must include one or more proposed solutions.
   - Make sure to format the sources, read the
     [contributing](../CONTRIBUTING.md#devtools) on this.
   - Ignore redundant and unnecessary lines of code, like setup and cleanup code
     performed which is handled by the platform itself (e.g, imports in leetcode
     or IO in HackerRank), type annotations in loosely typed languages like
     Python, etc. This helps to avoid cluttering the solutions, and focusing on
     the relevant algorithmic code.

2. **Editorial**

   - Each problem must include an `editorial.md` file explaining each proposed
     solution.
   - The title of the editorial must be a link to the problem, using the
     markdown syntax `[ProblemID](URL)`.
   - The editorial should describe how to derive the solution, why it's correct
     and the asymptotic complexity analysis. This is required for every
     solution/approach in separate sections, specify which one by adding
     `(sol x)` to the section name, additional support sections may be added.
   - Every mathematical notation, including the asymptotic analysis, must be
     typesetted using latex snippets like `$O(n^2)$` (which renders $O(n^2)$).

3. **Directory structure**
   - All files for a problem must be placed in a directory named after the
     problem's ID:
     - For LeetCode: `number.name` (e.g., `1.two_sum`)
     - For Codeforces: `letter.name` (e.g., `A.way_to_success`)
   - If the platform allows indexed directories without conflicts (e.g.,
     Codeforces contests), you must create subdirectories accordingly. LeetCode
     does not support indexed subdirectories.

4. **File naming**
   - All file and directory names must not contain spaces.
   - Use underscores `_` instead of dashes `-` in names.
   - Avoid upper case on names.
