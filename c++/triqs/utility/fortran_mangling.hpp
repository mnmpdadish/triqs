// Copyright (c) 2013 Commissariat à l'énergie atomique et aux énergies alternatives (CEA)
// Copyright (c) 2013 Centre national de la recherche scientifique (CNRS)
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You may obtain a copy of the License at
//     https://www.gnu.org/licenses/gpl-3.0.txt
//
// Authors: Olivier Parcollet

// Compiler independant call to Fortran names
#ifndef TRIQS_BIND_FORTRAN_LOWERCASE
#define TRIQS_FORTRAN_MANGLING(id) id##_
#else
#error "I do not know what to do with this fortran mangling !"
// ???
#endif
