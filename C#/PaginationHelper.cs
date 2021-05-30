using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp6
{
    public class PagnationHelper<T>
    {
        public PagnationHelper(IList<T> collection, int itemsPerPage)
        {
            this.ItemsPerPage = itemsPerPage;
            this.ItemCount = collection.Count;
            Boolean even = this.ItemCount % this.ItemsPerPage == 0;
            this.PageCount = collection.Count / ItemsPerPage + (even ? 0 : 1);
        }


        private int itemsPerPage;
        private int itemCount;
        private int pageCount;


        public int ItemCount { get => itemCount; set => itemCount = value; }
        public int PageCount { get => pageCount; set => pageCount = value; }
        public int ItemsPerPage { get => itemsPerPage; set => itemsPerPage = value; }

        public int PageItemCount(int pageIndex)
        {
            Boolean even = this.ItemCount % this.ItemsPerPage == 0;
            //int totalPages = this.ItemCount / this.ItemsPerPage+(even?0:1);
            if (pageIndex + 1 > this.PageCount | pageIndex < 0)
            {
                return -1;
            }
            else if (pageIndex + 1 == this.PageCount & !even)
            {
                return this.ItemCount % this.ItemsPerPage;
            }
            else
            {
                return this.ItemsPerPage;
            }
        }

        public int PageIndex(int itemIndex)
        {

            Boolean even = this.ItemCount % this.ItemsPerPage == 0;
            if (itemIndex < 0 | itemIndex + 1 > this.ItemCount)
            {
                return -1;
            }
            else if (itemIndex + 1 > this.ItemsPerPage)
            {
                return (itemIndex + 1) / this.ItemsPerPage +
                    ((itemIndex + 1) % this.ItemsPerPage == 0 ? 0 : 1) - 1;
            }
            else
            {
                return 0;
            }
        }
    }
}
