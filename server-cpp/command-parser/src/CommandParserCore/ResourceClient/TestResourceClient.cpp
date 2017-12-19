//
// Created by ketian on 6/10/17.
//

#include "TestResourceClient.h"
#include "ResourceClient.h"
#include <restclient-cpp/restclient.h>
#include <nlohmann/json.hpp>
#include <stdlib.h>
#include <string>

using json = nlohmann::json;
using namespace std;
#define FAIL    -1

namespace CommandParserCore {
    namespace Content {


        TestResourceClient::TestResourceClient():ResourceClient(){
            client = new ResourceClient();
        }

        int TestResourceClient::random(int start, int end)
        {
            srand(unsigned(time(0)));
            return (rand()%(end-start+1))+start;
        }

        int TestResourceClient::createPageSample(void) {
            int id;
            json page;
            while(pageNameMap[id = random(0, 100)]);
            int article1 = createArticleSample();
            int article2 = createArticleSample();
            int article3 = createArticleSample();
            int article4 = createArticleSample();
            if(article1 != FAIL && article2 != FAIL && article3 != FAIL && article4 != FAIL){
                page["page_name"] = to_string(id);
                page["articles"] = {article1, article2, article3, article4};
                int status_code = client->createPage(page);
                if(status_code != SUCCESS){
                    return FAIL;
                }else {
                    pageNameMap[id] = true;
                    return id;
                }
            }else{
                return FAIL;
            }
        }

        int TestResourceClient::createArticleSample(void) {
            int id;
            json article;
            while(articleIdMap[id = random(0, 100)]);
            article["title"] = to_string(id);
            article["body"] = to_string(id);
            article["article_id"] = id;
            article["creator_id"] = id;
            article["irc_id"] = id;
            int status_code = client->createArticle(article);
            if(status_code != SUCCESS){
                return FAIL;
            }else {
                articleIdMap[id] = true;
                return id;
            }
        }

        int TestResourceClient::createCommentSample(int article_id) {
            int id;
            json comment;
            while(commentIdMap[id = random(0, 100)]);
            comment["article_id"] = article_id;
            comment["comment_id"] = id;
            comment["body"] = to_string(id);
            comment["user_id"] = id;

            int status_code = client->createComment(comment);
            if(status_code != SUCCESS){
                return FAIL;
            }else{
                commentIdMap[id] = true;
                return id;
            }
        }

        int TestResourceClient::testIntegration(void) {

            int page_id = createPageSample();
            if(page_id < 0){
                return FAIL;
            }
            json page = client->getPage(to_string(page_id));
            json payload;
            payload["filter"]["page_name"] = to_string(page_id);
            payload["update"]["$set"]["page_name"] = "hello";

            int status_code = client->postPage(payload);
            if(status_code < 0){
                return FAIL;
            }

            status_code = client->deletePage("hello");
            if(status_code < 0){
                return FAIL;
            }

            int article_id = createArticleSample();
            if(article_id < 0){
                return FAIL;
            }

            json article = client->getArticle(article_id);
            json comment_id = createCommentSample(article_id);
            json comment = client->getComments(comment_id);

            payload.clear();
            payload["filter"]["comment_id"] = comment_id;
            payload["update"]["$set"]["body"] = "stupid xiangbin";
            status_code = client->postComment(payload);
            if(status_code < 0){
                return FAIL;
            }

            status_code = client->deleteComment(comment_id);
            if(status_code < 0){
                return FAIL;
            }

            payload.clear();
            payload["filter"]["article_id"] = article_id;
            payload["update"]["$set"]["body"] = "fresh air";
            status_code = client->postArticle(payload);
            if(status_code < 0){
                return FAIL;
            }

            status_code = client->deleteArticle(article_id);
            if(status_code < 0){
                return FAIL;
            }

            return SUCCESS;

        }


    }
}




