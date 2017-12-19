//
// TestBroker.hpp
//

#ifndef TestBroker_hpp
#define TestBroker_hpp

#include "Content.hpp"


namespace CommandParserCore {
namespace Content {

class TestBroker;

class TestBroker : public Broker {

public:
    TestBroker();
    int getAvailableDirectoryCount();

protected:

    virtual nlohmann::json getAllAvailableDirectory();
    virtual nlohmann::json getContentFromPage(const std::string page);
    virtual nlohmann::json getContentFromCurrentPage();
private:
    int availableDirectoryCount = 0;

};


}} //CommandParserCore::Content

#endif // TestBroker_hpp


