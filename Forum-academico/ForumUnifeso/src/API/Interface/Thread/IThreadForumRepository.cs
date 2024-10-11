using ForumUnifeso.src.API.Base;
using ForumUnifeso.src.API.Model;

namespace ForumUnifeso.src.API.Interface
{
    public interface IThreadForumRepository : IRepository<ThreadForum, int>
    {
        Task<IEnumerable<ThreadForum>> GetByTitleAsync(string threadForumTitle);

        Task<bool> DeleteByIdAsync(int id);
    }
}
