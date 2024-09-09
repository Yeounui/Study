
# Exponential growth function
expfun <- function(xdata, thetas) {
	e <- thetas[1] * (1 - exp(-thetas[2] * xdata))
	return(e)
}

# Gompertz growth function
gompfun <- function(xdata, thetas) {
	g <- thetas[1] * exp(thetas[2] * (1 - exp(-thetas[3] * xdata)) / thetas[3])
	return(g)
}

# Logistic growth function
logitfun <- function(xdata, thetas) {
	l <- (thetas[1] * thetas[2]) / (thetas[1] + (thetas[2] - thetas[1]) * exp(-thetas[3] * xdata))
	return(l)
}

# Objective function
Jtheta <- function(thetas, FUN, xdata, ydata) {
	ydatahat <- do.call(FUN, list(xdata, thetas))
	yresid <- ydata - ydatahat
	J <- sum(yresid^2)
	return(J)
}

# Akaike Information Criterion (AIC)
AIC <- function(thetas, FUN, xdata, ydata) {
  RSS <- Jtheta (thetas, FUN, xdata, ydata)
	N <- length(xdata)
	p <- length(thetas)
	A <- N * log(RSS / N) + 2 * p
	return(A)
}

# F-test
Ftest <- function(thetas1, thetas2, FUN1, FUN2, xdata, ydata) {

	RSS1 <- Jtheta(thetas1, FUN1, xdata, ydata)
	RSS2 <- Jtheta(thetas2, FUN2, xdata, ydata)
	
	N <- length(xdata)
	p1 <- length(thetas1)
	p2 <- length(thetas2)
	F <- ((RSS1 - RSS2) / (p2 - p1)) / (RSS2 / (N - p2))
	
	pvalue <- pf(F, df1 = p2 - p1, df2 = N - p2, lower.tail = FALSE)
	return(list(F = F, df1 = abs(p2 - p1), df2 = N - p2, pValue = pvalue))
}


# The main functions to interact with the F-distribution are df(), pf(), qf(), rf(). 
# The df() function gives the density, 
# the pf() function gives the distribution function, 
# the qf() function gives the quantile function, 
# and the rf() function generates random deviates.



