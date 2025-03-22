# SU2 Installation with MPI and Python Wrappers

## Prerequisites
- OpenMPI 4.1.2 (verified with `mpirun --version`)
- SWIG (installed via package manager)
- Python 3 with mpi4py

## Installation Commands
```bash
./meson.py build -Denable-pywrapper=true --prefix=/home/baadalvm/SU2
```

After configuration, the script displayed instructions to add environment variables to `.bashrc`:
```bash
export SU2_RUN=/home/baadalvm/SU2/bin
export SU2_HOME=/home/baadalvm/SU2
export PATH=$PATH:$SU2_RUN
export PYTHONPATH=$PYTHONPATH:$SU2_RUN
```

These variables were manually added to `.bashrc`, then:
```bash
./ninja -C build install
```

## Visualization Setup
For visualizing results, ParaView was installed in a Conda environment:
```bash
conda create -n paraview_env python=3.9
conda activate paraview_env
conda install conda-forge::paraview
```
ParaView version 5.13.2 was successfully installed and used to visualize SU2 results.
