class Bangladesh(object):
    leftLonBound = 88
    rightLonBound = 93
    upperLatBound = 20.5
    lowerLatBound = 27

    @staticmethod
    def lonWithinCountry(longitude):
        higherthanleftbound = longitude > 88
        lowerthanrightbound = longitude < 93
        withinlon = higherthanleftbound and lowerthanrightbound
        return withinlon
    @staticmethod
    def latWithinCountry(latitude):
        higherthanlowerbound = latitude > 20.5
        lowerthanupperbound = latitude < 27
        withinlat = higherthanlowerbound and lowerthanupperbound
        return withinlat
