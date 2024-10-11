namespace ForumUnifeso.src.API.Model
{

    public class ThreadForum
    {
        public int? Id { get; set; }
        
        public Post? Topic { get; set; }

        public int TopicId { get; set; }

      
        public List<Post> Answers { get; set; } = new List<Post>();

        public ThreadForum() {}

        public ThreadForum(int id, Post topic)
        {
            Id = id;
            Topic = topic;
        }
    }
}
