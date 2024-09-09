
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


# Get the sensitivity function for every parameter
sensitivity <- function(FUN, thetas, xdata = 0:80, eps = 1e-5) {
	yhat <- do.call(FUN, list(xdata, thetas))
	S <- matrix(NA, nrow = length(xdata), ncol = length(thetas))
	for (p in 1:length(thetas)) {
		thetas. <- thetas
		thetas.[p] <- thetas[p] * (1+eps)
		yhat. <- do.call(FUN, list(xdata, thetas.))
		S[, p] <- (yhat. - yhat) / (eps*thetas[p])
	}
	
	return(S)
}

relativeSensitivity <- function(FUN, thetas, xdata = 0:80, eps = 1e-5) {
	yhat <- do.call(FUN, list(xdata, thetas))
	S <- matrix(NA, nrow = length(xdata), ncol = length(thetas))
	for (p in 1:length(thetas)) {
		thetas. <- thetas
		thetas.[p] <- thetas[p] * (1+eps)
		yhat. <- do.call(FUN, list(xdata, thetas.))
		S[, p] <- ((yhat. - yhat) / (eps*thetas[p])) * abs(thetas[p])
	}
	
	return(S)
}

# Get the Fisher Information Matrix
FisherInformation <- function(thetas, FUN, xdata, eps = 1e-5) {
	sens <- sensitivity(FUN, thetas, xdata, eps)
	FIM <- t(sens)%*%sens
	return(FIM)
}

confInterval <- function(thetas, FUN, xdata, alpha = 0.05, eps = 1e-5) {
	FIM <- FisherInformation(thetas, FUN, xdata, eps)
	C <- solve(FIM)
	StDev <- sqrt(diag(C))
	N <- length(xdata)
	p <- length(thetas)
	t.05 <- qt(p = 1-alpha/2, df = N-p)
	
	return(StDev*t.05)
}

ModelLogit <- function(X, inputvalue, thetas = logitfit$par) {
	# do a transformation of input values based on thetas because sobolroalhs 
	# only considers models whose inputs follow uniform distributions on [0, 1]
	X <- matrix(mapply(function(x, theta){ (1.1*theta - 0.9*theta) * x + 0.9*theta }, 
					X, thetas), 
			ncol=ncol(X), nrow=nrow(X), byrow = TRUE)
	# apply the logistic function
	l <- apply(X, 1, function(x){logitfun(inputvalue, x)})
	return(l)
}

