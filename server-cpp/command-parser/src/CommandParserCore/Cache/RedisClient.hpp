/**
 *
 * RedisClientClient.hpp
 * header file for cache client
 *
 * 
 */

 /**
 
     TODO:
     - design parameter object
     - design redis key value pair
 
     Key should be in the format of:
     page_id:<PageID>:
  */
 
 

#ifndef RedisClient_hpp
#define RedisClient_hpp
#include <vector>
#include <unordered_map>
#include <cpp_redis/cpp_redis>
#include "Client.hpp"

namespace CommandParserCore::Cache
{

class RedisClientKeySerializer : public ClientKeySerializer
{
public:
    std::string serialize();
    void setPageID(const std::string id);
    void setCommand(const std::string cmd);
    


private:
    std::unordered_map<std::string, std::string> key_value;

    static const std::vector<std::string> key_list;

};



    
class RedisClient : public Client
{
public:
    RedisClient();
    virtual ~RedisClient();
    //true for success
    virtual bool set(const std::string & key, const std::string & value);
    virtual std::string get(const std::string & key);
    bool is_connected();
    



private:
    void init();
    cpp_redis::future_client client;
};

    
} // namespace CommandParserCore::Cache

#endif //RedisClient_hpp
