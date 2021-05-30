class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    self.__collection=collection
    self.__items=items_per_page
      
  
  # returns the number of items within the entire collection
  def item_count(self):
    return len(self.__collection)
      
  
  # returns the number of pages
  def page_count(self):
    if self.item_count()%self.__items>0:
        adding=1
    else:
        adding=0
    return self.item_count()//self.__items+adding
      
    
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
    if page_index<0:
        return -1
    elif page_index<self.page_count()-1:
        return self.__items
    elif page_index==self.page_count()-1:
        return self.item_count()-page_index*self.__items
    else:
        return -1
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
        if item_index+1%self.__items>0:
            adding=1
        else:
            adding=0
        if item_index<0:
            return -1
        elif item_index<self.item_count():
            return (item_index+1)//self.__items+adding-1
        else:
            return -1