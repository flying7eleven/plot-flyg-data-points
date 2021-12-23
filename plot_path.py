def main():
    from argparse import ArgumentParser
    from json import load
    from numpy import array
    from matplotlib.pyplot import imread, subplots, show

    # parse the arguments provided by the user
    parser = ArgumentParser(description='Tool for plotting the path of a flight into a map image')
    parser.add_argument('flyg_file')
    parser.add_argument('map_image_file')
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

    # determine the bounding box for the plot
    bounding_box = ((longitudes.min(), longitudes.max(), latitudes.min(), latitudes.max()))

    # read the image and prepare the plotting environment
    map_img = imread(args.map_image_file)
    fix, ax = subplots(figsize=(8, 7))

    # do the actual plot and rendering of the image
    ax.scatter(longitudes, latitudes, zorder=1, alpha=0.2, c='b', s=10)
    ax.set_title('Mapped Flyg flight path onto an map image')
    ax.set_ylabel('Longitude')
    ax.set_xlabel('Latitude')
    ax.set_xlim(bounding_box[0], bounding_box[1])
    ax.set_ylim(bounding_box[2], bounding_box[3])
    ax.imshow(map_img, zorder=0, extent=bounding_box, aspect='equal')

    # show the plot
    show()


if __name__ == '__main__':
    main()
