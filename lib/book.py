#!/usr/bin/env python3

class Book:
    # Define a class called Book
    # Define a method called __init__ that initializes title and page_count
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    # Define a method called get_page_count that returns the value of the page_count
    def get_page_count(self):
        try:
            return self._page_count
        except:
            return
    #  Define a method called set_page_count that sets the value of the page_count
    def set_page_count(self, page_count):
        if (type(page_count) == int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    page_count = property(get_page_count, set_page_count)

    # def page_count(self):
    #     if not isinstance(self.page_count, int):
    #         print("Page_count must be an integer")

    # def turn_page(self):
    #     print("Flipping the page... wow, you read fast!")
    pass
    
        
    
        