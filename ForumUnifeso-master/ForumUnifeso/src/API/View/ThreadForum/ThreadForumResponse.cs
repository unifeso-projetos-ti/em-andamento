namespace ForumUnifeso.src.API.View
{
    public class ThreadForumResponse {
        public int? Id { get; set; }
        public PostResponse? Topic { get;  set; }
        public List<PostResponse> Answers { get; set; } = new List<PostResponse>();
    }
}