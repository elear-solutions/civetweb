from conans import ConanFile, CMake, tools

class CivetweblibConan(ConanFile):
    name = "civetweb"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "This recipe file used to build and package binaries of civetweb repository"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        if (self.settings.os == "Android"):
            cmake.definitions[ "Platform" ] = "android"
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        #here src is directory path from where it should start checking for .h files and all mentioned in self.copy() 
        #it checks recursively by default
        self.copy("*.h", dst="include", src="include")
        self.copy("*.a", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        #self.cpp_info.libs name will be used to attach library in CMakelists.txt
        self.cpp_info.libs = [ "civetweb" ]
