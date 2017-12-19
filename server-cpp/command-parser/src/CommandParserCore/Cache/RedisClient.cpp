
#include "RedisClient.hpp"

namespace CommandParserCore::Cache
{

#define USE_DEFAULT_REDIS_SETTINGS 1
/**================================================== *
 * ==========  Constant Definition   ========== *
 * ================================================== */

static const std::string REDIS_HOST("server-redis");
static const unsigned int REDIS_PORT = 6379;

/* =======  End of Constant Definition   ======= */


const std::vector<std::string>
RedisClientKeySerializer::key_list = {"page_id",
                                        "cmd"
                                     };

std::string RedisClientKeySerializer::serialize() {
    std::string key;
    for (const auto & i : RedisClientKeySerializer::key_list) {
        auto search = key_value.find(i);
        if(search == key_value.end()){
            return std::string();
        }
        key += i;
        key += ':';
        key += search->second;
        key += ':';
        
    }
    if (key.size() != 0) {
        key.pop_back(); // pop out ':'
    }
    return key;
}
void RedisClientKeySerializer::setCommand(const std::string cmd) {
    key_value["cmd"] = cmd;
}

void RedisClientKeySerializer::setPageID(const std::string id){
    key_value["page_id"] = id;
}


RedisClient::RedisClient()
{
    init();
    
}

RedisClient::~RedisClient()
{
    client.disconnect();
}
void RedisClient::init()
{
#ifdef USE_DEFAULT_REDIS_SETTINGS
    client.connect();
#else
    client.connect(REDIS_HOST, REDIS_PORT);
#endif
}

bool RedisClient::set(const std::string & key, const std::string & value) {
    if( !client.is_connected() ) {
        return false; 
    } 
    auto set_result = client.set(key, value);
    client.commit();
    return set_result.get().ok();
}
   
std::string RedisClient::get(const std::string & key){
    if( !client.is_connected() ) {
        return std::string(); 
    } 
    auto get_result = client.get(key);
    client.commit();
    auto result = get_result.get();
    if (result.ok()) {
        if (result.is_string()){
            return result.as_string();
        }
    }

    auto type = result.get_type();
    
    return std::string();
}

bool RedisClient::is_connected() {
    return client.is_connected();
}



} //CommandParserCore::Cache





