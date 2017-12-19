
cmake_minimum_required(VERSION 3.8)
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/externals/sanitizers-cmake/cmake" ${CMAKE_MODULE_PATH})
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Wall")
find_package(Sanitizers)
find_program(VALGRIND "valgrind")
project("websocket-command-parser")
enable_testing()
set(P_NAME "WebSocketServer")

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(LOCAL_SRCS "")
set(CMAKE_CXX_STANDARD 17)
aux_source_directory(src LOCAL_SRCS)
include_directories(/usr/local/include ${CMAKE_CURRENT_SOURCE_DIR}/src)
link_directories(/usr/local/lib)

add_subdirectory(src/CommandParserCore)
add_executable( ${P_NAME} 
                src/WebSocketServer.cpp )



set(RESOURCE_DIR ${CMAKE_SOURCE_DIR}/resources )            
# if(WINCE)
# set_target_properties( ${SAMPLE_NAME} PROPERTIES LINK_FLAGS "/ENTRY:wmainCRTStartup")
# endif()
target_link_libraries( ${P_NAME} PocoNet PocoUtil PocoJSON PocoXML PocoFoundation restclient-cpp CommandParserCore cpp_redis tacopie)

add_custom_command(TARGET ${P_NAME} POST_BUILD
                   COMMAND ${CMAKE_COMMAND} -E copy_directory
                           ${RESOURCE_DIR}
                           $<TARGET_FILE_DIR:${P_NAME}>/resources
                   )

add_custom_command(TARGET ${P_NAME} PRE_BUILD
                    COMMAND ${CMAKE_COMMAND} -E copy
                            $<TARGET_FILE_DIR:${P_NAME}>/compile_commands.json
                            ${CMAKE_SOURCE_DIR}/compile_commands.json
                    )


set(UNIT_TEST "${P_NAME}_test")
set(TEST_SRCS 
        testsuite/src/tests-main.cpp
       testsuite/src/WebSocketFrameHandler-test.cpp
       testsuite/src/Broker-test.cpp
       testsuite/src/Record-test.cpp
        testsuite/src/ResourceClientTest.cpp
        testsuite/src/Cache-test.cpp
        testsuite/src/catch.hpp)

add_executable(${UNIT_TEST}
                ${TEST_SRCS})
add_sanitizers(${UNIT_TEST})
target_link_libraries(${UNIT_TEST} PocoNet PocoUtil PocoJSON PocoXML PocoFoundation PocoCppUnit restclient-cpp CommandParserCore cpp_redis tacopie)
add_test(NAME ${P_NAME} WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR} COMMAND ${UNIT_TEST})
add_custom_target(valgrind
        COMMAND "${VALGRIND}" --tool=memcheck --leak-check=yes --show-reachable=yes --num-callers=20 --track-fds=yes --log-file="valgrind-logs.txt" $<TARGET_FILE:${UNIT_TEST}>)


