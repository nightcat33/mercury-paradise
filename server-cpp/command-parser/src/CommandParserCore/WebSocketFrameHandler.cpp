//
//  WebSocketFrameHandler.cpp
//  poco_websocket_demo
//
//  Created by Xiangbin Hu on 5/7/17.
//
//

#include "WebSocketFrameHandler.hpp"

#include <Poco/JSON/Parser.h>

#include <Poco/Dynamic/Var.h>
#include <nlohmann/json.hpp>
// using namespace JSON;
// using namespace Dynamic;
/**
 * Default constructor
 * Initilizes the reference count per AutoPtr requirement
 */
WebSocketFrameHandler::WebSocketFrameHandler(){

}


/**
 * Destructor
 */
WebSocketFrameHandler::~WebSocketFrameHandler() noexcept {

}

/**************/

nlohmann::json WebSocketFrameHandler::parseJSONString(std::string json) {
    auto result = nlohmann::json::parse(json);
    return result;
}


/**
 * The main function to be called for the handler
 * default to return an empty string
 */
std::string WebSocketFrameHandler::handle(std::string json) {
    if(!this->broker){
        return nullptr;
    }
    auto jsonPtr = parseJSONString(json);
    auto var = jsonPtr.at("command").get<std::string>();
    auto reply = this->broker->reply(var);
    return reply;
    
    
    // return std::string();
}

/**
 * This function takes a shared ptr of Broker and set that to the handler
 * Please use BrokerFactory to generate a broker.
 */
bool WebSocketFrameHandler::setBroker(std::unique_ptr<CommandParserCore::Content::Broker>& broker){
    if(!broker)
        return false;
    this->broker = std::move(broker);
    return true;
}
