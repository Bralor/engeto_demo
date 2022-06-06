from tasks.tasks import EngetoTaskEntity


class TestEngetoEntity:
    """Run the testing functions to check task object."""

    def setup(self):
        self.testing_inst = EngetoTaskEntity(
            name="převaděč jednotek",
            time=10,
            tests=True,
            lesson="Lekce01"
        )

    def test_correct_attribute_name(self):
        assert self.testing_inst.name == "převaděč jednotek"

    def test_incorrect_attribute_name(self):
        assert self.testing_inst.name != "převaděč času"

    def test_correct_repr_method(self):
        assert str(self.testing_inst) == "Lekce01: převaděč jednotek"

    def test_empty_parameter_solution(self):
        assert not self.testing_inst.solution

    def test_defined_parameter_solution(self):
        self.testing_inst.solution = "/foo/bar/task_solution.py"
        assert self.testing_inst.solution == "/foo/bar/task_solution.py"
