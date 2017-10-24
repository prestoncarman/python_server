# server.py

import os
import logging
import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.autoreload
from tornado.options import define, options


# import handlers as needed - here we import all of them
from aswwu.base_handlers import *
from aswwu.route_handlers import *

# import our super secret keys
from settings import keys

# define some initial options that can be passed in at run time
# e.g. `python server.py --port=8881` would run the server on port 8881
define("port", default=8888, help="run on the given port", type=int)
define("log_name", default="aswwu", help="name of the logfile")
define("current_year", default="1617")

# the main class that wraps everything up nice and neat
class Application(tornado.web.Application):
    def __init__(self):
        # define some global settings
        settings = {
            "login_url": "/login",
            "secret_key": keys["hmac"]
        }

        # list out the routes (as regex) and their corresponding handlers
        handlers = [
            # (r"/collegian_search/(.*)", CollegianArticleSearch),
            (r"/login", BaseLoginHandler),
            (r"/profile/(.*)/(.*)", ProfileHandler),
            (r"/profile_photo/(.*)/(.*)", ProfilePhotoHandler),
            (r"/role/administrator", AdministratorRoleHandler),
            # (r"/role/collegian", CollegianRoleHandler),
            (r"/role/volunteer", VolunteerRoleHandler),
            (r"/search/all", SearchAllHandler),
            (r"/search/(.*)/(.*)", SearchHandler),
            (r"/update/(.*)", ProfileUpdateHandler),
            (r"/volunteer", VolunteerHandler),
            (r"/volunteer/(.*)", VolunteerHandler),
            (r"/feed", FeedHandler),
            (r"/verify", BaseVerifyLoginHandler),
            (r"/", BaseIndexHandler),
            # (r"/senate_election/showall", AllElectionVoteHandler),
            (r"/senate_election/vote/(.*)", ElectionVoteHandler),
            # (r"/senate_election/livefeed", ElectionLiveFeedHandler),
            # (r"/pages", PagesHandler),
            (r"/saml/account/", SamlHandler),
            (r"/matcher", MatcherHandler),
            (r"/forms/job/new", NewFormHandler),
            (r"/forms/job/view/(.*)", ViewFormHandler),
            (r"/forms/job/delete", DeleteFormHandler),
            (r"/forms/application/submit", SubmitApplicationHandler),
            (r"/forms/application/view/(.*)/(.*)", ViewApplicationHandler),
            (r"/forms/application/status", ApplicationStatusHandler),
            (r"/forms/resume/upload", ResumeUploadHandler),
            (r"/forms/resume/download/(.*)/(.*)", ViewResumeHandler),
            (r"/askanything/add",AskAnythingAddHandler),
            (r"/askanything/view", AskAnythingViewAllHandler),
            (r"/askanything/view/rejected", AskAnythingRejectedHandler),
            (r"/askanything/(.*)/vote", AskAnythingVoteHandler),
            (r"/askanything/authorize", AskAnythingAuthorizeHandler),
            (r"/askanything/(.*)/authorize", AskAnythingAuthorizeHandler),
        ]

        # a bunch of setup stuff
        # mostly for logging and telling Tornado to start with the given settings
        self.options = options
        logger = logging.getLogger(options.log_name)
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("aswwu/"+options.log_name+".log")
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter("{'timestamp': %(asctime)s, 'loglevel' : %(levelname)s %(message)s }")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        tornado.web.Application.__init__(self, handlers, **settings)
        logger.info("Application started on port " + str(options.port))

# running `python server.py` actually tells python to rename this file as "__main__"
# hence this check to make sure we actually wanted to run the server
if __name__ == "__main__":
    # pass in the conf name with `python server.py CONF_NAME`
    # by default this is "default"
    config = tornado.options.parse_command_line()
    if len(config) == 0:
        conf_name = "default"
    else:
        conf_name = config[0]

    # initiate the IO loop for Tornado
    io_loop = tornado.ioloop.IOLoop.instance()
    tornado.options.parse_config_file("aswwu/"+conf_name+".conf")
    # create a new instance of our Application
    application = Application()
    application.listen(options.port)
    # tell it to autoreload if anything changes
    tornado.autoreload.start()
    io_loop.start()