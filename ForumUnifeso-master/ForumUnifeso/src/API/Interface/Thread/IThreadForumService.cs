namespace ForumUnifeso.src.API.Interface
{
    using ForumUnifeso.src.API.Base;
    using ForumUnifeso.src.API.Model;

    public interface IThreadForumService : IService<ThreadForum, int>
    {
        Task<IEnumerable<ThreadForum>> GetByTitleAsync(string threadForumTitle);

        Task<bool> DeleteByIdAsync(int id);
    }
}
