#---Imports--------------+
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, Matern, RationalQuadratic
import numpy as np
import os
import shutil
import json
import torch
import gpytorch
from gpytorch.kernels import RBFKernel, MaternKernel, ScaleKernel
from gpytorch.models import ExactGP
from gpytorch.likelihoods import GaussianLikelihood

"""

"""
class regression_GP(ExactGP):
    def __init__(self, X_train, y_train, X_test, y_test, likelihood, \
            model_name="regression_GP"):
        super().__init__(X_train, y_train, likelihood)
        self.mean_module = gpytorch.means.ConstantMean()
        self.covar_module = ScaleKernel(RBFKernel())

        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test


    def forward(self, x):
        with gpytorch.settings.fast_pred_var():
            mean_x = self.mean_module(x)
            covar_x = self.covar_module(x)
            return gpytorch.distributions.MultivariateNormal(mean_x, covar_x)


    def train_model(self, likelihood, num_iterations, lr):
        self.train()
        likelihood.train()

        optimizer = torch.optim.Adam(self.parameters(), lr=lr)
        mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, self)

        for i in range(num_iterations):
            optimizer.zero_grad()
            output = self(self.X_train)
            loss = -mll(output, self.y_train)
            loss.backward()
            optimizer.step()


