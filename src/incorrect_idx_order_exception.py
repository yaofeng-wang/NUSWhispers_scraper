
class IncorrectIdxOrderException(Exception):
    """
    Exception raised when the start_idx is larger than end_idx
    
    Attributes
    ----------
    start_idx : int
        index of the first post to be scraped
    end_idx : int
        index of the last post to be scraped
    
    """
    def __init__(self, start_idx, end_idx):
        self.message = 'start_idx, of {}, is larger than end_idx, of {}'.format(start_idx, end_idx)
    

