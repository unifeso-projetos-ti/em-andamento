using ForumUnifeso.src.API.Model;
using System.ComponentModel.DataAnnotations;

namespace ForumUnifeso.src.API.View
{
    public class PostRequest
    {
        public string Title { get;  set; }
       
        public string Description { get;  set; }
        public DateTime Date { get;  set; }

        public PersonRequest Author { get;  set; }

        public int ThreadForumId { get; set; }
    }
}
