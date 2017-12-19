

#include "Record.hpp"

namespace CommandParserCore::Cache{

RecordIdentifier::RecordIdentifier(const std::string& page, const std::string& command) {
    this->page = page;
    this->command = command;
    this->ts = std::time(nullptr); 
}



std::string RecordIdentifier::getPage() const {
    return this->page;
}
std::string RecordIdentifier::getCommand() const {
    return this->command;
}
time_t RecordIdentifier::getTime() const {
    return this->ts;
}


RecordIdentifier Record::getID() const {
    return id;
}


Record::Record(const std::string & page, const std::string & command, const std::string & result){
    this->setID(RecordIdentifier(page, command));
    this->setResult(result);

}


void Record::setID(const RecordIdentifier& id) {
    this->id = id;

}

// set result of the record
void Record::setResult(const std::string & result) {
    this->result = result;
}
   
// get result of the record
    
const std::string Record::getResult() const {
    return this->result;
}




Record RecordFactory::newInstance(const std::string & page, const std::string & command, const std::string & result) {
    auto record = Record(page, command, result);
    return record;

}




} // CommandParserCore::Cache





