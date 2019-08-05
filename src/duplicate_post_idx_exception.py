class DuplicatePostIdxException(Exception):
    """
    Raised when a post index already exists in post_content dictionary
    """
    def __init(self, message, errors=None):
        super().__init__(message)
        self.errors = errors

