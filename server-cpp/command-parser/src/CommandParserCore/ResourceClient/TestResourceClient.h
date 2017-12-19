//
// Created by ketian on 6/10/17.
//

#ifndef WEBSOCKET_COMMAND_PARSER_TESTRESOURCECLIENT_H
#define WEBSOCKET_COMMAND_PARSER_TESTRESOURCECLIENT_H

#include "ResourceClient.h"
#include <string>

namespace CommandParserCore {
    namespace Content {

        class TestResourceClient : public ResourceClient {

        public:

            TestResourceClient();

            int createPageSample(void);
            int createArticleSample(void);
            int createCommentSample(int article_id);
            int random(int start, int end);
            int testIntegration(void);


        private:
            ResourceClient *client;
            unordered_map<int, bool> commentIdMap;
            unordered_map<int, bool> articleIdMap;
            unordered_map<int, bool> pageNameMap;

        };
    }
}



#endif //WEBSOCKET_COMMAND_PARSER_TESTRESOURCECLIENT_H
