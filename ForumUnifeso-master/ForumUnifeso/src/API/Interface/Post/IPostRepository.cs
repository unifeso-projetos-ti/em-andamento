using ForumUnifeso.src.API.Base;
using ForumUnifeso.src.API.Model;

namespace ForumUnifeso.src.API.Interface
{
    public interface IPostRepository : IRepository<Post, int>
    {
        Task<bool> DeleteByIdAsync(int id);

    }
}
