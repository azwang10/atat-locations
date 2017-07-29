# atat-locations

Determines the location of ATAT boxes, the complement of TATA boxes, within half of all genes in the E. coli genome. All genes are given the same scale with location 0 being the start site and location 1 being the stop site.

It was hypothesized that more ATAT boxes would be located at the earlier region of each gene sequence. An ATAT box located early on in a gene may promote RNA polymerase (RNAP) binding in the direction opposite to regular transcription on the DNA and may help regulate gene expression. It has been shown that two RNAPs transcribing RNA in opposite directions on the same gene sequence may collide and bump each other off the DNA. This has the effect for inhibiting gene expression.

From the data though, no clear trend can be seen. Final plot is [final_plot.png](final_plot.png). Also the main code is [genes.py](genes.py).
