# partition-of-a-set-in-Python
A Python 3 script that generates the set of all [partitions](https://en.wikipedia.org/wiki/Partition_of_a_set) of a given non-empty set.

## How it works?
It uses the following recursive definition of the set of all partitions of a finite set:

Let P(S) be the set of all partitions of the set S. If S = {a}, then P(S) = {{a}}. If #P(S) > 1, then P(S) = R &#8899; Q. Where

![](https://github.com/ArthurHDRodrigues/partition-of-a-set-in-Python/blob/main/partition.jpeg)

R essencially adds the new [class of equivalence](https://en.wikipedia.org/wiki/Equivalence_class) {x} to each partition A in P(S\{x}) and Q adds x to each class of each existent partition in P(S\{x}).


## Example
I will add this tomorrow, I promise
