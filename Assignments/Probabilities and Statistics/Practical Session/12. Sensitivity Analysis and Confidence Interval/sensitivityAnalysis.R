setwd("...")

source("Functions.R")

grassdata <- read.table("grassdata.txt", header = TRUE)

pexp <- c(10, 0.01)
plogit <- c(0.1, 10, 0.01)
pgomp <- c(2, 0.01, 0.01)

expfit <- optim(par = pexp, fn = Jtheta, lower = c(8, 0), upper = c(12, 1), method = "L-BFGS-B", 
		FUN = expfun, xdata = grassdata$Day, ydata = grassdata$Yield)

logitfit <- optim(par = plogit, fn = Jtheta, lower = c(0, 8, 0), upper = c(5, 12, 0.7), method = "L-BFGS-B",
		FUN = logitfun, xdata = grassdata$Day, ydata = grassdata$Yield)

gompfit <- optim(par = pgomp, fn = Jtheta, lower = c(0, 0.01, 0.01), upper = c(10, 1, 1), method = "L-BFGS-B",
		FUN = gompfun, xdata = grassdata$Day, ydata = grassdata$Yield)

# sensitivity functions
sensLogit <- sensitivity(FUN = logitfun, thetas = logitfit$par, xdata = 0:100, eps = 1e-5)
sensExp <- sensitivity(FUN = expfun, thetas = expfit$par, xdata = 0:100, eps = 1e-5)
sensGomp <- sensitivity(FUN = gompfun, thetas = gompfit$par, xdata = 0:100, eps = 1e-5)

# plot the sensitivity function for every parameter
plotSens <- function(sens, parNames = c("W0", "Wf", "mu")) {
	require(ggplot2)
	require(reshape2)
	
	Sens <- as.data.frame(sens)
	colnames(Sens) <- parNames
	Sens.m <- melt(data.frame(x = 0:100, Sens), id.vars = "x")
	print(Sens.m)
	gg <- ggplot(Sens.m, aes(x = x, y = value)) + 
			geom_line() + ylab(expression(paste("Sensitivity  ",bgroup("(",over(delta~y[j],delta~theta[i]),")")))) + xlab("Day") +
			facet_grid(variable ~ ., scales = 'free', labeller = label_parsed)+
			theme_bw()+theme(strip.background = element_rect(fill = "white"), strip.text.y = element_text(angle = 0))
	
	return(gg)
}

# plotSens(sens = sensLogit, parNames = c("W0", "Wf", "mu"))
# plotSens(sens = sensExp, parNames = c("Wf", "mu"))
# plotSens(sens = sensGomp, parNames = c("W0", "mu", "D"))

pdf("sensitivityLogit.pdf", width = 8, height = 5)
plotSens(sens = sensLogit, parNames = c("W0", "Wf", "mu"))
dev.off()
pdf("sensitivityExponential.pdf", width = 8, height = 5)
plotSens(sens = sensExp, parNames = c("Wf", "mu"))
dev.off()
pdf("sensitivityGompertz.pdf", width = 8, height = 5)
plotSens(sens = sensGomp, parNames = c("W0", "mu", "D"))
dev.off()


# Fisher Information Matrix
FIM <- FisherInformation(thetas = logitfit$par, FUN = logitfun, xdata = grassdata$Day)

confInterval(thetas = logitfit$par, FUN = logitfun, xdata = grassdata$Day)
confInterval(thetas = expfit$par, FUN = expfun, xdata = grassdata$Day)
confInterval(thetas = gompfit$par, FUN = gompfun, xdata = grassdata$Day)

