set(LIB_NAME "CommandParserCore")
set(${LIB_NAME}_SOURCE "")
aux_source_directory(. ${LIB_NAME}_SOURCE)
aux_source_directory(./ResourceClient ${LIB_NAME}_SOURCE)
aux_source_directory(./Cache ${LIB_NAME}_SOURCE)
add_library(CommandParserCore ${${LIB_NAME}_SOURCE})
