# partition-of-a-set-in-Python
A Python 3 script that generates the set of all [partitions](https://en.wikipedia.org/wiki/Partition_of_a_set) of a given non-empty set.

## How it works?
This program arises from the idea of constructing the set *P(S)* of all partitions of a finite set *S* from the set *P(S \\{x})*, where *x* is an arbitrary element of *S*.

If *S* is a [singleton](https://en.wikipedia.org/wiki/Singleton_(mathematics)), then *P(S) = {{x}}*. To build *P(S)* for bigger sets, we first build *P(S\\{x})* and then do two things:

First, for each partition in *P(S\\{x})*, we constitute a new partition for *S* by adding a new [class of equivalence](https://en.wikipedia.org/wiki/Equivalence_class), namely *{x}*. The set of all these partitions is the set *R*, in the image below;

Second, for each partition *A* in *P(S\\{x})*, we create [*#A*](https://en.wikipedia.org/wiki/Cardinality) new partitions by adding *x* to each class of equivalence. The resulting set is the set *Q* below.

Formally speaking, it uses the following recursive definition of the set of all partitions of a finite set:

Let *P(S)* be the set of all partitions of the set *S8. If *S = {a}*, then *P(S) = {{a}}*. If *#P(S) > 1*, then *P(S) = R &#8899; Q*. Where

![](https://github.com/ArthurHDRodrigues/partition-of-a-set-in-Python/blob/main/partition2.jpeg)


## Example
I will add this one day, I promise
