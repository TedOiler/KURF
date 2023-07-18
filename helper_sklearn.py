import numpy as np
from scipy.stats import norm
import random


def surrogate(model, X):
  return model.predict(X, return_std=True)

def acq_pi(X, Xsamples, model):
  yhat, _ = surrogate(model, X)
  best = max(yhat) # calculate the best so far

  mu, std = surrogate(model, Xsamples)
  mu = mu[:, 0]
  gamma = (mu - best) / (std + 1E-9)
  probs = norm.cdf(gamma) # add a very small number to std to avoid dividing with 0
  return probs

def acq_ei(X, Xsamples, model):
  yhat, _ = surrogate(model, X)
  best = max(yhat) # calculate the best so far

  mu, std = surrogate(model, Xsamples)
  mu = mu.reshape(-1,1)[:, 0]
  gamma = (mu-best)/(std + 1E-9) # add a very small number to std to avoid dividing with 0
  probs = std * (gamma * norm.cdf(gamma)) + norm.pdf(gamma)
  return probs

def opt_acq(X, y, model, acq=acq_ei):
  Xsamples = np.random.uniform(low=30.0, high=120.0, size=(1000,1)) # can be improved upon
  scores = acq(X, Xsamples, model)
  ix = np.argmax(scores)
  return Xsamples[ix, 0]