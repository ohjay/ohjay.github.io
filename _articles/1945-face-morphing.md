---
layout: graphics
category: graphics
title: Face Morphing
permalink: /graphics/face-morphing/
tags:
  - 194
  - 5
---

# Face Morphing

<br />

> [Read the full writeup.](/graphics/1945)

<br />

Here, we build a system for morphing between faces (or in theory any images with similar structure). We do so by defining corresponding feature points for each of the two input images, computing a triangulation over those points, interpolating between the feature points to create an output "morphed" shape, and finally warping each image into that shape.

<br />

Using this program, we can easily create fun morphing sequences by varying our interpolation parameter over time. For example, when relatives claim our dog looks like Bill Cosby, we can [not use our program to] create a side-by-side comparison and [actually use our program to create] an apparently entertaining GIF.

<br />

<img src="/images/billcosby.jpg" data-action="zoom" />

<br />

<div style="position: relative; padding-bottom: 70.80%"><iframe src="https://gfycat.com/ifr/PoisedFlamboyantHellbender" frameborder="0" scrolling="no" width="100%" height="100%" style="position: absolute; top: 0; left: 0" allowfullscreen></iframe></div>
<!-- <img class="gfyitem" data-id="PoisedFlamboyantHellbender" /> -->

<br />

We're also able to "alter people's ethnicity" by morphing a subject into the average face of any given country. We do so below with my old roommate Oliver and your average Japanese actor (truly).

<br />

<table><tr>
    <td style="text-align: center" width="25%">
        <img src="/graphics/1945/images/oliver.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="25%">
        <img src="/graphics/1945/images/japaneseactor.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="25%">
        <img src="/images/olivertri.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="25%">
        <img src="/images/japaneseactortri.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

<div style="position: relative; padding-bottom: 70.80%"><iframe src="https://gfycat.com/ifr/PastelFriendlyIndianpalmsquirrel" frameborder="0" scrolling="no" width="100%" height="100%" style="position: absolute; top: 0; left: 0" allowfullscreen></iframe></div>
<!-- <table><tr>
    <td style="text-align: center" width="50%">
        <img src="/graphics/1945/images/japanese_oliver.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="50%">
        <img class="gfyitem" data-id="PastelFriendlyIndianpalmsquirrel" />
    </td>
</tr></table> -->

<!-- Extra scripts -->
<!-- <script type="text/javascript" src="https://assets.gfycat.com/gfycat.js"></script> -->
