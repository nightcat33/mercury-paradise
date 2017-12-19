//
// Broker.cpp
//
// This file implements broker
//


#include "Content.hpp"
#include <nlohmann/json.hpp>

namespace CommandParserCore {
namespace Content {


BrokerStateTracker::BrokerStateTracker() {
    setCurrentPosition(Page::HOME); 
}

BrokerStateTracker::BrokerStateTracker(PageID page) {
    setCurrentPosition(page);
}

PageID BrokerStateTracker::getCurrentPosition() const {
    return this->currentPage;
}

void BrokerStateTracker::setCurrentPosition(PageID page) {
    this->currentPage = page;
}    



void Broker::init() {
    cache_client = std::make_unique<Cache::RedisClient>();
}


void Broker::parseCommand(std::string command) {
    commandAction = std::string();
    commandArgs = std::vector<std::string>();

    command.append(" ");
    std::string delimiter = " ";
    std::string token;
    size_t pos = 0;
    if(command.find(delimiter) == std::string::npos) {
        commandAction = command;
        return;
    }
    while((pos = command.find(delimiter)) != std::string::npos) {
        token = command.substr(0, pos);
        if(commandAction.size() == 0)
            commandAction = token;
        else
            commandArgs.push_back(token);
        command.erase(0, pos + delimiter.length());
    }
}

/**
 * This function takes a command string and replies
 * with json object pointer.
 */
std::string Broker::reply(std::string command){

    parseCommand(command);
    auto it = this->command_handler_map.find(commandAction);
    nlohmann::json ret;
    if (it == this->command_handler_map.end()){
        ret["content"] = command;
        return ret.dump();

    
    }
    auto temp = (this->*(it->second))();
    ret["command"] = commandAction;
    ret["content"] = temp;
    return ret.dump();
}

/**
 * Handler for "ls"
 * It should get all current available directory and put them in a json array
 */
nlohmann::json Broker::LSHandler(){
    nlohmann::json ret;
    auto allAvailableDirectory = this->getAllAvailableDirectory();    
    ret["all_available_directory"] = allAvailableDirectory;
    return ret; 
}

/**
 * Goto a directory
 */
nlohmann::json Broker::CDHandler(){
    

    // get content
     
    if(commandArgs.size() != 1){
        nlohmann::json ret;
        return ret;
    }
    auto arg = commandArgs.back();
    auto ret = getContentFromPage(arg);
    // change user position
    // TODO
    tracker.setCurrentPosition(arg);
    return ret;
}    
/**
 * Goto Home
 */
nlohmann::json Broker::HOMEHandler(){
    // TODO
    auto ret = getContentFromPage(Page::HOME);
    return ret;
}    
/**
 * Post an article
 */
nlohmann::json Broker::POSTHandler(){
    // TODO
    nlohmann::json ret;
    return ret;
}    
/**
 * Comment an article
 */
nlohmann::json Broker::COMMENTHandler(){
    // TODO
    nlohmann::json ret;
    return ret;
}    
/**
 * Get next page of a directory
 */
nlohmann::json Broker::NEXTHandler(){
    // TODO
    nlohmann::json ret;
    return ret;
}    
/**
 * Get previous page of a directory
 */
nlohmann::json Broker::PREVHandler(){
    // TODO
    nlohmann::json ret;
    return ret;
}    

/**
 * 指定一个有效目标
 */
nlohmann::json Broker::TYPEHandler(){
    // TODO
    nlohmann::json ret;
    return ret;
}    

/**
 * Open commandline mode
 */
nlohmann::json Broker::OPENHandler(){
    // TODO
    nlohmann::json ret;
    return ret;
}    

/**
 * Close commandline mode
 */
nlohmann::json Broker::CLOSEHandler(){
    // TODO
    nlohmann::json ret;
    return ret;
}    




}} //CommandParserCore::Content

