"""Tests for check_linear_fit."""
import sys
from pathlib import Path

from polus.mm.utils.fitting.check_linear_fit.check_linear_fit import check_linear_fit

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_check_linear_fit() -> None:
    """Test check_linear_fit."""
    xs = [1.0, 2.0, 3.0]
    ys = [1.0, 2.0, 3.0]
    tol_quad = 0.1
    slope_min = 0.5
    slope_max = 1.5
    is_within_bounds = check_linear_fit(xs, ys, tol_quad, slope_min, slope_max)
    assert is_within_bounds


# now check for case that is out of bounds, make ys very large
def test_check_linear_fit_out_of_bounds() -> None:
    """Test check_linear_fit."""
    xs = [1.0, 2.0, 3.0]
    ys = [-5, 720, 100.0]
    tol_quad = 0.1
    slope_min = 0.5
    slope_max = 1.0
    is_within_bounds = check_linear_fit(xs, ys, tol_quad, slope_min, slope_max)
    assert not is_within_bounds


def test_check_linear_fit_cwl() -> None:
    """Test check_linear_fit CWL."""
    xs = [1.0, 2.0, 3.0]
    ys = [1.0, 2.0, 3.0]
    tol_quad = 0.1
    slope_min = 0.5
    slope_max = 1.5
    cwl_file = Path("check_linear_fit.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["xs"] = xs
    input_to_props["ys"] = ys
    input_to_props["tol_quad"] = tol_quad
    input_to_props["slope_min"] = slope_min
    input_to_props["slope_max"] = slope_max

    input_yaml_path = Path("check_linear_fit-sfct.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert "success" in stdout
