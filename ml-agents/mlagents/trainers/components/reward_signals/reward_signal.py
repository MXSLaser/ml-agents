import logging
from mlagents.trainers.trainer import UnityTrainerException
from mlagents.trainers.policy import Policy

import tensorflow as tf

logger = logging.getLogger("mlagents.trainers")


class RewardSignal(object):
    def __init__(self, policy: Policy, strength, gamma):
        """
        Initializes a reward signal. At minimum, you must pass in the policy it is being applied to, 
        the reward strength, and the gamma (discount factor.)
        """
        raise UnityTrainerException("The initialize for this RewardSignal was not implemented.")

    def evaluate(self, current_info, next_info):
        """
        Evaluates the reward for the agents present in current_info given the next_info
        :current_info: The current BrainInfo. 
        :next_info: The BrainInfo from the next timestep.
        :return: a tuple of (scaled intrinsic reward, unscaled intrinsic reward) provided by the generator
        """
        raise UnityTrainerException("The evaluate for this RewardSignal was not implemented.")


    def update(self, training_buffer, n_sequences):
        """
        If the reward signal has an internal model (e.g. GAIL or Curiosity), update that model.
        :param training_buffer: The training buffer
        :param n_sequences: The number of sequences in the training buffer.
        :return: A dict of {"Stat Name": stat} to be added to Tensorboard
        """
        raise UnityTrainerException("The update for this RewardSignal was not implemented.")

    @classmethod
    def check_config(cls, config_dict, param_keys=[]):
        """
        Check the config dict, and throw an error if there are missing hyperparameters.
        """
        for k in param_keys:
            if k not in config_dict:
                raise UnityTrainerException(
                    "The hyper-parameter {0} could not be found for {1}.".format(
                        k, cls.__name__
                    )
                )
