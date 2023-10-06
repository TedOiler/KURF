library(AlgDesign)
library(OptimalDesign)
#use nlargest = 5 as example 
#compute FullFactor Design around local optimal
nlargest = 1
upperbound = 6.27*nlargest
lowerbound = 6.29*nlargest
dat <- gen.factorial(3,2)
dat[dat==-1]=lowerbound
dat[dat==0]=(lowerbound+upperbound)/2
dat[dat==1]=upperbound
FullFacIni <-dat

#compute D-optimal Design with 7 initial sample 
Fx <- Fx_cube(~x1 + x2 + I(x1^2) + I(x2^2) + I(x1*x2), n.levels=c(51, 51))
keep <- rep(TRUE, nrow(Fx))
  for(i in 1:nrow(Fx)) if(prod(abs(Fx[i, 2:3])) > 0.2) keep[i] <- FALSE
Fx <- Fx[keep, ]
w <-od_KL(Fx, 7, bin=TRUE, t.max=5)$w.best
w <-od_plot(Fx = Fx, w = w, X = Fx[, 2:3], return.pools = TRUE)$Pool
my_df <- data.frame(w)
dat_2 <- subset(my_df, V3 != 0)
dat_2[dat_2==-1]=lowerbound
dat_2[dat_2==1]=upperbound
dat_2[dat_2==0.2]=(lowerbound+upperbound)/2+0.2*0.01*nlargest
dat_2[dat_2==-0.2]=(lowerbound+upperbound)/2-0.2*0.01*nlargest
dat_2[dat_2==0]=(lowerbound+upperbound)/2
DoptimalIni<-dat_2

#compute D-optimal Design with 11 initial sample
Fx <- Fx_cube(~x1 + x2 + I(x1^2) + I(x2^2) + I(x1*x2), n.levels=c(51, 51))
keep <- rep(TRUE, nrow(Fx))
for(i in 1:nrow(Fx)) if(prod(abs(Fx[i, 2:3])) > 0.2) keep[i] <- FALSE
Fx <- Fx[keep, ]
w <-od_KL(Fx, 11, bin=TRUE, t.max=5)$w.best
w <-od_plot(Fx = Fx, w = w, X = Fx[, 2:3], return.pools = TRUE)$Pool
my_df <- data.frame(w)
dat_3 <- subset(my_df, V3 != 0)
dat_3[dat_3==-1]=lowerbound
dat_3[dat_3==1]=upperbound
dat_3[dat_3==0.2]=(lowerbound+upperbound)/2+0.2*0.01*nlargest
dat_3[dat_3==-0.2]=(lowerbound+upperbound)/2-0.2*0.01*nlargest
dat_3[dat_3==0]=(lowerbound+upperbound)/2
dat_3[dat_3==-0.16]=(lowerbound+upperbound)/2-0.16*0.01*nlargest
dat_3[dat_3==-0.04]=(lowerbound+upperbound)/2-0.04*0.01*nlargest
DoptimalIni_11<-dat_3

#compute D-optimal Design with 13 initial sample
Fx <- Fx_cube(~x1 + x2 + I(x1^2) + I(x2^2) + I(x1*x2), n.levels=c(51, 51))
keep <- rep(TRUE, nrow(Fx))
for(i in 1:nrow(Fx)) if(prod(abs(Fx[i, 2:3])) > 0.2) keep[i] <- FALSE
Fx <- Fx[keep, ]
w <-od_KL(Fx, 13, bin=TRUE, t.max=5)$w.best
w <-od_plot(Fx = Fx, w = w, X = Fx[, 2:3], return.pools = TRUE)$Pool
my_df <- data.frame(w)
dat_4 <- subset(my_df, V3 != 0)
dat_4[dat_4==-1]=lowerbound
dat_4[dat_4==1]=upperbound
dat_4[dat_4==0.2]=(lowerbound+upperbound)/2+0.2*0.01*nlargest
dat_4[dat_4==-0.2]=(lowerbound+upperbound)/2-0.2*0.01*nlargest
dat_4[dat_4==0]=(lowerbound+upperbound)/2
dat_4[dat_4==-0.16]=(lowerbound+upperbound)/2-0.16*0.01*nlargest
dat_4[dat_4==-0.04]=(lowerbound+upperbound)/2-0.04*0.01*nlargest
dat_4[dat_4==0.16]=(lowerbound+upperbound)/2+0.16*0.01*nlargest
dat_4[dat_4==0.04]=(lowerbound+upperbound)/2+0.04*0.01*nlargest
DoptimalIni_13<-dat_4

#compute I-Optimal Design with 12 initial sample
Fx <- Fx_cube(~x1 + x2 + I(x1^2) + I(x2^2) + I(x1*x2), n.levels=c(51, 51))
keep <- rep(TRUE, nrow(Fx))
  for(i in 1:nrow(Fx)) if(prod(abs(Fx[i, 2:3])) > 0.2) keep[i] <- FALSE
Fx <- Fx[keep, ]
w <-od_KL(Fx, 12, bin=TRUE, t.max=5, crit='I')$w.best\
w <-od_plot(Fx = Fx, w = w, X = Fx[, 2:3], return.pools = TRUE)$Pool
my_df <- data.frame(w)
dat_2 <- subset(my_df, V3 != 0)
dat_2 = dat_2*((upperbound-lowerbound)/2) + ((upperbound+lowerbound)/2)