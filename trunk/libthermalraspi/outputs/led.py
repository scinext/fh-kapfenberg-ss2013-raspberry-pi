class Led(object):
    def go_to_rgb(self, rgb):
        assert False, 'abstract'
    def get_current_rgb(self):
        assert False, 'abstract'
        return [0,0,0]
    pass
