#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostTypeofConan(base.BoostBaseConan):
    name = "boost_typeof"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_typeof"
    lib_short_names = ["typeof"]
    header_only_libs = ["typeof"]
    b2_requires = [
        "boost_config",
        "boost_preprocessor",
        "boost_type_traits"
    ]
