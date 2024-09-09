setwd("D:/__Google Drive__/__Ghent University__/Teaching/Probability & Statistics/PC Practical/11._Model_Selection")

source("Functions1.R")

# read the data
grassdata <- read.table("grassdata.txt", header = TRUE)

# starting values
pexp <- c(10, 0.01)
plogit <- c(0.1, 10, 0.01)
pgomp <- c(2, 0.01, 0.01)

expfit <- optim(par = pexp, fn = Jtheta, lower = c(8, 0), upper = c(12, 1), method = "L-BFGS-B", 
	FUN = expfun, xdata = grassdata$Day, ydata = grassdata$Yield)

logitfit <- optim(par = plogit, fn = Jtheta, lower = c(0, 8, 0), upper = c(5, 12, 0.7), method = "L-BFGS-B",
	FUN = logitfun, xdata = grassdata$Day, ydata = grassdata$Yield)

gompfit <- optim(par = pgomp, fn = Jtheta, lower = c(0, 0.01, 0.01), upper = c(10, 1, 1), method = "L-BFGS-B",
	FUN = gompfun, xdata = grassdata$Day, ydata = grassdata$Yield)


# Plot the data and fitted curves

pdf("parameterestimation.pdf")
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
dev.off()

# Model selection

AIC(expfit$par, expfun, grassdata$Day, grassdata$Yield)
AIC(logitfit$par, logitfun, grassdata$Day, grassdata$Yield)
AIC(gompfit$par, gompfun, grassdata$Day, grassdata$Yield)

Ftest(expfit$par, logitfit$par, expfun, logitfun, grassdata$Day, grassdata$Yield)
Ftest(expfit$par, gompfit$par, expfun, gompfun, grassdata$Day, grassdata$Yield)


