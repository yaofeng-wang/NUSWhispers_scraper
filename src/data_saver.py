import xlsxwriter

class DataSaver():
    """
    Component used to save scraped data into a file

    Attributes
    ----------
    file_name : str
        The name of the file, without the name, which will be used
        (default 'output')

    Methods
    -------
    append_to_text_file()
        Appends data into a text file

    create_empty_text_file()
        Creates an empty text file

    write_to_empty_xlsx_file()
        Creates a new xlsx file and transfer all the scrapped_data into it

    """
    def __init__(self, file_name='output'):
        """
        Parameters
        ----------
        file_name : str
            The name of the file which will be used (without extension)
        
        """
        self.file_name = file_name

    def append_to_text_file(self, text):
        """
        Appends text to file
        
        Parameters:
        text : str
            The content that will be appended into file

        """
        with open(self.file_name + '.txt', 'a', encoding='utf-8') as f:
            f.write(str(text))
            f.close()

    def create_empty_text_file(self):
        """
        Creates an empty file

        """
        open(self.file_name + '.txt', 'w+', encoding='utf-8').close()

    def write_to_empty_xlsx_file(self, post_content):
        """
        Creates a new xlsx file and transfer the scraped data into the file

        """
        workbook = xlsxwriter.Workbook(self.file_name + '.xlsx')
        worksheet = workbook.add_worksheet()
        for idx, post in enumerate(post_content.items()):
            post_idx, contents = post
            post_text, num_likes, num_comments, post_age = contents
            worksheet.write(idx, 0, post_idx)
            worksheet.write(idx, 1, post_text)
            worksheet.write(idx, 2, num_likes)
            worksheet.write(idx, 3, num_comments)
            worksheet.write(idx, 4, post_age)
        workbook.close()


