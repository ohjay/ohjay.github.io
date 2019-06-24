---
layout: graphics
category: graphics
title: Path Tracing
permalink: /graphics/path-tracing/
tags:
  - 184
  - 3
---

# Path Tracing

<br />

> [Read the full writeup.](/graphics/1843)

<br />

In this project, we implemented a physically-based renderer – a program that produces photorealistic images from scene descriptions by modeling the transport of light. Put shallowly, the renderer traces rays from the eye into the environment and represents the objects they hit as output pixels.

<br />

<table><tr>
    <td style="text-align: center" width="50%">
        <img src="/images/pt2_lucy.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="50%">
        <img src="/images/pt2_blob.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

That being the case, in a naïve implementation we're forced to run an intersection test between every environment-bound ray and every geometric primitive in the environment. In order to speed this up, we partition the primitives into different spatial regions ("bounding volumes" / BVs), each of which contains a lot of other BVs, and collision-test every ray against a single BV at a time. If a ray doesn't collide with a BV, it doesn't collide with any of the primitives (or other BVs) <em>inside</em> that BV. Thus, at each step we're able to eliminate a huge amount of the search space.

<br />

<img src="/images/bvh.jpg" data-action="zoom" />

<br />

Once we make an initial intersection, we need to calculate the lighting at that point. We do so by sending a ray straight toward each light (direct illumination) and also by bouncing randomly sampled, randomly terminated BSDF rays around the scene (indirect illumination). In each case, we apply the accumulated illumination at the intersected point to the current screen-space pixel.

<br />

This is called path tracing, incidentally, because by bouncing rays around the scene we simulate tracing the full path of light from its sources to the eye. (For the unfamiliar, we technically do trace rays from the eye <em>to</em> the light sources. It's computationally infeasible to travel in the correct direction; an overwhelming majority of rays wouldn't hit the eye at all.)

<br />

Upon completion of the path tracing algorithm, we are able to produce images as such.

<br />

<table><tr>
    <td style="text-align: center" width="33.33%">
        <img src="/images/dragon.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="33.33%">
        <img src="/images/pt4_banana.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="33.33%">
        <img src="/images/pt4_r1024.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

As icing on the cake, we also reflect and refract in order to properly implement the BSDFs of various materials.

<br />

<img src="/images/pt5_s1024.jpg" data-action="zoom" />
