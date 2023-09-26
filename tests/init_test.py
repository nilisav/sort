from click.testing import CliRunner
import sort_i.__init__

runner = CliRunner()
def test_first():
    result = runner.invoke(sort_i.__init__.testfunc, [])
    assert result.output == "[]\n"

def test_second():
    result = runner.invoke(sort_i.__init__.testfunc, ["1", "2", "3"])
    assert result.output == "[1, 2, 3]\n"

def test_third():
    result = runner.invoke(sort_i.__init__.testfunc, ["1", "5", "3", "8", "4"])
    assert result.output == "[1, 3, 4, 5, 8]\n"

def test_fourth():
    result = runner.invoke(sort_i.__init__.testfunc, ["2", "5", "9", "1", "2"])
    assert result.output == "[1, 2, 2, 5, 9]\n"