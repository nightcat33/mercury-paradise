//
// Created by Xiangbin Hu on 5/9/17.
//

#include "catch.hpp"
#include "CommandParserCore/WebSocketFrameHandler.hpp"
#include "CommandParserCore/Content.hpp"
// SCENARIO("parser can parse json string successfully") {
//     GIVEN("A json string and a WebSocketFrameHandler") {
//         std::string json = "{"
//                 "\"name\" : \"test\","
//                 "\"weight\" : 32"
//                 "}";
// 
//         auto handler = std::make_unique<WebSocketFrameHandler>();
// 
// 
//         WHEN("the json string parsed by the parser") {
//             auto result = handler->parseJSONString(json);
//             auto test_name = result->get("name");
//             auto value_name = test_name.convert<std::string>();
//             auto test_weight = result->get("weight");
//             auto value_weight = test_weight.convert<int>();
// 
//             THEN("the values are retrieved") {
//                 REQUIRE(value_name == std::string("test"));
//                 REQUIRE(value_weight == 32);
// 
//             }
//         }
//     }
// }
// 
// 
// SCENARIO("the main function handles correctly") {
// 
//     auto handler = std::make_unique<WebSocketFrameHandler>();
//     GIVEN("a simple desired output"){
//         std::string json = "{\"command\" : \"hello world!\"}";
//         auto desired = Poco::JSON::Object::Ptr(new Poco::JSON::Object());
//         std::string command = "hello world!";
//         desired->set("command", Poco::Dynamic::Var(command));
//         WHEN("handler has TestBroker") {
//             auto factory = CommandParserCore::Content::BrokerFactory();
//             auto broker = factory.newInstance(CommandParserCore::Content::BrokerType::TEST);
//             handler->setBroker(broker);
//             THEN("The input command and the output result should match") {
//                 auto result = handler->handle(json);
//                 REQUIRE(command == result);
//             }
//         }
//     }


//    GIVEN("handler with TestBroker"){
//        auto factory = Command::Content::BrokerFactory();
//        auto broker = factory.newInstance(Command::Content::BrokerType::TEST);
//        handler->setBroker(broker);
//        WHEN("the command is ls") {
//            std::string json = "{\"command\" : \"ls\"}";
//            auto result = handler->handle(json); 
//            auto result_ptr = handler->parseJSONString(result);
//            THEN("the article id matches") {
//                auto article_id = result_ptr->get("article_id");
//                REQUIRE(article_id.extract<int>() == 32);
//            }
//            
//        }
//    }
// }

