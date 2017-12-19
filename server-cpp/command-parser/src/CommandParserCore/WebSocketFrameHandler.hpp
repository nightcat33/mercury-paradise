//
//  WebSocketFrameHandler.hpp
//  poco_websocket_demo
//
//  Created by Xiangbin Hu on 5/7/17.
//
//

#ifndef WebSocketFrameHandler_hpp
#define WebSocketFrameHandler_hpp

#include <stdio.h>
#include <string>
#include <Poco/JSON/Object.h>
#include <Poco/RefCountedObject.h>
#include "Content.hpp"
#include <nlohmann/json.hpp>
/**
    This handler is expecting a json stirng with the following format
    {
        user_information : {

        }

        payload : {

        }
    }
 */
class WebSocketFrameHandler
{
public:
    /* Default constructor */
    WebSocketFrameHandler();
    
    /* Destructor */
    virtual ~WebSocketFrameHandler() noexcept;
    
    /* Parse the JSON string to a POCO JSON object */
    nlohmann::json parseJSONString(std::string json);

    /* the main function to be called for the handler */
    std::string handle(std::string json);

    /* set broker */
    bool setBroker(std::unique_ptr<CommandParserCore::Content::Broker>& broker);

   

private:
    std::unique_ptr<CommandParserCore::Content::Broker> broker = nullptr;
    
    
};

#endif /* WebSocketFrameHandler_hpp */
