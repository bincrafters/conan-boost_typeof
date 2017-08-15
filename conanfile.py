from conans import ConanFile, tools, os

class BoostTypeofConan(ConanFile):
    name = "Boost.Typeof"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-typeof"
    source_url = "https://github.com/boostorg/typeof"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    requires =  "Boost.Level5Group/1.64.0@bincrafters/testing"
   
    def package_id(self):
        self.info.header_only()
        
    #This library is part of one or more cyclic dependency groups within Boost.
    
    #All members of cyclic dependency groups must be built under single package per group for Conan.
    
    #The combination is performed in the package(s) listed in the requires field.
    
    #This package enables simple consumption of this library while abstracting away the cyclic dependency issues. 