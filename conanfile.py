#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostTypeofConan(base.BoostBaseConan):
    name = "boost_typeof"
    url = "https://github.com/bincrafters/conan-boost_typeof"
    lib_short_names = ["typeof"]
    header_only_libs = ["typeof"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_mpl",
        "boost_preprocessor",
        "boost_type_traits"
    ]


