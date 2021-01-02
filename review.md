# Peer-review at the Topological Data Analysis and Beyond workshop at NeurIPS'2020

## Decision

Paper Decision
NeurIPS 2020 Workshop TDA and Beyond Program Chairs
30 Oct 2020 (modified: 31 Oct 2020)
NeurIPS 2020 Workshop TDA and Beyond Paper30 Decision
Readers: Everyone

Decision: Accept (Poster)
Comment: Reviewers agreed that this would make a good addition to the workshop, hence we suggest a poster presentation.

## Review 3

Review of "Simplicial Neural Networks"
NeurIPS 2020 Workshop TDA and Beyond Paper30 AnonReviewer2
27 Oct 2020 (modified: 31 Oct 2020)
NeurIPS 2020 Workshop TDA and Beyond Paper30 Official Review
Readers: Program Chairs, Paper30 Reviewers Submitted, Paper30 Authors

Review:

This paper generalizes graph neural networks to simplicial complexes. The two main contributions are simplicial complexes as input data and the extension of the definition of convolution. The experiment is based on real-world data: a coauthorship complex.

The paper is well written and detailed although not self-contained, and provides a natural extension of graph neural networks to a higher dimensional data structure. The authors claim that they expect this approach to be far better to hypergraph neural networks. It would have been interesting if they provided an experimental comparison between both architectures.

Finally, I find the paper a significant contribution and a natural introduction of computational topology into artificial intelligence methods.

Rating: 2: Accept as poster presentation
Confidence: 5: The reviewer is absolutely certain that the evaluation is correct and very familiar with the relevant literature

## Review 2

Promising work on neural network convolution on simplicial complexes
NeurIPS 2020 Workshop TDA and Beyond Paper30 AnonReviewer3
27 Oct 2020 (modified: 31 Oct 2020)
NeurIPS 2020 Workshop TDA and Beyond Paper30 Official Review
Readers: Program Chairs, Paper30 Reviewers Submitted, Paper30 Authors

Review:

**Summary of the paper**
The authors present a new form of neural networks, based on an intrinsic construction of simplicial complexes and the learning of corresponding weights during the simplicial convolution. A layer using simplicial convolution is defined as the composition of the inverse Fourier-transformed $\mathcal{F}_k^{-1}$ of real $k$-co-chains, with a low-order polynomial, whose parameterization is set to mimic frequencies in the domain through such filters. The result is applied with the convolution operation to the co-chains of a simplicial complex, the data domain, and finally chained with a nonlinear activation function with bias term. As an experiment, a data set on authorships and co-authorships of scientific articles was chosen, from which some entries were replaced by constants and the missing citations were imputed. For this purpose 4-rates of missing values on the co-chains of a co-authoring complex were artificially generated, of 10, 20, 30 and finally 50 each. The $L_1$ norm was trained on a corresponding complex with known citations. Simplicial neural networks are therefore capable of imputing data after experimental evaluation and also show the applicability of transfer learning to problems of the same domain.

**Strengths**
* The abstract is brief and informative. Also the introduction is mostly clearly motivated and reflects the relevant literature. The elaboration of the simplicial convolution is motivated by related work in signal processing.
* Very good is the observation that the Laplacians of simplicial complexes in the $k$th dimension are isomorphic to the $k$th cohomology group of the associated simplicial complex. For such networks this gives a favourable possibility of investigation by homological methods.
* The choice of low order polynomials is very well motivated with three crucial aspects, namely by an efficient implementation with $n$-sparsely coded matrix-vector multiplications, by the reduction of computational complexity and by the property of $n$-localisation, so that if two simplices are more than $n$-steps apart, a convolution layer of degree $n$ will not learn any interaction between the two simplices. It is worth mentioning, that this is elaborated in the appendix.

