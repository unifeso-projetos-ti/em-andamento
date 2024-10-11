using ForumUnifeso.src.API.Model;
using System.ComponentModel.DataAnnotations;

namespace ForumUnifeso.src.API.View
{
    public class PostResponse
    {
        public string Title { get; set; }
       
        public string Description { get; set; }
        public DateTime Date { get; set; }

        public PersonResponse Author { get; set; }
    }
}
