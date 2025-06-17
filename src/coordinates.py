# Defines four corners for the city in rectangular shape.
# Top-right, top-left, bottom-left, and bottom-right.
corners = [
    (43.855470, -79.170260),
    (43.855470, -79.543510),
    (43.581173, -79.543510),
    (43.581173, -79.170260),
]

# Coordinates for points of interest in the city
UNION_STATION = (43.645869, -79.381207)
EXHIBITION_STATION = (43.635855, -79.419000)
CITY_HALL = (43.652940, -79.383840)
DUNDAS_AND_OSSINGTON = (43.649310, -79.420739)
DISTILLERY_DISTRICT = (43.650302, -79.359594)
U_OF_T = (43.662558, -79.397847)
MIDTOWN = (43.706733, -79.398300)

# List of points defining the coast line of the city.
# Used to remove points in the grid that happen to be in the water.
coast = sorted(
    [
        (43.581172, -79.543510),
        (43.581351, -79.543496),
        (43.588199, -79.535976),
        (43.591767, -79.510716),
        (43.593851, -79.509725),
        (43.595501, -79.500514),
        (43.597934, -79.498423),
        (43.601290, -79.496271),
        (43.602474, -79.492589),
        (43.610938, -79.486426),
        (43.618095, -79.483877),
        (43.629934, -79.472631),
        (43.636839, -79.459578),
        (43.629965, -79.425934),
        (43.633490, -79.403876),
        (43.645914, -79.359450),
        (43.633930, -79.348031),
        (43.654317, -79.318482),
        (43.661809, -79.317150),
        (43.671131, -79.279743),
        (43.695387, -79.255172),
        (43.700547, -79.244145),
        (43.703126, -79.239381),
        (43.735092, -79.204754),
        (43.747687, -79.186421),
        (43.755109, -79.172303),
        (43.759371, -79.153083),
        (43.765726, -79.146936),
        (43.769269, -79.140931),
        (43.794372, -79.117465),
    ],
    key=lambda x: x[1],
)

GO_TRAIN_STATIONS = [
    (43.645869, -79.381207), # Union station*
    (43.765600, -79.364523), # Oriole station
    (43.793726, -79.371188), # Old Cummer station
    (43.753787, -79.479018), # Downsview Park station*
    (43.823098, -79.302258), # Milliken station
    (43.786053, -79.284546), # Agincourt station
    (43.732648, -79.265035), # Kennedy station*
    (43.700375, -79.513791), # Weston station
    (43.657096, -79.450198), # Bloor station
    (43.636916, -79.535974), # Kipling station*
    (43.617095, -79.496395), # Mimico station
    (43.635855, -79.419000), # Exhibition station
    (43.754630, -79.199181), # Guildwood station
    (43.739814, -79.231723), # Eglinton station
    (43.716781, -79.255050), # Scarborough station
    (43.686524, -79.299930), # Danforth station
    # (43.591552, -79.546146), # Long Branch station
    # (43.706416, -79.562962), # Etobicoke North station
    # (43.780231, -79.131090), # Rouge Hill station
]
# The last three stations are within city limits but not within the bounds of our heatmap

TTC_SUBWAY_STATIONS = [
    (43.636916, -79.535974), # Kipling station*
    (43.645342, -79.521779), # Islington station
    (43.647918, -79.514032), # Royal York station
    (43.649688, -79.499134), # Old Mill station
    (43.649195, -79.487987), # Jane station
    (43.653357, -79.470500), # High Park station
    (43.654894, -79.464578), # Keele station
    (43.656757, -79.455259), # Dundas West station
    (43.659527, -79.446380), # Lansdow station
    (43.660150, -79.439274), # Dufferin station
    (43.662288, -79.428861), # Ossington station
    (43.663443, -79.421976), # Christie station
    (43.665646, -79.413791), # Bathurst station
    (43.667562, -79.406463), # Spadina station
    (43.667793, -79.402292), # St George station
    (43.669663, -79.392221), # Bay station
    (43.670956, -79.387595), # Bloor-Yonge station
    (43.672399, -79.376302), # Sherbourne station
    (43.673651, -79.368485), # Castle Frank station
    (43.676150, -79.361141), # Broadview station
    (43.677414, -79.355024), # Chester station
    (43.679241, -79.347511), # Pape station
    (43.680185, -79.341442), # Donlands station
    (43.682190, -79.332879), # Greenwood station
    (43.685119, -79.326253), # Coxwell station
    (43.686638, -79.312690), # Woodbine station
    (43.692227, -79.300543), # Main Street station
    (43.695391, -79.292660), # Victoria Park station
    (43.710067, -79.280746), # Warden station
    (43.732648, -79.265035), # Kennedy station*
    (43.775293, -79.347201), # Don Mills station
    (43.770852, -79.368780), # Leslie station
    (43.769018, -79.376824), # Bessarion station
    (43.768273, -79.384641), # Bayview station
    (43.779673, -79.415666), # Finch station
    (43.768483, -79.412805), # North York Centre station
    (43.761410, -79.411894), # Sheppard-Yonge street
    (43.745126, -79.406727), # York-Mills street
    (43.724695, -79.404459), # Lawrence station
    (43.705175, -79.398802), # Eglinton station
    (43.699146, -79.398336), # Davisville station
    (43.686173, -79.395186), # St Clair station
    (43.679783, -79.392128), # Summerhill station
    (43.674871, -79.390686), # Rosedale station
    (43.663938, -79.385612), # Wellesley station
    (43.659833, -79.383985), # College station
    (43.656448, -79.382000), # Dundas station
    (43.653582, -79.382181), # Queen station
    (43.649217, -79.380537), # King station
    (43.645869, -79.381207), # Union station*
    (43.647219, -79.385262), # St Andrew station
    (43.650337, -79.387388), # Osgoode station
    (43.654325, -79.388759), # St Patrick station
    (43.659229, -79.390944), # Queen's Park station
    (43.666179, -79.393723), # Museum station
    (43.674219, -79.407522), # Dupont station
    (43.683437, -79.416782), # St Clair West station
    (43.699285, -79.436715), # Eglinton West station
    (43.706801, -79.438041), # Glencarin station
    (43.712509, -79.443964), # Lawrence West station
    (43.723023, -79.450968), # Yorkdale station
    (43.731907, -79.453731), # Wilson station
    (43.750725, -79.467873), # Sheppard West station
    (43.753787, -79.479018), # Downsview Park station*
    (43.762847, -79.493907), # Finch West station
    (43.773145, -79.501732), # York University station
    (43.776414, -79.509948), # Pioneer Village station
    (43.783072, -79.523471), # Highway 407 station
    (43.792479, -79.528968), # Vaughan station
]
