import openmm.openmm as mm

from miniomm.miniomm import run_omm
import miniomm.util
import miniomm
import argparse


def _banner():
    return f"""
            _         _                              
 _ __ ___  (_) _ __  (_)  ___   _ __ ___   _ __ ___  
| '_ ` _ \ | || '_ \ | | / _ \ | '_ ` _ \ | '_ ` _ \ 
| | | | | || || | | || || (_) || | | | | || | | | | |
|_| |_| |_||_||_| |_||_| \___/ |_| |_| |_||_| |_| |_|
                                               {miniomm.__version__}           
A minimalistic OpenMM MD frontend.   
https://github.com/giorginolab/miniomm
"""


def main():
    parser = argparse.ArgumentParser(
        description="MiniOMM, a minimalistic OpenMM frontend to run MD systems.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    platformNames = [
        mm.Platform.getPlatform(i).getName()
        for i in range(mm.Platform.getNumPlatforms())
    ]
    parser.add_argument(
        "--input", type=str, default="input", help="name of the input file"
    )
    parser.add_argument(
        "--platform",
        type=str,
        choices=platformNames,
        help="name of the platform to benchmark",
    )
    parser.add_argument(
        "--device", default=None, type=int, help="device index for CUDA or OpenCL"
    )
    parser.add_argument(
        "--precision",
        default="mixed",
        choices=("single", "mixed", "double"),
        help="precision mode for CUDA or OpenCL: single, mixed, or double",
    )

    args = parser.parse_args()

    print(_banner())
    run_omm(args)


if __name__ == "__main__":
    main()
