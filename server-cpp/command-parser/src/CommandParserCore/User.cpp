
#include "User.hpp"

namespace CommandParserCore {
namespace User { 

Session::Session() : 
    isConnected(false),
    state(SessionState::ERROR)
    {};

void Session::login() {
    // TODO
}

void Session::logout() {
    // TODO
}
bool Session::isGood() {
    // TODO
    return this->isConnected && this->state == SessionState::NORMAL;
}



     


}} // namespace CommandParserCore::User
