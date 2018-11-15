# sphinx-gallery-extra

## What is this repository for?

[Sphinx-Gallery](https://github.com/sphinx-gallery/sphinx-gallery) lets you build galleries out of
your Python scripts. While sphinx-gallery has a lot of great functionality, there are always
new features that could be added! As the sphinx-gallery team needs to ensure that its package
remains stable for a diverse group of users, this can make it more difficult to try new ideas
in the core sphinx-gallery package.

This repository is for more experimental, still-evolving, or useful but out-of-scope features.
Its contents are **not** "officially" supported features of sphinx gallery, meaning that they
may not work in some Python versions, some documentation build systems, etc. However, we think
that having a place for this code will make it easier for the community to contribute in a
more fluid manner.

## How is this repository organized?

Currently, each sub-folder in this repository represents a different feature (or set of features)
with a common theme. For example, there is a folder called `scrapers` that has experimental
scraper code for images on disk. For other experimental scrapers, we'd love to see PRs to this folder!

If you'd like to contribute something that doesn't fit into one of the folders here, create a new one!
The goal of this project is to encourage more creativing and experimentation relative to the core
sphinx-gallery package.

