class Conf(object):
    def __init__(self, args):
        self.args = args
        self.dataset = args.dataset

    def _set_path(self, dataset_type):
        if self.dataset == 'TIHM':
            return './{}/tihm15'.format(dataset_type)
        elif self.dataset == 'DRI':
            return './{}/tihmdri'.format(dataset_type)

    @property
    def raw_data(self):
        return self._set_path('raw_data')

    @property
    def csv_data(self):
        return self._set_path('csv_data')

    @property
    def npy_data(self):
        return self._set_path('npy_data')

    @property
    def data_path(self):
        data_path = {
            'env': self._set_path('csv_data') + '/env/data/',
            'flag': self._set_path('csv_data') + '/env/flag/',
            'clinical': self._set_path('csv_data') + '/clinical/data/',
        }
        return data_path


# Validated UTI, may not in the flags files

def validated_date():
    patient_data = {
        '1077': ['2020-10-06'],
        '1313': ['2020-10-06'],
    }
    return patient_data