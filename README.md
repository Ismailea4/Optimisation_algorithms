# Optimisation_algorithms
A package contain Algorithms to minimise functions (1D or multivariate) with Algorithms of decomposition and inversing matrix

## How to use :
_After installing the package use following import :_ <br>

For 1 dimensionel minimisation : <br>
**from Optimisation_tools.minimisation_1D import 
  Unrestricted_fixed_Step,
  Unrestricted_accelerated_Step,
  ExSearch_method,
  Interval_Halving,
  Dichotomous,
  Fibonacci,
  Golden_Section,
  Newton_1D,
  Quasi_Newton_1D,
  Secant_1D**

For multivariate minimisation : <br>
**from Optimisation_tools.multivariate_minimisation import
  Methode_Newton,
  Methode_Newton2,
  Quasi_Newton,
  descant_gradient,
  Conjugate_gradient**

For Matrix decomposition and inverse : <br>
**from Optimisation_tools.matrix_decomposition_inverse import
  decomp_LU,
  LU_inv,
  Choleski_decomp,
  Choleski_inv,
  Gauss_inv**

For Search step : <br>
**from Optimisation_tools.step_search
  Armijo,
  Goldstein**
  
