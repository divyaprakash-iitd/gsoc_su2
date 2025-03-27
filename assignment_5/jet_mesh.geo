Point(1) = {0, 0, 0, 1.0};
Point(2) = {0, 0.1, 0, 1.0};
Point(3) = {0, 0.01, 0, 1.0};
Point(4) = {1.0, 0.02, 0, 1.0};
Point(5) = {0.5, 0, 0, 1.0};
Point(6) = {0.5, 0.1, 0, 1.0};
//+
Line(1) = {1, 5};
Line(2) = {3, 4};
Line(3) = {1, 3};
Line(4) = {5, 4};
Line(5) = {2, 2};
Line(6) = {2, 6};
Line(7) = {3, 2};
Line(8) = {4, 6};
//+
Curve Loop(1) = {1, 4, -2, -3};
Plane Surface(1) = {1};
Curve Loop(2) = {2, 8, -6, -7};
Plane Surface(2) = {2};

//+
Transfinite Curve {1, 2, 6} = 150 Using Progression 1; // 20
Transfinite Curve {3, 4} = 50 Using Progression 1; // 10
Transfinite Curve {7, 8} = 75 Using Progression 1; // 15
Transfinite Surface {1};
Transfinite Surface {2};
Recombine Surface {1, 2};
//+
Physical Curve("inlet", 9) = {3};
Physical Curve("outlet", 10) = {4};
Physical Curve("symmetry", 11) = {1};
Physical Curve("outlet_coflow", 12) = {8};
Physical Curve("inlet_coflow", 13) = {7};
Physical Curve("farfield", 14) = {6};

