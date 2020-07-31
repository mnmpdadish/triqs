# Copyright (c) 2014-2015 Commissariat à l'énergie atomique et aux énergies alternatives (CEA)
# Copyright (c) 2014-2015 Centre national de la recherche scientifique (CNRS)
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
# Authors: Michel Ferrero, Olivier Parcollet, Nils Wentzell

from triqs.gf import *

g = GfImFreq(indices = [list(range(3)), list(range(5))], beta = 40, n_points = 1000)
gt = g.transpose()

assert g.data.shape == (2000, 3, 5)
assert gt.data.shape == (2000, 5, 3)
