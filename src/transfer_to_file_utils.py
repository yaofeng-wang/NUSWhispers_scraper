import xlsxwriter

class TransferToFileUtils():
    """
    Component used to save scraped data into a file

    Methods
    -------
    append_to_text_file()
        Appends data into a text file

    create_empty_text_file()
        Creates an empty text file

    write_to_empty_xlsx_file()
        Creates a new xlsx file and transfer all the scrapped_data into it

    """

    def append_to_text_file(self, text, file_name='output'):
        """
        Appends text to file
        
        Parameters
        ----------
        text : str
            The content that will be appended into file

        file_name : str
            The name of the file which will be used (without extension)
            (default : 'output')

        """
        with open(file_name + '.txt', 'a', encoding='utf-8') as f:
            f.write(str(text))
            f.close()

    def create_empty_text_file(self, file_name='output'):
        """
        Creates an empty file

        Parameters
        ----------
        file_name : str
            The name of the file which will be used (without extension)
            (default : 'output')

        """
        open(file_name + '.txt', 'w+', encoding='utf-8').close()

    def write_to_empty_xlsx_file(self, post_contents, file_name='output'):
        """
        Creates a new xlsx file and transfer the scraped data into the file
        
        Parameters
        ----------
        post_contents : dictionary
            A dictionary where the key is the post index and the value is
            the post content

        file_name : str
            The name of the file which will be used (without extension)
            (default : 'output')

        """
        workbook = xlsxwriter.Workbook(file_name + '.xlsx')
        worksheet = workbook.add_worksheet()
        for idx, post_content in enumerate(post_contents.items()):
            post_idx, content = post_content
            categories, text, num_likes, num_comments, age, num_favs \
                    = content
            worksheet.write(idx, 0, post_idx)
            worksheet.write(idx, 1, categories)
            worksheet.write(idx, 2, text)
            worksheet.write(idx, 3, num_likes)
            worksheet.write(idx, 4, num_comments)
            worksheet.write(idx, 5, age)
            worksheet.write(idx, 6, num_favs)
        workbook.close()


