##Ranking/Ordering Evaluation Measures

This package offers an implementation of the Rank Discounted Cumulative Gain (RankDCG) evaluation measure. This measure is designed to evaluate ranking-ordering algorithms. RankDCG had three fundamental properties: 1) consistent lower and upper score bounds (from 0 to 1), 2) it works with non-normal value distribution, and 3) it has transitivity property. For more detail see the paper ([RankDCG](http://www.dk-lab.com/wp-content/uploads/2014/07/RankDCG.pdf))

Bellow is the list of all measures available in this package:

* Rank Discounted Cumulative Gain (RankDCG) - a newly proposed measure t
* Normalized Discounted Cumulative Gain (nDCG)
* Discounted Cumulative Gain (DCG)
* Average Precision (AP)
* Mean Average Precision (MAP)

NOTE: More ranking-ordering evaluation measures are available in sklearn and scipy packages. Scipy has an implementation of Kendall's tau (scipy.stats.kendalltau).

##Installation
Download the package and add ranking_measures directory to your python path or to your project folder.

##Usage

```python
from ranking_measures import measures

print measures.find_rankdcg([4,3,2,2,1], [3,4,2,2,1])
```

More example are in examples.py file.

##Here is how RankDCG works:
Imagine you need to create a movie recommendation algorithm. In your collection you have three movies some gold standard scores are assigned it them. Ex:[A_9, B_3, C_1] Note: the movies can be in any order. Both [C_1, A_9, B_3] and [B_3, C_1, A_9] are valid inputs as long as the items are stationary.) For simplisity, we separate movies from the ranks by creating two separate lists and map the possitions from a movie to corresponing score. Our new data will look as follows: movies - [A, B, C], scores - [9, 3, 1]. If your new recommendation algorithm assignes new scores to the data, lets say [5,1,7], just call measures.findrankdgc() function with your god standard scores and predicted scores. The algorithm with map and the scores to its positions and evaluate the result.


Email me with any questions: dkaterenchuk [ at ] gradcenter [dot] cuny [dot] edu