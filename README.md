# Quine-McCluskey
> A Python/C++ implementation of Quine McCluskey(Tabulation) method to minimise boolean functions.

### Folder Structure:
- `tabulation.py` : Python3 implementation of the algorithm
- `tabulation.cpp`: C++ implementation of the algorithm
- `pla.py` : solves a `programmable logic array`. It uses tabulation to find possible solutions of n provided functions and then calculates the least combination that solves all functions.

###### NOTE: pla.py is buggy
The C++ implementaion is more readable and slightly more optimized.

### Algorithm
- The Quine McCluskey algorithm reference is [here](https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm)
- Once the prime implicants are obtained, I have used [Petrick Method](https://en.wikipedia.org/wiki/Petrick%27s_method) for minimisation.

### Screenshots
- Python3:

![Python3 Tabulation](https://github.com/mohdomama/Quine-McCluskey/blob/master/screenshots/PythonTab.png)

- C++:

![C++ Tabulation](https://github.com/mohdomama/Quine-McCluskey/blob/master/screenshots/C%2B%2BTab1.png)
![C++ Tabulation](https://github.com/mohdomama/Quine-McCluskey/blob/master/screenshots/C%2B%2BTab2.png)

###### I have given a more verbose output with C++
