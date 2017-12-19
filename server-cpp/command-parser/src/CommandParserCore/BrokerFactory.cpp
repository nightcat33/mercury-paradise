//
// BrokerFactory.cpp
// This file contains implementation of broker factory which generates brokers
//
#include "Content.hpp"
#include "TestBroker.hpp"
namespace CommandParserCore {
namespace Content {

std::unique_ptr<Broker> BrokerFactory::newInstance(BrokerType type) {
    switch(type){
        case BrokerType::TEST:
            return std::make_unique<TestBroker>();
            // break;
        default:
            return nullptr;
            // break;
    }
    return nullptr;
}

} } // namespace CommandParserCore::Content