**Weaknesses**
* The simplicial complexes are not naturally limited to pairwise relations, in contrast to graph neural networks. Furthermore the computational complexity is given to $\mathcal{O}(\xi |K_k|)$ for a simplicial complex $K$ and a density factor $\xi$. It would be interesting here to compare this directly with graph-neural networks for the computational complexity and to use empirically also such an experiment. Unfortunately, the advantage of this method is not worked out explicitly by means of comparative examples for graph neural networks or conventional convolution networks.
* When reading the paper, the vector field problem seemed to me to be the most interesting one, but this was only briefly addressed in the abstract and again in the final part of the paper. But no concrete idea was deposited.
* The orientation of the simplicial complexes is not discussed. But this is an important point, as it seems to me, because non-orientatable domains could probably cause problems in learning. How would one deal with this?
* The third point of the strengths listed above also seems to be a weakness. In the introduction there is some discussion about the global topological structure. But this seems not to be really taken up in learning, as long as the degree of the polynomial is smaller or equal than a $n$-sequence of $k$-co-chains?

All in all, none of these weaknesses seem to me to be somehow serious, much more than an opportunity to write further work in this direction and develop the approach. Nevertheless, there are weaknesses which at least for me reveal ambiguities and questions, which is why I rate the paper in its current form with a 2: Accept as a poster presentation.

Rating: 2: Accept as poster presentation
Confidence: 4: The reviewer is confident but not absolutely certain that the evaluation is correct

## Review 1

Laplacian => convolutional layer: here, * = "simplicial"
NeurIPS 2020 Workshop TDA and Beyond Paper30 AnonReviewer1
25 Oct 2020 (modified: 31 Oct 2020)
NeurIPS 2020 Workshop TDA and Beyond Paper30 Official Review
Readers: Program Chairs, Paper30 Reviewers Submitted, Paper30 Authors

Review:

This work is interesting and thought provoking; it highlights a recurring theme of workshop submissions (on that see more below) that one can use a Laplacian to define a convolutional layer on a sophisticated data structure. The basic idea of using the spectral theory of the Laplacian to define a convolution operator seems elegant and sound, though I haven't checked the details by hand. I was initially very excited reading this paper, but my excitement was slightly tempered for reasons mentioned below.

I am a little confused by the left panel of Figure 2: if the accuracy of reconstruction is almost exactly 1-(% missing data) then that must mean something. I am assuming that this means something considerably better than random guessing but must admit it seems as if the latter is a plausible reading. Again, I think I am being obtuse here but could not say for certain, which suggests to me that at a minimum the "clarification" in the supplementary material should be more verbose.

Notwithstanding the imputation of missing data, I am a little at a loss as to what the applications of these things might look like in practice. As the authors state, their example can be easily viewed as a Dowker complex corresponding to a suitable relation (of course this is true of any finite simplicial complex, but, e.g. doing this sort of translation with a Vietoris-Rips complex might strain one's imagination a bit more, which of course is the point of a preferred data representation), and one could just as well consider this as a bipartite graph. It is not clear to me what the advantage of the simplicial data structure is here--I do not doubt that there is some advantage in certain applications, but I don't know what form those would take. Perhaps there are applications to databases, but I could not say.

The only other thing that prevents me from assigning the higher rating is the panoply of related submissions to the workshop that cover very similar terrain, e.g., cell complex neural networks, sheaf neural networks, topological CNNs, etc. In particular, if one is striving for generality and a unifying perspective on these various constructs, it seems hard to beat the sheaf NN--if there is a more general construct than a sheaf that admits a Laplacian then that would be news to me.

Rating: 2: Accept as poster presentation
Confidence: 4: The reviewer is confident but not absolutely certain that the evaluation is correct

### Answer

Clarification on the computation of the accuracy
NeurIPS 2020 Workshop TDA and Beyond Paper30 Authors Stefania Ebli (privately revealed to you)
27 Nov 2020
NeurIPS 2020 Workshop TDA and Beyond Paper30 Official Comment
Readers: Program Chairs, Paper30 Reviewers Submitted, Paper30 Authors

Comment:

We thank the reviewer for the useful feedback.

We would like to reply in regards to the doubts about the computation of the accuracy of the network. We would like to point out that the accuracy has been computed only on the unknown values as explained in the section Supplementary Material, paragraph 'Mean accuracy and absolute error'. Since the known values are not considered in this computation, it means that the prediction of the missing values is considerably better than random guessing. We agree that it is interesting that, even if the accuracy is computed only on the missing values, it is close to 100-(%missing data). We will further investigate this phenomena in our future work.
