using ForumUnifeso.src.API.Base;
using ForumUnifeso.src.API.Base.Context;
using ForumUnifeso.src.API.Interface;
using ForumUnifeso.src.API.Model;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Hosting;

namespace ForumUnifeso.src.API.Repository
{
    public class PostRepository : IPostRepository
    {
        private readonly PrincipalDbContext _context;

        public PostRepository(PrincipalDbContext context)
        {
            _context = context;
        }

        public async Task<Post> AddAsync(Post post)
        {
            _context.Post.Add(post);
            await _context.SaveChangesAsync();
            return post;
        }

        public async Task<Post> UpdateAsync(Post post)
        {
            _context.Post.Update(post);
            await _context.SaveChangesAsync();
            return post;
        }

        public async Task<Post?> GetByIdAsync(int postId)
        {
            return await _context.Post.FirstOrDefaultAsync(post => post.Id == postId);
        }

        public async Task<IEnumerable<Post>> GetAllAsync()
        {
            return await _context.Post.ToListAsync();
        }

        public async Task<bool> DeleteByIdAsync(int id)
        {
            var post = await GetByIdAsync(id);
            if (post is not null)
            {
                _context.Post.Remove(post);
                await _context.SaveChangesAsync();
                return true;
            }
            else
            {
                return false;
            }
        }

        public async Task<bool> DeleteAsync(Post post)
        {
            _context.Post.Remove(post);
            await _context.SaveChangesAsync();
            return true;
        }
    }
}
