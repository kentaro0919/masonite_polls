from masonite.testing import UnitTest
from routes.web import ROUTES
from app.http.controllers.PollsController import PollsController


class TestPallsUnit(UnitTest):

    def setup_method(self):
        super().setup_method()

        self.routes(ROUTES)

    def test_route_exists(self):
        assert self.route("/polls/")

    def test_view_is_ok(self):
        assert self.route("/polls/").ok()

    def test_view_is_status_200(self):
        assert self.route("/polls/").status("200 OK")

    def test_view_contains(self):
        assert self.route("/polls/").contains(
            "Hello, world. You're at the polls index."
        )

    def test_unit_test_has_controller(self):
        assert self.route("/polls/").has_controller(PollsController)
