


#include "catch.hpp"
#include "CommandParserCore/Cache/Record.hpp"

SCENARIO("Record Factory functionality"){
    
    CommandParserCore::Cache::RecordFactory factory;
    WHEN("a record is spawned"){
        std::string page("foo");
        std::string command("boo");
        std::string result("{\"content\":\"Hello World\"}");
        auto record = factory.newInstance(page, command, result);
        THEN("The information of the id should match"){
            auto id = record.getID();
            REQUIRE(id.getPage() == page);
            REQUIRE(id.getCommand() == command);
        }
    
    }
}



