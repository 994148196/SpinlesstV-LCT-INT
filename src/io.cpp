#include "interaction_expansion.hpp"
#include <iostream>

void InteractionExpansion::print(std::ostream &os) const{
  os<<"***********************************************************************************************************"<<std::endl;
  os<<"***                                      CTBSS for spinless fermions                                    ***"<<std::endl;
  os<<"***                                      Lei Wang, ETH Zurich, 2014                                     ***"<<std::endl;
  os<<"***                                      lewang@phys.ethz.ch                                            ***"<<std::endl;
  os<<"***********************************************************************************************************"<<std::endl;
  os<<"n_bond: "<< n_bond << std::endl; 
  os<<"max order: "<<max_order << std::endl; 
  os<<"mc steps: "<<mc_steps << ",\ttherm steps: "<<therm_steps << std::endl;
  os<<"itime_max: " <<  itime_max << ",\tnblock: "<<nblock<<",\tsteps_per_block: "<< steps_per_block << std::endl; 
  os<<"recalc_period: "<< recalc_period<<",\tblocksize: "<< blocksize << std::endl; 
  os<<"T: "<<temperature<<",\tV: "<<V<<std::endl;
}

