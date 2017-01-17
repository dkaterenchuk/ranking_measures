##Ranking/Ordering Evaluation Measures

This package offers an implementation of the Rank Discounted Cumulative Gain (RankDCG) evaluation measure. This measure is designed to evaluate ranking-ordering algorithms. RankDCG had three fundamental properties: 1) consistent lower and upper score bounds, 2) it works with non-normal score distribution, and 3) it has transitivity property. For more detail see the paper ([RankDCG](http://www.dk-lab.com/wp-content/uploads/2014/07/RankDCG.pdf))

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
