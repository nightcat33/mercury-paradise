

#include "catch.hpp"
#include "CommandParserCore/Cache/RedisClient.hpp"

SCENARIO("Redis Connectivity", "[cache]"){
    WHEN("a instance is instantiated"){
        CommandParserCore::Cache::RedisClient client;
        THEN("service should be available") {
            auto set_result = client.set("Hello", "world!");
            auto get_result = client.get("Hello");
            INFO(set_result);
            INFO(get_result);
            REQUIRE(set_result);
            REQUIRE(get_result == "world!");
            
        }
    }
    WHEN("a serializer is used"){
        CommandParserCore::Cache::RedisClient client;
        THEN("service should be available") {
            auto serializer = CommandParserCore::Cache::RedisClientKeySerializer();
            serializer.setPageID("1234321");
            serializer.setCommand("ls");
            auto key = serializer.serialize();
            auto set_result = client.set(key, "world!");
            key = serializer.serialize();
            auto get_result = client.get(key);
            INFO(key);
            INFO(set_result);
            INFO(get_result);
            REQUIRE(set_result);
            REQUIRE(get_result == "world!");
            
        }

    }

}
