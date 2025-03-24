# GSoC 2025 Assignments for SU2

## Assignment-1: SU2 Installation with MPI and Python Wrappers

### Prerequisites
- OpenMPI 4.1.2 (verified with `mpirun --version`)
- SWIG (installed via package manager)
- Python 3 with mpi4py

### Installation Commands
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

## Assignment 2: Turbulent Jet Case
The provided geo file was used to create the mesh using gmsh and converted to su2 format using the following.
```bash
gmsh -2 jet_mesh.geo -save_all -o jet_mesh.su2 -format su2
```
The following changes were made.
1. The width of the domain was increased to 10 times the jet diameter.
2. The mesh was refined further
![Mesh](assignment_2/gsoc_2_mesh.png)

The configuration file of [Sandia Jet](https://github.com/su2code/VandV/tree/master/rans/SANDIA_jet) was used as starting point and changes were made to it according to the details in the provided [paper](https://www.researchgate.net/publication/254224677_Investigation_of_the_Mixing_Process_in_an_Axisymmetric_Turbulent_Jet_Using_PIV_and_LIF).

A simulation was run and some plots are shown below.

![Velocity Contours](assignment_2/gsoc_2_velocity.png)
![Residual Plot](assignment_2/rms_residuals.png)

## Assignment 3: Using Python Wrapper
The mesh was downloaded from [here](https://github.com/su2code/TestCases/blob/master/py_wrapper/flatPlate_unsteady_CHT/2D_FlatPlate_Rounded.su2).

```bash
mpirun -np 4 python3 -m mpi4py launch_unsteady_CHT_FlatPlate.py --parallel -f unsteady_CHT_FlatPlate_Conf.cfg
```

## Assignment 4: Modification of the python wrapper setup


## Assignment 5: Addition of New Volume Output
