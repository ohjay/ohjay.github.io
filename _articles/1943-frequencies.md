---
layout: graphics
category: graphics
title: Frequencies
permalink: /graphics/frequencies/
tags:
  - 194
  - 3
---

# Frequencies

<br />

> [Read the full writeup.](/graphics/1943)

<br />

There are a lot of things going on in this project.

<br />

The first of these is a sharpening implementation. As it happens, images are perceived as "sharp" due to a prevalence of high frequencies, or edges. Thus, to sharpen an image all we have to do is extract its high frequencies... and then just add them back in again.

<br />

<table><tr>
    <td style="text-align: center" width="50%">
        <img src="/images/dennis.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="50%">
        <img src="/images/dennis_sharp.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

Next, we take it upon ourselves to create a hybrid image. A hybrid image combines low frequencies with disparate high frequencies, such that from afar it is only possible to see the low-frequency content but from up close it is more natural to focus on the high frequencies. We generate a hybrid image as the sum of these two components.

<br />

<table><tr>
    <td style="text-align: center" width="33.33%">
        <img src="/images/derek.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="33.33%">
        <img src="/images/nutmeg.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="33.33%">
        <img src="/images/derekcat.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

After that, we assemble Gaussian and Laplacian stacks of our images, which highlight the various types of observable frequencies.

<br />

<table><tr>
    <td style="text-align: center" width="20%">
        <img src="/graphics/1943/images/lincoln_g1.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="20%">
        <img src="/graphics/1943/images/lincoln_g2.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="20%">
        <img src="/graphics/1943/images/lincoln_g3.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="20%">
        <img src="/graphics/1943/images/lincoln_g4.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="20%">
        <img src="/graphics/1943/images/lincoln_g5.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

Finally, we attempt to seamlessly merge pairs of images using a multiresolution blending technique. Essentially, we linearly combine the images at different layers of their Laplacian stacks (using a Gaussian masking stack as weights), and eventually sum up all of the results.

<br />

<table><tr>
    <td style="text-align: center" width="45%">
        <img src="/images/wall2d2_gray.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="55%">
        <img src="/images/spade.jpg" data-action="zoom" />
    </td>
</tr></table>
