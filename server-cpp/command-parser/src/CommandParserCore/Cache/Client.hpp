

/**
 *
 * Client.hpp
 * header file for cache client
 *
 * 
 */

 /**
 
     TODO:
     - design parameter object
     - design redis key value pair
 
     Key should be in the format of:
     page:<PageID>:
  */
 
 
#ifndef Client_hpp
#define Client_hpp

#include <cpp_redis/cpp_redis>


namespace CommandParserCore::Cache
{

class ClientKeySerializer
{
public:
    ClientKeySerializer() = default;
    virtual ~ClientKeySerializer() = default;
    virtual std::string serialize() = 0;
private:
  
};



    
class Client
{
public:
    Client() = default;
    virtual ~Client() = default;

    //true for success
    virtual bool set(const std::string & key, const std::string & value) = 0;
    virtual std::string get(const std::string & key) = 0;
};

    
} // namespace CommandParserCore::Cache

#endif //Client_hpp
