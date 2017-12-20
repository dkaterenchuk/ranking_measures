"""examples.py: an example code for running rank-ordering evaluation package
=========================================================================

ranking_eval is a set of common ranking algorithms such as:
*dcg
*ndcg
*precision
*precision_k
*average_precision
*rankdcg

RankDCG is described in this paper:
"RankDCG: Rank-Ordering Evaluation Measure," Denys Katerenchuk, Andrew Rosenberg
http://www.dk-lab.com/wp-content/uploads/2014/07/RankDCG.pdf
"""

__author__ = "Denys Katerenchuk, The Graduate Center, CUNY"

__license__ = """The MIT License (MIT)

Copyright (c) [2015] [Denys Katerenchuk]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


__version__ = "1.0.1"

import measures



def test_measures(reference, hypothesis):
    """
    Runs all rank-ordering evaluation measures on given pair of lists.
    """

    print("\t DCG:\t\t\t{0}".format(measures.find_dcg(hypothesis)))
    print("\t nDCG:\t\t\t{0}".format(measures.find_ndcg(reference, hypothesis)))
    print("\t Precision:\t\t{0}".format(measures.find_precision(reference, hypothesis)))
    print("\t Precision at k:\t{0}".format(measures.find_precision_k(reference, hypothesis, len(reference))))
    print("\t Average precision:\t{0}".format(measures.find_average_precision(reference, hypothesis)))
    print("\t RankDCG:\t\t{0}".format(measures.find_rankdcg(reference, hypothesis), "\n"))

#Defining test cases
L1 = [9, 4, 4, 2, 2, 2, 1, 1, 1, 1]
L2 = [9, 4, 4, 2, 2, 1, 2, 1, 1, 1]
L3 = [4, 4, 2, 9, 2, 2, 1, 1, 1, 1]
L4 = [1, 4, 4, 2, 2, 2, 9, 1, 1, 1]
L5 = [1, 4, 4, 2, 2, 2, 1, 1, 1, 9]
L6 = [1, 1, 1, 1, 2, 2, 2, 4, 4, 9]

#Testing:
print("1. Perfect ordering:")
test_measures(L1, L1)

print("2. Slightly wose case (low ranks):")
test_measures(L1, L2)

print("3. Further worsen case (hight ranks):")
test_measures(L1, L3)

print("4. Placement of a high rank element into the low rank 'subgroup':")
test_measures(L1, L4)

print("5. Case #4 but with further misplacement of the hight rank element inside the low rank 'subgroup':")
test_measures(L1, L5)

print("6. The worst case (reverse ordering):")
test_measures(L1, L6)


