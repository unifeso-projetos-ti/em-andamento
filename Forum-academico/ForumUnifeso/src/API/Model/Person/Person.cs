namespace ForumUnifeso.src.API.Model
{
    public class Person
    {
        public int Id { get; set; }
        public string Name { get; set; }

        public List<Post> Posts { get; set; } = new List<Post>();
        
        public Person(int id, string name) {
            Id = id;
            Name = name;
        }

        public Person() {}
    }
}
