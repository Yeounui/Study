#setwd("Courses/Modeling_And_Simulation_Of_Biosystems/Parameter_Estimation")

source("Functions.R")

# Reading the data
grassdata <- read.table("grassdata.txt", header = TRUE)
attach(grassdata)

# Set Starting values
pexp <- c(10, 0.01)
plogit <- c(0.1, 10, 0.01)
pgomp <- c(2, 0.01, 0.01)

# Minimizing the objective function
expfit <- optim(par = pexp, fn = Jtheta, lower = c(8, 0), upper = c(12, 1), method = "L-BFGS-B", 
		FUN = expfun, xdata = grassdata$Day, ydata = grassdata$Yield)
expfit     # 10.69223106  0.03114085     Value: 5.940612

logitfit <- optim(par = plogit, fn = Jtheta, lower = c(0, 8, 0), upper = c(5, 12, 0.7), method = "L-BFGS-B",
		FUN = logitfun, xdata = grassdata$Day, ydata = grassdata$Yield)
logitfit   # 2.07744535 9.74918130 0.06602125     Value: 0.5579139

gompfit <- optim(par = pgomp, fn = Jtheta, lower = c(0, 0.01, 0.01), upper = c(10, 1, 1), method = "L-BFGS-B",
		FUN = gompfun, xdata = grassdata$Day, ydata = grassdata$Yield)
gompfit    # 2.03850534 0.06765377 0.04168066     Value: 0.0.8573189

# Plot the data and fitted curves
#pdf("parameterestimation.pdf")
plot(x = grassdata$Day, y = grassdata$Yield, 
	ylim = c(0, 10), xlim = c(0, 80),
	ylab = "Yield (ton/ha)", xlab = "Day", 
	pch = 19)
xseq <- seq(min(grassdata$Day),max(grassdata$Day), 1)
lines(x = xseq, y = expfun(xseq, expfit$par), lty = "dashed")
lines(x = xseq, y = logitfun(xseq, logitfit$par), lty = "solid")
lines(x = xseq, y = gompfun(xseq, gompfit$par), lty = "dotdash")
legend(x = "bottomright", 
		legend = c("Exponential Growth Function", "Logistic Growth Function", "Gompertz Growth Function"), 
		lty = c("dashed", "solid", "dotdash"))
#dev.off()

# If standard Nelder-Mead is used, initial values need to be adapted some to get good results
pexp2 <- c(10, 0.1)
plogit2 <- c(1, 10, 0.05)
pgomp2 <- c(2, 0.01, 0.01)

expfit2 <- optim(par = pexp2, fn = Jtheta, 
                FUN = expfun, xdata = grassdata$Day, ydata = grassdata$Yield)
expfit2    # 10.71831401  0.03095498     Value: 5.940328

logitfit2 <- optim(par = plogit2, fn = Jtheta, 
                  FUN = logitfun, xdata = grassdata$Day, ydata = grassdata$Yield)
logitfit2  # 2.08035110 9.75203786 0.06592504     Value: 0.5578974

gompfit2 <- optim(par = pgomp2, fn = Jtheta,
                 FUN = gompfun, xdata = grassdata$Day, ydata = grassdata$Yield)
gompfit2   # 2.04220639 0.06688204 0.04109712     Value: 0.8551687

plot(x = grassdata$Day, y = grassdata$Yield, 
     ylim = c(0, 10), xlim = c(0, 80),
     ylab = "Yield (ton/ha)", xlab = "Day", 
     pch = 19)
xseq <- seq(min(grassdata$Day),max(grassdata$Day), 1)
lines(x = xseq, y = expfun(xseq, expfit2$par), lty = "dashed")
lines(x = xseq, y = logitfun(xseq, logitfit2$par), lty = "solid")
lines(x = xseq, y = gompfun(xseq, gompfi2t$par), lty = "dotdash")
legend(x = "bottomright", 
       legend = c("Exponential Growth Function", "Logistic Growth Function", "Gompertz Growth Function"), 
       lty = c("dashed", "solid", "dotdash"))

# If you start at (1,1) for exponential, you arrive at a local minimum
pexp3 <- c(1, 1)

expfit3 <- optim(par = pexp3, fn = Jtheta, 
                 FUN = expfun, xdata = grassdata$Day, ydata = grassdata$Yield)
expfit$value      # 5.940328
expfit2$value     # 5.940328
expfit3$value     # 23.29
