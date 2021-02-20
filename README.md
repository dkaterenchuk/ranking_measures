## Ranking/Ordering Evaluation Measures

This package offers an implementation of the Rank Discounted Cumulative Gain (RankDCG) evaluation measure. This measure is designed to evaluate ranking-ordering algorithms. RankDCG had three fundamental properties: 1) consistent lower and upper score bounds (from 0 to 1), 2) it works with non-normal value distribution, and 3) it has transitivity property. For more detail see the paper ([RankDCG](http://arxiv.org/abs/1803.00719))

Bellow is the list of all measures available in this package:

* Rank Discounted Cumulative Gain (RankDCG) - a newly proposed measure
* Normalized Discounted Cumulative Gain (nDCG)
* Discounted Cumulative Gain (DCG)
* Average Precision (AP)
* Mean Average Precision (MAP)

NOTE: More ranking-ordering evaluation measures are available in sklearn and scipy packages. Scipy has an implementation of Kendall's tau (scipy.stats.kendalltau).

## Installation

Download the package and add ranking_measures directory to your python path or to your project folder.

## Usage

```python
from ranking_measures import measures

print measures.find_rankdcg([4,3,2,2,1], [3,4,2,2,1])
```

More example are in examples.py file.

## A high-level description of the usage for RankDCG:

Imagine you need to create a movie recommendation algorithm for a particular user. In your collection of movies, you have three items, [A, B, C] with some gold standard user preference scores assigned them. Ex:[A_9, B_3, C_1] Note: the movies can be in any order. Both [C_1, A_9, B_3] and [B_3, C_1, A_9] are valid inputs as long as the items are stationary. For simplicity, we separate movies from the ranks by creating two separate lists and map the positions from a movie to the corresponding score. Our new data will look as follows: movie list - [A, B, C], score list - [9, 3, 1]. After long sleepless nights you test your new algorithm to see these scores: [5,1,7]. How accurate are these recommendation scores? Here is how to find out:

```python
from ranking_measures import measures

# the function requires reference/gold standart list and hypothesis/prediction list
print measures.find_rankdcg([9,3,1], [5,1,7])

# 0.125 
```

The algorithm will map and the scores from the reference to the hypothesis and return an evaluation score. In this case, the score is 0.125, which is far from perfect. Keep working on your algorithm!

## Citation

Please cite if you use this evaluation in your research.
```python
@inproceedings{katerenchuk2016rankdcg,
  title={RankDCG: Rank-Ordering Evaluation Measure},
  author={Katerenchuk, Denys and Rosenberg, Andrew},
  booktitle={Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC 2016)},
  number={978-2-9517408-9-1},
  year={2016},
  organization={European Language Resources Association (ELRA)}
}
```

## Have questions or comments?

Email me: dkaterenchuk [ at ] gradcenter [dot] cuny [dot] edu
