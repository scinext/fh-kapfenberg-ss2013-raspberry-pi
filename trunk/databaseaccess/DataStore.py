import abc

class DataStore(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_samples(self,fromTimestamp,toTimestamp):
        pass

    @abc.abstractmethod
    def add_sample(self, measurement):
        pass