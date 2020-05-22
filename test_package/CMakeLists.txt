cmake_minimum_required(VERSION 3.12)

project(nats_tool)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_definitions(-DSPDLOG_FMT_EXTERNAL)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Boost COMPONENTS coroutine REQUIRED)
find_package(OpenSSL REQUIRED)

list(REMOVE_ITEM CONAN_LIBS "boost_unit_test_framework")

add_executable(nats_tool nats_tool.cpp)
target_link_libraries(nats_tool ${CONAN_LIBS})

