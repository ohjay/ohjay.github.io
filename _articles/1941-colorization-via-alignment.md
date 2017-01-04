---
layout: graphics
category: graphics
title: Colorization via Alignment
permalink: /graphics/colorization-via-alignment/
tags:
  - 194
  - 1
---

# Colorization via Alignment

<br />

> [Read the full writeup.](/graphics/1941)

<br />

<u>The input</u>: no more and no less than the Prokudin-Gorskii collection, formatted as digitized stacks of glass plate negatives (where each of the aforementioned negatives represents a single RGB color channel).

<br />

<table><tr>
    <td style="text-align: center" width="25%">
        <img src="/images/emir_negatives.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="25%">
        <img src="/images/00201a_negatives.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="25%">
        <img src="/images/00872a_negatives.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="25%">
        <img src="/images/01880a_negatives.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

<u>The output</u>: colorized photographs. In this particular case, colorization comes down to aligning the three negatives and stacking them into a single (`height`) x (`width`) x (`3`) NumPy array. We align by experimentally translating two of the negatives and measuring the quality of alignment with the final negative, through normalized cross-correlation over either colors or edges. Eventually, of course, our aim is to take the RGB alignment with the best score.

<br />

To speed up the process, we run a coarse-to-fine search (read: image pyramid) over the displacements.

<br />

<table><tr>
    <td style="text-align: center" width="50%">
        <img src="/images/emir_edge.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="50%">
        <img src="/images/00201a.jpg" data-action="zoom" />
    </td>
</tr><tr>
    <td style="text-align: center" width="50%">
        <img src="/images/00872a.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="50%">
        <img src="/images/01880a.jpg" data-action="zoom" />
    </td>
</tr></table>
