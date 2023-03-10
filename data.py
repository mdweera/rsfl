from tensorflow.examples.tutorials.mnist import input_data

class Dataset:
    def __init__(self):
        self.mnist = input_data.read_data_sets("./", one_hot=True)
        self.num_samples = self.mnist.train._num_examples
        self.batch_size = 128
        self.num_batches = int(self.num_samples / self.batch_size)
        print(self.num_samples)

    def get_test_data(self):
        return (self.mnist.test.images, self.mnist.test.labels)

    def get_train_data(self):
        return (self.mnist.train.images, self.mnist.train.labels)

    def get_validation_data(self):
        return (self.mnist.validation.images, self.mnist.validation.labels)