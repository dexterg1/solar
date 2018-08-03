cmake_minimum_required(VERSION 3.8)
project(solar)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        spa.c
        spa.h
        spa_tester.c)

add_executable(solar ${SOURCE_FILES})