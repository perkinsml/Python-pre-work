
class Genre(object):

    def __init__(self, name, num_members, num_albums, num_records_sold, genre):
        self.name = name
        self.num_members = num_members
        self.num_albums = num_albums
        self.num_records_sold = num_records_sold
        self.genre = genre

    def print_stats(self):
        print(f"Band: {self.name}, Members: {self.num_members}, Albums: {self.num_albums}, Sold: {self.num_records_sold}, Genre: {self.genre}")
        # print "Band: %s, Members: %d, Albums: %d, Sold: %d, Genre: %s" % (self.name, self.num_members, self.num_albums, self.num_records_sold, self.genre)
queen = Genre('Queen', 4, 15, 105000000, 'Rock')
queen.print_stats()
