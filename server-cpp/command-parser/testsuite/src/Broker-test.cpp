
#include "catch.hpp"
#include "CommandParserCore/TestBroker.hpp"
#include "iostream"

SCENARIO("TestBroker", "[broker]"){
    GIVEN("a simple desired output"){
        nlohmann::json desired;
        std::string command = "hello world!";
        desired["content"] = command;
        WHEN("TestBroker is directly called") {
            CommandParserCore::Content::TestBroker test;

            auto a = nlohmann::json::parse(test.reply(command));
            THEN("reply is echoed") {
                REQUIRE(a.at("content").get<std::string>() == command);
            }
        }
        WHEN("TestBroker is manufactured by factory") {
            auto factory = CommandParserCore::Content::BrokerFactory();
            auto broker = factory.newInstance(CommandParserCore::Content::BrokerType::TEST);
            auto a = nlohmann::json::parse(broker->reply(command));
            THEN("reply is echoed") {
                REQUIRE(a.at("content").get<std::string>() == command);
            }
        }

    }
}

SCENARIO("Check TestBroker command handlers", "[broker]"){
    GIVEN("a TestBroker manufactured by a factory"){
        auto factory = CommandParserCore::Content::BrokerFactory();
        auto broker = factory.newInstance(CommandParserCore::Content::BrokerType::TEST);
        WHEN("ls is called"){
            auto a = nlohmann::json::parse(broker->reply("cd HOME"));
            auto reply = a.at("content").dump();

            INFO(reply);
           THEN("the result should not be empty"){
                REQUIRE(reply.size() > 0);
            }
        
        }
    } 
}


