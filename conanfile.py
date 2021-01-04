from conans import ConanFile, CMake, tools


class natsasioConan(ConanFile):
    name = "nats_asio"
    version = "0.0.12"
    commit = version
    license = "MIT"
    author = "Vladislav Troinich antlad@icloud.com"
    url = "https://github.com/antlad/nats_asio"
    description = "Async client for NATS using boost asio"
    topics = ("opcua")
    settings = "cppstd", "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    build_policy = "missing"
    requires = (
        "boost/1.74.0",
        "fmt/6.2.0",
        "spdlog/1.5.0",
        "openssl/1.1.1d",
        "nlohmann_json/3.9.1"
    )

    def source(self):
        self.run(
            "git clone https://github.com/antlad/nats_asio.git && cd nats_asio && git checkout {}".format(self.version))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="nats_asio", args=[])
        cmake.build()

    def package(self):

        self.copy("*.hpp", dst="./include/",
                  src="./nats_asio/include/", keep_path=True)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["nats_asio"]
        self.cpp_info.includedirs = ['./include/']
