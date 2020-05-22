from conans import ConanFile, CMake, tools
import os

class natsasioTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = (
        "cxxopts/v2.1.2@inexorgame/stable"
    )

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join("bin", "nats_tool --help")
            self.run(bin_path, run_environment=True)
