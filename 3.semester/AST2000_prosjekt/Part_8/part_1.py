import ast2000tools.utils as utils
from ast2000tools.relativity import RelativityExperiments

seed = utils.get_seed('antonabr')
experiment = RelativityExperiments(seed)

experiment.spaceship_duel(6)
