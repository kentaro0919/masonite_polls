"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get().route("/", "WelcomeController@show").name("welcome"),
    Get().route("/polls/", "PollsController@index").name("polls.index"),
]
