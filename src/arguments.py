import argparse


class Arguments:

    def setup(self):
        parser = argparse.ArgumentParser(
            description='Faces and eyes recognizer')

        parser.add_argument('--object_type',  action="store", dest="object_type",
                            default='FACE', type=str)
        parser.add_argument('--show_border',  action="store", dest="show_border",
                            default=True, type=self.__str2bool)
        parser.add_argument('--show_image',  action="store", dest="show_image",
                            default=True, type=self.__str2bool)

        args = parser.parse_args()
        return args.object_type, args.show_border, args.show_image

    def __str2bool(self, v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 'True', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'False', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')
