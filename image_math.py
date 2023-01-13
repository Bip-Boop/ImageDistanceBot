import numpy as np
from image_vectorization import VGGClassifier, InceptionClassifier

class ImageMath:
    def __init__(self, networks=('vgg16', ), active_network='vgg16'):
        # load only if needed
        self.vc = None
        self.ic = None
        self.network = None
        self.load_networks(networks)
        self.set_active_network(active_network)


    def load_networks(self, networks):
        network_set = False
        if 'vgg16' in networks:
            self.vc = VGGClassifier()
            network_set = True
        if 'inception_v3' in networks:
            self.ic = InceptionClassifier()
            network_set = True

        if not network_set:
            print(f"There are no such networks: {networks}. Please, consider choosing from the following: "  )
            ImageMath.list_possible_networks()
    
    def set_active_network(self, active_network):
        if 'vgg16' == active_network:
            if self.vc == None:
                self.vc = VGGClassifier()
            self.network = self.vc
        elif 'inception_v3' == active_network:
            if self.ic == None:
                self.ic = InceptionClassifier()
            self.network = self.ic
        else:
            print(f"There is no such network: {active_network}. Please, consider choosing one of the following: "  )
            ImageMath.list_possible_networks()

    def list_possible_networks():
        print(('vgg16', 'inception_v3'))
    
    def calculate_conscious_distance(self, filename1, filename2, network = None):
        if network is not None:
            self.set_active_network(network)
        if self.network is None:
           raise Exception("There is no active network. Please, choose one")
           
        img_vec_a = self.network.conscious_prediction(filename1)
        img_vec_b = self.network.conscious_prediction(filename2)
        dist = np.linalg.norm(img_vec_a - img_vec_b)
        return dist
    
    def calculate_subconscious_distance(self, filename1, filename2, network = None):
        if network is not None:
            self.set_active_network(network)
        if self.network is None:
           raise Exception("There is no active network. Please, choose one")
           
        img_vec_a = self.network.subconscious_prediction(filename1)
        img_vec_b = self.network.subconscious_prediction(filename2)
        dist = np.linalg.norm(img_vec_a - img_vec_b)
        return dist
    
    def calculate_names(self, filename1, filename2, network = None):
        if network is not None:
            self.set_active_network(network)
        if self.network is None:
           raise Exception("There is no active network. Please, choose one")
           
        name_a = self.network.classification_prediction(filename1)
        name_b = self.network.classification_prediction(filename2)

        return name_a, name_b