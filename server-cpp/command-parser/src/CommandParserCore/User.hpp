
//
// User.hpp
// Header file for user
//
// 
//

#ifndef User_hpp
#define User_hpp

#include <Poco/JSON/Parser.h>
#include <Poco/Dynamic/Var.h>

namespace CommandParserCore {
namespace User { 

enum class SessionState {
    NORMAL,
    ERROR
};

/**
 * The class for tracking the user session
 * This class is in charge of the life cycle of user websocket on the cpp side
 */
class Session {

public:
    Session();
    /* the function to login */    
    void login();
    /* the function to logout */
    void logout();
    /* the function to check whether the session is good */
    bool isGood();



private:
    bool isConnected;
    //char sessionID[128];
    SessionState state;
     
};




}} // namespace CommandParserCore::User

#endif /* User_hpp */
