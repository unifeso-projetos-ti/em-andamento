namespace ForumUnifeso.src.API.Interface
{
    using ForumUnifeso.src.API.Base;
    using ForumUnifeso.src.API.Model;
    public interface IPostService : IService<Post, int>
    {
        Task<bool> DeleteByIdAsync(int id);
    }
}
