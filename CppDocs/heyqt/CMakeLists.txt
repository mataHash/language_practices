cmake_minimum_required(VERSION 3.16)
project(heyqt VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Esto es vital para que Qt genere el código de señales y slots automáticamente
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# Exporta los comandos para que tu LSP (clangd) funcione perfecto
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)

add_executable(heyqt main.cpp)

target_link_libraries(heyqt PRIVATE Qt6::Widgets)
