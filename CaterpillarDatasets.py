# opening hdf files
import h5py


filename = 'file1.hdf'


def open_file(filename):
    with h5py.File(filename, 'r') as f:
        # List all groups
        print("Keys: %s" % f.keys())
        a_group_key = list(f.keys())[0]

        # Get the data
        data = list(f[a_group_key])

        print data



def main():
    filename = '/Users/devanshi/Downloads/Caterpillar Inital Data/file1.hdf'
    open_file(filename)


if __name__ == "__main__":
    main()
