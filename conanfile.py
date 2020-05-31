from conans import ConanFile, CMake, tools

class natsasioConan(ConanFile):
    name = "nats_asio"
    version = "0.0.9"
    commit = version
    license = "MIT"
    author = "Vladislav Troinich antlad@icloud.com"
    url = "https://github.com/antlad/nats_asio"
    description = "Async client for NATS using boost asio"
    topics = ("opcua")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    build_policy = "missing"
    requires = (
        "boost/1.71.0@conan/stable",
        "fmt/6.1.2",
        "spdlog/1.5.0",
        "OpenSSL/1.1.1c@conan/stable",
        "jsonformoderncpp/3.7.2@vthiery/stable"
    )

    def source(self):
        self.run("git clone https://github.com/antlad/nats_asio.git && cd nats_asio && git checkout {}".format(self.version))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="nats_asio", args=[])
        cmake.build()

    def package(self):
        
        self.copy("*.hpp", dst="./include/", src="./nats_asio/include/", keep_path=True)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["nats_asio"]
        self.cpp_info.includedirs = ['./include/']

