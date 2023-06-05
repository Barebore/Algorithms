class Track:
    def __init__(self, start_x=0, start_y=0):
        self.tr = []
        self.start_x = start_x
        self.start_y = start_y

    def add_track(self,tr):
        self.tr.append(tr)

    def get_tracks(self):   
        return tuple(self.tr)
    
    def __len__(self):
        total_length_track = 0
        start_coords = [self.start_x, self.start_y]
        for point in self.tr:
            total_length_track += ((point.to_x - start_coords[0])**2 + (point.to_y - start_coords[1])**2)**0.5
            start_coords = [point.to_x, point.to_y]

        return int(total_length_track)
    
    def __eq__(self, other):
        return len(self) == len(other)
    
    def __lt__(self, other):
        return len(self) < len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2