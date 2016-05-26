from conans import ConanFile
from conans.tools import download, unzip
import os

VERSION = "0.0.2"


class CMakeOptimizedArgParsing(ConanFile):
    name = "cmake-opt-arg-parsing"
    version = os.environ.get("CONAN_VERSION_OVERRIDE", VERSION)
    requires = ("cmake-include-guard/master@smspillaz/cmake-include-guard", )
    generators = "cmake"
    url = "http://github.com/polysquare/cmake-opt-arg-parsing"
    licence = "MIT"
    options = {
        "dev": [True, False]
    }
    default_options = "dev=False"

    def requirements(self):
        if self.options.dev:
            self.requires("cmake-module-common/master@smspillaz/cmake-module-common")

    def source(self):
        zip_name = "cmake-opt-arg-parsing.zip"
        download("https://github.com/polysquare/"
                 "cmake-opt-arg-parsing/archive/{version}.zip"
                 "".format(version="v" + VERSION),
                 zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy(pattern="*.cmake",
                  dst="cmake/cmake-opt-arg-parsing",
                  src="cmake-opt-arg-parsing-" + VERSION,
                  keep_path=True)
