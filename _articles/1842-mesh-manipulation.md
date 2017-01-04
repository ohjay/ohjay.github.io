---
layout: graphics
category: graphics
title: Mesh Manipulation
permalink: /graphics/mesh-manipulation/
tags:
  - 184
  - 2
---

# Mesh Manipulation

<br />

> [Read the full writeup.](/graphics/1842)

<br />

The **mesh editor** produced as a result of this project allows users to load, view, and edit triangle meshes (formatted as basic COLLADA files). Specifically, users can upsample the mesh with Loop subdivision and flip/split edges.

<br />

Most of this work is done by performing operations on the halfedge data structure by which we represent our meshes. Since our meshes are in the end composed only of vertices and edges, mesh editing really boils down to the creation/deletion of vertices and edges, alongside the repositioning of vertices. 

<br />

<table><tr>
    <td style="text-align: center" width="50%">
        <img src="/images/pt5_torus1.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="50%">
        <img src="/images/pt5_bugs3.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

We also wrote a couple of GLSL fragment shaders; the image below contains an example of environment map reflection.

<br />

<img src="/images/pt6_shader2_so_beautiful.jpg" data-action="zoom" />

<br />

The editor can excitingly be used to render meshes exported from commercial 3D modeling software! The bird below is an Owen Jow original (created using Autodesk Maya).

<br />

<img src="/images/goldbird13.jpg" data-action="zoom" />
