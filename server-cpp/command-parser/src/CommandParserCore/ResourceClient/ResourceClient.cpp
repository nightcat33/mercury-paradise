//
// Created by ketian on 6/8/17.
//
#include "ResourceClient.h"
#include <restclient-cpp/restclient.h>
#include <string>

using json = nlohmann::json;
using namespace std;



namespace CommandParserCore {
    namespace Content {

        ResourceClient::ResourceClient(){};

        json ResourceClient::getPage(PageID page_name) {
            json payload;
            RestClient::Response r;
            payload["page_name"] = page_name;
            r = RestClient::post("http://0.0.0.0:5000/pages/readone", \
                                                  "text/json", \
                                                  payload.dump());
            if(r.code != SUCCESS){
                payload["status_code"] = PAGE_NOT_FOUND;
                return payload;
            }

            payload = json::parse(r.body);
            payload["status_code"] = SUCCESS;
            return payload;
        }

        int ResourceClient::deletePage(string page_name){
            json payload;
            payload["page_name"] = page_name;
            RestClient::Response r;

            auto status = getPage(page_name)["status_code"];
            if(status != SUCCESS)
                return PAGE_NOT_FOUND;


            r = RestClient::post("http://0.0.0.0:5000/pages/deleteone", \
                                                  "text/json", \
                                                  payload.dump());
            return SUCCESS;
        }

        int ResourceClient::postPage(json page) {
            RestClient::Response r;
            r = RestClient::post("http://0.0.0.0:5000/pages/updateone", \
                                                  "text/json", \
                                                  page.dump());
            if(r.code != SUCCESS)
                return PAGE_NOT_FOUND;
            else
                return SUCCESS;
        }


        json ResourceClient::getComments(int comment_id) {
            json payload;
            payload["comment_id"] = comment_id;
            RestClient::Response r;
            r = RestClient::post("http://0.0.0.0:5000/comments/readone", \
                                                  "text/json", \
                                                  payload.dump());

            if(r.code != SUCCESS){
                payload["status_code"] = COMMENT_NOT_FOUND;
                return payload;
            }

            payload = json::parse(r.body);
            payload["status_code"] = SUCCESS;
            return payload;
        }


        int ResourceClient::postComment(json comment) {
            RestClient::Response r;
            r = RestClient::post("http://0.0.0.0:5000/comments/updateone", \
                                                  "text/json", \
                                                  comment.dump());
            if(r.code != SUCCESS)
                return COMMENT_NOT_FOUND;
            else
                return SUCCESS;
        }

        int ResourceClient::deleteComment(int comment_id) {
            json payload;
            payload["comment_id"] = comment_id;
            auto status = getComments(comment_id)["status_code"];
            if(status != SUCCESS)
                return COMMENT_NOT_FOUND;
            RestClient::Response r;
            r = RestClient::post("http://0.0.0.0:5000/comments/deleteone", \
                                                  "text/json", \
                                                  payload.dump());

            return SUCCESS;
        }

        json ResourceClient::getArticle(int article_id) {
            json payload;
            payload["article_id"] = article_id;
            RestClient::Response r;
            r = RestClient::post("http://0.0.0.0:5000/article/readone", \
                                                  "text/json", \
                                                  payload.dump());
            if(r.code != SUCCESS){
                payload["status_code"] = ARTICLE_NOT_FOUND;
                return payload;
            }
            payload = json::parse(r.body);
            payload["status_code"] = SUCCESS;
            return payload;
        }

        int ResourceClient::createPage(json page) {
            RestClient::Response r;
            r = RestClient::post("http://0.0.0.0:5000/pages/createone", \
                                                  "text/json", \
                                                  page.dump());
            return r.code;
        }

        int ResourceClient::createComment(json comment) {
            RestClient::Response r;
            r = RestClient::post("http://0.0.0.0:5000/comments/createone", \
                                                  "text/json", \
                                                  comment.dump());
            return r.code;
        }

        int ResourceClient::createArticle(json article) {
            RestClient::Response r;
            r = RestClient::post("http://0.0.0.0:5000/article/createone", \
                                                  "text/json", \
                                                  article.dump());
            return r.code;
        }

        int ResourceClient::postArticle(json article) {
            RestClient::Response r;
            r = RestClient::post("http://0.0.0.0:5000/article/updateone", \
                                                  "text/json", \
                                                  article.dump());
            if(r.code != SUCCESS)
                return ARTICLE_NOT_FOUND;
            else
                return SUCCESS;
        }

        int ResourceClient::deleteArticle(int article_id) {
            json payload;
            payload["article_id"] = article_id;
            RestClient::Response r;
            auto status = getArticle(article_id)["status_code"];
            if(status != SUCCESS)
                return ARTICLE_NOT_FOUND;
            r = RestClient::post("http://0.0.0.0:5000/article/deleteone", \
                                                  "text/json", \
                                                  payload.dump());

            return SUCCESS;
        }

    }
}



