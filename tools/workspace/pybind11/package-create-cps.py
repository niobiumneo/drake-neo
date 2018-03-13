#!/usr/bin/env python2

from drake.tools.install.cpsutils import read_defs

defs = read_defs("#define PYBIND11_(VERSION[^\s]+)\s+([^\s]+)")

content = """
{
  "Cps-Version": "0.8.0",
  "Name": "pybind11",
  "Description": "Seamless operability between C++11 and Python",
  "License": "BSD-3-Clause",
  "Version": "%(VERSION_MAJOR)s.%(VERSION_MINOR)s.%(VERSION_PATCH)s",
  "Default-Components": [":module"],
  "Components": {
    "module": {
      "Type": "interface",
      "Includes": ["@prefix@/include/pybind11"],
      "Compile-Features": ["c++11"]
    }
  },
  "X-CMake-Includes": ["${CMAKE_CURRENT_LIST_DIR}/pybind11Tools.cmake"],
  "X-CMake-Variables-Init": {
    "CMAKE_MODULE_PATH": "${CMAKE_CURRENT_LIST_DIR};${CMAKE_MODULE_PATH}"
  }
}
""" % defs

print(content[1:])
