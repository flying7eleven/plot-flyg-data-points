def main():
    from argparse import ArgumentParser
    from json import load
    from numpy import array

    # parse the arguments provided by the user
    parser = ArgumentParser(description='Tool for determining the dimensions for the OSM map export')
    parser.add_argument('flyg_file')
    args = parser.parse_args()

    # try to load the flyg data file
    with open(args.flyg_file, 'r') as file_handle:
        flyg_data = load(file_handle)

    # convert the data set to the required format for easier processing
    longitudes = []
    latitudes = []
    for current_plane_position in flyg_data['planePositions']:
        longitudes.append(current_plane_position['longitude'])
        latitudes.append(current_plane_position['latitude'])
    longitudes = array(longitudes)
    latitudes = array(latitudes)

    # print the bounding box the user has to set on OSM
    print(f'Left:\t{longitudes.min():.4f}')
    print(f'Top:\t{latitudes.min():.4f}')
    print(f'Right:\t{longitudes.max():.4f}')
    print(f'Bottom:\t{latitudes.max():.4f}')


if __name__ == '__main__':
    main()
