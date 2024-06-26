"""Tests for fix_side_chain."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_fix_side_chain() -> None:
    """Test fix_side_chain."""
    cwl_file = Path("fix_side_chain.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "2ki5.pdb"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_pdb_path"]["path"] = file_path
    input_yaml_path = Path("fix_side_chain.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert Path("system.pdb").exists()
