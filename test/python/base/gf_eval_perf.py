# Copyright (c) 2017 Commissariat à l'énergie atomique et aux énergies alternatives (CEA)
# Copyright (c) 2017 Centre national de la recherche scientifique (CNRS)
# Copyright (c) 2020 Simons Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You may obtain a copy of the License at
#     https:#www.gnu.org/licenses/gpl-3.0.txt
#
# Authors: Olivier Parcollet, Nils Wentzell

from triqs.gf import *
from triqs.gf.gf_fnt import call_vec, call_s

beta = 10.0
n = 2

g= GfImFreq(beta=beta, indices=[0])

print(g.data.shape, g.indices.data)

def run() : 
    for i in range(10000):
      g(2)

def run_s() : 
    for i in range(10000):
      call_s(g)


def run_vec() : 
   return call_vec(g)




