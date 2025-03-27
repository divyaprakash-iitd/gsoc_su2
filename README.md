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
![Computational Domain](assignment_2/c_domain.jpg)

The following changes were made.
1. The width of the domain was increased to 10 times the jet diameter.
2. The mesh was refined further
![Mesh](assignment_2/gsoc_2_mesh.png)

The configuration file of [Sandia Jet](https://github.com/su2code/VandV/tree/master/rans/SANDIA_jet) was used as starting point and changes were made to it according to the details in the provided [paper](https://www.researchgate.net/publication/254224677_Investigation_of_the_Mixing_Process_in_an_Axisymmetric_Turbulent_Jet_Using_PIV_and_LIF).

A simulation was run and some plots are shown below.

<p align="center">
  <img src="assignment_2/rms_residuals.png" alt="convergence plot">
  <br>
  <em>Convergence plot</em>
</p>

<p align="center">
  <img src="assignment_2/gsoc_2_velocity.png" alt="velocity contours">
  <br>
  <em>Velocity magnitude contours</em>
</p>

## Assignment 3: Using Python Wrapper
The mesh was downloaded from [here](https://github.com/su2code/TestCases/blob/master/py_wrapper/flatPlate_unsteady_CHT/2D_FlatPlate_Rounded.su2).

<p align="center">
  <img src="assignment_3/gsoc_3_temp.png" alt="mesh">
  <br>
  <em>Computational Mesh</em>
</p>

The simulation was run using the python wrapper.
```bash
mpirun -np 4 python3 -m mpi4py launch_unsteady_CHT_FlatPlate.py --parallel -f unsteady_CHT_FlatPlate_Conf.cfg
```
<p align="center">
  <img src="assignment_3/gsoc_3_temp.webp" alt="Filled contours showing temperature variation of one complete cycle">
  <br>
  <em>Filled contours showing temperature variation of one complete cycle</em>
</p>


## Assignment 4: Modification of the python wrapper setup

This was done in two steps.
1. The simulation from assignment 3 was converted to steady state
2. The temporal variation was changed to spatial using the following.
```python
for iVertex in range(nVertex_CHTMarker):
    WallTemp = 293.0 + 57.0*sin(2*pi* iVertex / (nVertex_CHTMarker - 1))
    SU2Driver.SetMarkerCustomTemperature(CHTMarkerID, iVertex, WallTemp)
```

<p align="center">
  <img src="assignment_4/gsoc_4_temp.png" alt="Spatial varying temperature">
  <br>
  <em>The warped surface showing the sinusoidally varying temperature</em>
</p>

<p align="center">
  <img src="assignment_4/rms_residuals.png" alt="convergence plot">
  <br>
  <em>Convergence plot</em>
</p>

<p align="center">
  <img src="assignment_4/gsoc_4_temp_c.png" alt="temperature plot">
  <br>
  <em>Temperature contours</em>
</p>

## Assignment 5: Addition of New Volume Output
Changes in the source code
```diff
diff --git a/assignment_5/CFlowCompOutput.cpp b/assignment_5/CFlowCompOutput.cpp
index e460109..9254964 100644
--- a/assignment_5/CFlowCompOutput.cpp
+++ b/assignment_5/CFlowCompOutput.cpp
@@ -50,2 +50,3 @@ CFlowCompOutput::CFlowCompOutput(const CConfig *config, unsigned short nDim) : C
     requestedScreenFields.emplace_back("RMS_ENERGY");
+    requestedScreenFields.emplace_back("RMS_SS");
     nRequestedScreenFields = requestedScreenFields.size();
@@ -101,2 +102,5 @@ void CFlowCompOutput::SetHistoryOutputFields(CConfig *config){
 
+  // My Addition
+  AddHistoryOutput("RMS_SS",    "rms[SS]",  ScreenOutputFormat::FIXED, "RMS_SS", "Root-mean square of sound speed.", HistoryFieldType::RESIDUAL);
+  
   /// BEGIN_GROUP: RMS_RES, DESCRIPTION: The root-mean-square residuals of the SOLUTION variables.
@@ -240,2 +244,6 @@ void CFlowCompOutput::SetVolumeOutputFields(CConfig *config){
   AddVolumeOutput("MACH",        "Mach",                    "PRIMITIVE", "Mach number");
+  
+  // My Addition
+  AddVolumeOutput("SOUNDSPEED",        "Soundspeed",                    "PRIMITIVE", "local speed of sound");
+  
   AddVolumeOutput("PRESSURE_COEFF", "Pressure_Coefficient", "PRIMITIVE", "Pressure coefficient");
@@ -337,2 +345,5 @@ void CFlowCompOutput::LoadVolumeData(CConfig *config, CGeometry *geometry, CSolv
   
+  // My Addition
+  SetVolumeOutputValue("SOUNDSPEED", iPoint, Node_Flow->GetSoundSpeed(iPoint));
+
   const su2double factor = solver[FLOW_SOL]->GetReferenceDynamicPressure();
@@ -394,2 +405,6 @@ void CFlowCompOutput::LoadHistoryData(CConfig *config, CGeometry *geometry, CSol
 
+
+  // My Addition
+  SetHistoryOutputValue("RMS_SS", log10(flow_solver->GetRes_RMS(0)));
+
   SetHistoryOutputValue("RMS_DENSITY", log10(flow_solver->GetRes_RMS(0)));
```
