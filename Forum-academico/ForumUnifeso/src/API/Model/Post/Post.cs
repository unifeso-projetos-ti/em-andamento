namespace ForumUnifeso.src.API.Model
{
    public class Post
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public DateTime Date{ get; set; }

        public Person Author { get; set; }
        public int AuthorId { get; set; }


        public int? ThreadForumId { get; set; }
        public ThreadForum ThreadForum { get; set; }

        public Post() {}
        public Post(int id, string title, string description, DateTime date, Person author) 
        {
            Id = id;
            Title = title;
            Description = description;
            Date = date;
            Author = author;
        }
    }
}
