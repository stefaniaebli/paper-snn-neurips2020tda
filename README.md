# DeepSphere: a graph-based spherical CNN

[Stefania Ebli](https://people.epfl.ch/stefania.ebli),
[Michaël Defferrard](https://deff.ch),
[Gard Spreemann](https://www.epfl.ch/labs/hessbellwald-lab) \
[Topological Data Analysis and Beyond workshop](https://tda-in-ml.github.io) at the [Conference on Neural Information Processing Systems (NeurIPS)](https://neurips.cc), 2020

> We present simplicial neural networks (SNNs), a generalization of graph neural networks to data that live on a class of topological spaces called [simplicial complexes].
> These are natural multi-dimensional extensions of graphs that encode not only pairwise relationships but also higher-order interactions between vertices—allowing us to consider richer data, including vector fields and n-fold collaboration networks.
> We define an appropriate notion of convolution that we leverage to construct the desired convolutional neural networks.
> We test the SNNs on the task of imputing missing data on coauthorship complexes.

```
@inproceedings{snn,
  title = {Simplicial Neural Networks},
  author = {Ebli, Stefania and Defferrard, Michaël and Spreemann, Gard},
  booktitle = {Topological Data Analysis and Beyond workshop at NeurIPS},
  year = {2020},
  archiveprefix = {arXiv},
  eprint = {2010.03633},
  url = {https://arxiv.org/abs/2010.03633},
}
```

## Resources

PDF available at [arXiv], [OpenReview].

Related: [code], [poster], [data].

[arXiv]: https://arxiv.org/abs/2010.03633
[OpenReview]: https://openreview.net/forum?id=Mg0DZl-Xe4
[code]: https://github.com/stefaniaebli/simplicial_neural_networks
[poster]: https://doi.org/10.5281/zenodo.4309827
[data]: https://doi.org/10.5281/zenodo.4144319

## Compilation

Compile the latex source into a PDF with `make`.
Run `make clean` to remove temporary files and `make arxiv.zip` to prepare an archive to be uploaded on arXiv.

## Figures

All the figures, along with the code and data to reproduce them, are in the [`figures`](figures/) folder.
While the PDFs are stored, they can be regenerated with `make figures`.

## Poster

A poster is in the [`poster_neurips`](poster_neurips/) folder.
It is compiled by `make` and a PDF is available at [`doi:10.5281/zenodo.4309827`][poster].

## Peer-review

The reviews, decision, and our answers are in [`review.md`](review.md) and on [OpenReview].

## History

* 2020-12-28: revision uploaded on arXiv (git tag `arxiv-20201228`)
* 2020-12-07: poster uploaded on OpenReview (git tag `poster-neurips`)
* 2020-12-01: revision uploaded on OpenReview (git tag `openreview-revised`)
* 2020-10-07: uploaded on arXiv (git tag `arxiv-20201007`)
* 2020-10-07: submitted to the TDA@NeurIPS workshop (git tag `neurips-submission`)

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
