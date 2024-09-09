if (!require(deSolve)) install.packages('deSolve')
library(deSolve)

#' Solve the Monod dynamics.
#'
#' Note: you should *NOT* have to call this function yourselves. Use
#' `single.monod` and `double.monod` instead.
monod.solve <- function(times, log_alpha, log_beta, log_s0) {
  monod.rhs <- function(t, state, parameters) {
    with(as.list(c(state, parameters)), {
      list(c(-alpha * s / (beta + s)))
    })
  }
  
  state <- c(s = exp(log_s0))
  parameters <- c(alpha = exp(log_alpha), beta = exp(log_beta))
  sol <-
    ode(
      y = state,
      times = times,
      parms = parameters,
      func = monod.rhs
    )
  return(sol[, "s"])
}

#' Dynamics of the single Monod model.
#'
#' Takes a vector `times` of time points and a vector `thetas` of
#' parameters (alpha, beta, S0) and returns the fitted OUR at those
#' time points.
single.monod <- function(times, thetas) {
  s <- do.call(monod.solve, c(list(times=times), as.list(thetas)))
  exp(thetas[1]) * s / (exp(thetas[2]) + s)
}

#' Dynamics of the double Monod model.
#'
#' Like the single Monod model, takes a vector `times` of time points
#' and a vector `thetas` of parameters (alpha1, beta1, S1.0, alpha2,
#' beta2, S2.0) and returns the fitted OUR at those time points.
double.monod <- function(times, thetas) {
  s1 <- do.call(monod.solve, c(list(times=times), as.list(thetas[1:3])))
  s2 <- do.call(monod.solve, c(list(times=times), as.list(thetas[4:6])))
  exp(thetas[1]) * s1 / (exp(thetas[2]) + s1) + 
    exp(thetas[4]) * s2 / (exp(thetas[5]) + s2)
}
