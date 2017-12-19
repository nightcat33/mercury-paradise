from flask import Flask
from flask_restful import Api, Resource
import resources.user as user
import resources.irc as irc
import resources.article as article
import resources.comments as comments
import resources.user_profile as user_profile
import resources.update_history as update_history
import resources.pages as pages

app = Flask(__name__)
api = Api(app)

api.add_resource(user.UserCreateOne, '/user/createone')
api.add_resource(user.UserCreateMultiple,'/user/createmultiple')
api.add_resource(user.UserUpdateOne, '/user/updateone')
api.add_resource(user.UserUpdateMultiple, '/user/updatemultiple')
api.add_resource(user.UserReadOne, '/user/readone')
api.add_resource(user.UserReadMultiple, '/user/readmultiple')
api.add_resource(user.UserDeleteOne, '/user/deleteone')
api.add_resource(user.UserDeleteMultiple, '/user/deletemultiple')

api.add_resource(irc.IrcCreateOne, '/irc/createone')
api.add_resource(irc.IrcCreateMultiple, '/irc/createmultiple')
api.add_resource(irc.IrcUpdateOne, '/irc/updateone')
api.add_resource(irc.IrcUpdateMultiple, '/irc/updatemultiple')
api.add_resource(irc.IrcReadOne, '/irc/readone')
api.add_resource(irc.IrcReadMultiple, '/irc/readmultiple')
api.add_resource(irc.IrcDeleteOne, '/irc/deleteone')
api.add_resource(irc.IrcDeleteMultiple, '/irc/deletemultiple')

api.add_resource(article.ArticleCreateOne, '/article/createone')
api.add_resource(article.ArticleCreateMultiple, '/article/createmultiple')
api.add_resource(article.ArticleUpdateOne, '/article/updateone')
api.add_resource(article.ArticleUpdateMultiple, '/article/updatemultiple')
api.add_resource(article.ArticleReadOne, '/article/readone')
api.add_resource(article.ArticleReadMultiple, '/article/readmultiple')
api.add_resource(article.ArticleDeleteOne, '/article/deleteone')
api.add_resource(article.ArticleDeleteMultiple, '/article/deletemultiple')

api.add_resource(comments.CommentsCreateOne, '/comments/createone')
api.add_resource(comments.CommentsCreateMultiple, '/comments/createmultiple')
api.add_resource(comments.CommentsUpdateOne, '/comments/updateone')
api.add_resource(comments.CommentsUpdateMultiple, '/comments/updatemultiple')
api.add_resource(comments.CommentsReadOne, '/comments/readone')
api.add_resource(comments.CommentsReadMultiple, '/comments/readmultiple')
api.add_resource(comments.CommentsDeleteOne, '/comments/deleteone')
api.add_resource(comments.CommentsDeleteMultiple, '/comments/deletemultiple')

api.add_resource(user_profile.UserProfileCreateOne, '/user_profile/createone')
api.add_resource(user_profile.UserProfileCreateMultiple, '/user_profile/createmultiple')
api.add_resource(user_profile.UserProfileUpdateOne, '/user_profile/updateone')
api.add_resource(user_profile.UserProfileUpdateMultiple, '/user_profile/updatemultiple')
api.add_resource(user_profile.UserProfileReadOne, '/user_profile/readone')
api.add_resource(user_profile.UserProfileReadMultiple, '/user_profile/readmultiple')
api.add_resource(user_profile.UserProfileDeleteOne, '/user_profile/deleteone')
api.add_resource(user_profile.UserProfileDeleteMultiple, '/user_profile/deletemultiple')

api.add_resource(update_history.UpdateHistoryCreateOne, '/update_history/createone')
api.add_resource(update_history.UpdateHistoryCreateMultiple, '/update_history/createmultiple')
api.add_resource(update_history.UpdateHistoryUpdateOne, '/update_history/updateone')
api.add_resource(update_history.UpdateHistoryUpdateMultiple, '/update_history/updatemultiple')
api.add_resource(update_history.UpdateHistoryReadOne, '/update_history/readone')
api.add_resource(update_history.UpdateHistoryReadMultiple, '/update_history/readmultiple')
api.add_resource(update_history.UpdateHistoryDeleteOne, '/update_history/deleteone')
api.add_resource(update_history.UpdateHistoryDeleteMultiple, '/update_history/deletemultiple')

api.add_resource(pages.PageCreateOne, '/pages/createone')
api.add_resource(pages.PageCreateMultiple, '/pages/createmultiple')
api.add_resource(pages.PageUpdateOne, '/pages/updateone')
api.add_resource(pages.PageUpdateMultiple, '/pages/updatemultiple')
api.add_resource(pages.PageReadOne, '/pages/readone')
api.add_resource(pages.PageReadMultiple, '/pages/readmultiple')
api.add_resource(pages.PageDeleteOne, '/pages/deleteone')
api.add_resource(pages.PageDeleteMultiple, '/pages/deletemultiple')

if __name__ == '__main__':
	app.run(host='0.0.0.0')




