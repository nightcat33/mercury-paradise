//
// Created by ketian on 6/8/17.
//

#ifndef WEBSOCKET_COMMAND_PARSER_RESOURCECLIENT_H
#define WEBSOCKET_COMMAND_PARSER_RESOURCECLIENT_H

#include <Poco/JSON/Parser.h>
#include <Poco/Dynamic/Var.h>
#include "../Content.hpp"
#include <string>
#include <nlohmann/json.hpp>

#define SUCCESS         200
#define COMMENT_NOT_FOUND   -1
#define PAGE_NOT_FOUND      -2
#define ARTICLE_NOT_FOUND   -3

using json = nlohmann::json;

using namespace std;
namespace CommandParserCore {
    namespace Content {



        class ResourceClient {

        public:
            ResourceClient();

            virtual json getPage(PageID page_name);
            virtual int postPage(json page);
            virtual int deletePage(string page_name);
            virtual int createPage(json page);

            virtual json getComments(int comment_id);
            virtual int postComment(json comment);
            virtual int deleteComment(int comment_id);
            virtual int createComment(json comment);

            virtual json getArticle(int article_id);
            virtual int postArticle(json article);
            virtual int createArticle(json article);
            virtual int deleteArticle(int article_id);

        };

    }
}
#endif //WEBSOCKET_COMMAND_PARSER_RESOURCECLIENT_H
