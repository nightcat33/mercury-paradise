

#ifndef Record_hpp
#define Record_hpp

#include <string>
#include <ctime>
namespace CommandParserCore::Cache {


class RecordIdentifier {

public:
    RecordIdentifier():page(""), command(""), ts(0) {};
    RecordIdentifier(const std::string& page, const std::string& command);
    std::string getPage() const; 
    std::string getCommand() const;
    time_t getTime() const;
private:
    std::string page;
    std::string command;
    time_t ts;
};




class Record {
public:
    
    Record(const std::string & page, const std::string & command, const std::string & result);

    void setID(const RecordIdentifier& id);

    // return id if the record
    RecordIdentifier getID() const;
   
    // set result of the record
    void setResult(const std::string & result);
   
    // get result of the record
    const std::string getResult() const;
private:
    RecordIdentifier id;
    std::string result;

};

class RecordFactory {

public:
    Record newInstance(const std::string & page, const std::string & command, const std::string & result);


};

} //CommandParserCore::Cache
#endif // Record_hpp



