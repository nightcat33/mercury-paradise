//
// TestBroker.cpp
//
// This file implements broker for testing
//


#include "TestBroker.hpp"
#include "ResourceClient/ResourceClient.h"
namespace CommandParserCore {
namespace Content {

TestBroker::TestBroker() {
    this->init();
}

/**
 * The test implementation of get all available directory inserts 20 json object with
 * the format of 
 * {
 *  "item" : int
 * }
 * into the array
 */
nlohmann::json TestBroker::getAllAvailableDirectory() {
    //auto ret = nlohmann::json(new Poco::JSON::Array()); 
    //for (int i = 0; i < 20; i++){
    //    auto temp = nlohmann::json(new Poco::JSON::Object());
    //    temp->set("item", Poco::Dynamic::Var(i));
    //    auto temp_var = Poco::Dynamic::Var(temp);
    //    ret->add(temp_var);
    //}
    // availableDirectoryCount = 20;
    Cache::RedisClientKeySerializer serializer;
    serializer.setPageID(tracker.getCurrentPosition());
    serializer.setCommand("get_all_available_directory");
    auto key = serializer.serialize();
    if(cache_client->is_connected()){
        auto cache_search_result = cache_client->get(key);
        if(cache_search_result.size() > 0) {
            return nlohmann::json::parse(cache_search_result);
        }
    }
    nlohmann::json ret;  
    auto client = ResourceClient();
    auto result = client.getPage(tracker.getCurrentPosition());
    if(result.at("status_code").get<int>() != SUCCESS) {
        return ret; 
    }
   
    ret["page_content"] = result;
    cache_client->set(key, ret.dump());
    return ret;
}
/**
 * This function takes a command string and replies
 * with json object pointer.
 */
//nlohmann::json TestBroker::reply(std::string command){
//
//    auto it = this->command_handler_map.find(command);
//    auto ret = nlohmann::json(new Poco::JSON::Object());
//    if (it == this->command_handler_map.end()){
//         ret->set("content", Poco::Dynamic::Var(command));
//         return ret;
//    }
//    auto temp = (this->*(it->second))(); 
//    
//    ret->set("content", Poco::Dynamic::Var(temp));
//    return ret;
//}

/**
 * The handler for LS
 */
//nlohmann::json TestBroker::LSHandler(){
//    auto ret = nlohmann::json(new Poco::JSON::Object());
//    ret->set("title", Poco::Dynamic::Var("Hello world!"));
//    ret->set("body", Poco::Dynamic::Var("world Hello!"));
//    ret->set("article_id", Poco::Dynamic::Var(32));
//    ret->set("creator_id", Poco::Dynamic::Var(23));
//    ret->set("comments", Poco::Dynamic::Var(nlohmann::json(new Poco::JSON::Array())));
//    ret->set("irc_id", Poco::Dynamic::Var(33));
//    
//    return ret; 
//}


nlohmann::json TestBroker::getContentFromPage(const PageID page){
    Cache::RedisClientKeySerializer serializer;
    serializer.setPageID(tracker.getCurrentPosition());
    serializer.setCommand("get_content_from_page");
    auto key = serializer.serialize();
    if(cache_client->is_connected()){
        auto cache_search_result = cache_client->get(key);
        if(cache_search_result.size() > 0) {
            return nlohmann::json::parse(cache_search_result);
        }
    }
    nlohmann::json ret;  
    auto client = ResourceClient();
    auto result = client.getPage(tracker.getCurrentPosition());
    if(result.at("status_code").get<int>() != SUCCESS) {
        return ret; 
    }
   
    ret["page_content"] = result;
    cache_client->set(key, ret.dump());
    return ret;
}

nlohmann::json TestBroker::getContentFromCurrentPage() {
   return this->getContentFromPage(tracker.getCurrentPosition()); 
}






}} //CommandParserCore::Content

