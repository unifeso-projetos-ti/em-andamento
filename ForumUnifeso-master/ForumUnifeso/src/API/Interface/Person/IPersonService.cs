using ForumUnifeso.src.API.Base;
using ForumUnifeso.src.API.Model;

namespace ForumUnifeso.src.API.Interface
{
  
    public interface IPersonService : IService<Post, int>
    {
        Task<bool> DeleteByIdAsync(int id);
    }
}
