"""Package entrypoint for the check_linear_fit package."""

# Base packages
import logging
import sys
from os import environ

import typer
from polus.mm.utils.fitting.check_linear_fit.check_linear_fit import check_linear_fit

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.check_linear_fit.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="check_linear_fit.")


@app.command()
def main(
    xs: list[float] = typer.Option(
        ...,
        "--xs",
        help="",
    ),
    ys: list[float] = typer.Option(
        ...,
        "--ys",
        help="",
    ),
    tol_quad: float = typer.Option(
        ...,
        "--tol_quad",
        help="",
    ),
    slope_min: float = typer.Option(
        ...,
        "--slope_min",
        help="",
    ),
    slope_max: float = typer.Option(
        ...,
        "--slope_max",
        help="",
    ),
) -> None:
    """check_linear_fit."""
    logger.info(f"xs: {xs}")
    logger.info(f"ys: {ys}")
    logger.info(f"tol_quad: {tol_quad}")
    logger.info(f"slope_min: {slope_min}")
    logger.info(f"slope_max: {slope_max}")

    is_linear_and_within_bounds = check_linear_fit(
        xs=xs,
        ys=ys,
        tol_quad=tol_quad,
        slope_min=slope_min,
        slope_max=slope_max,
    )
    if is_linear_and_within_bounds:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    app()
