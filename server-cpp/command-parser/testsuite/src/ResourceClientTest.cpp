//
// Created by ketian on 6/10/17.
//

#include "catch.hpp"
#include "CommandParserCore/ResourceClient/TestResourceClient.h"
#include <string>

using namespace std;

SCENARIO("TestResourceClient"){
    GIVEN("a simple desired output"){

        WHEN("TestResourceClient is directly called") {
            auto test = CommandParserCore::Content::TestResourceClient();
            auto status_code = test.testIntegration();

            THEN("The input command and the output result should match") {
                REQUIRE(status_code == SUCCESS);
            }
        }
    }
}

SCENARIO("Test if somethong not found"){
    GIVEN("a simple desired output"){

        WHEN("TestResourceClient is directly called") {
            auto test = CommandParserCore::Content::TestResourceClient();

            auto status_comment = test.getComments(200)["status_code"];
            auto status_page = test.getPage("200")["status_code"];
            auto status_article = test.getArticle(200)["status_code"];

            auto status_delete_comment = test.deleteComment(200);
            auto status_delete_page = test.deletePage("200");
            auto status_delete_article = test.deleteArticle(200);

            json payload;
            auto status_post_comment = test.postComment(payload);
            auto status_post_page = test.postPage(payload);
            auto status_post_article = test.postArticle(payload);

            THEN("The input command and the output result should match") {
                REQUIRE(status_comment == COMMENT_NOT_FOUND);
                REQUIRE(status_delete_comment == COMMENT_NOT_FOUND);
                REQUIRE(status_page == PAGE_NOT_FOUND);
                REQUIRE(status_delete_page == PAGE_NOT_FOUND);
                REQUIRE(status_article == ARTICLE_NOT_FOUND);
                REQUIRE(status_delete_article == ARTICLE_NOT_FOUND);

                REQUIRE(status_post_page == PAGE_NOT_FOUND);
                REQUIRE(status_post_article == ARTICLE_NOT_FOUND);
                REQUIRE(status_post_comment == COMMENT_NOT_FOUND);

            }
        }
    }
}



