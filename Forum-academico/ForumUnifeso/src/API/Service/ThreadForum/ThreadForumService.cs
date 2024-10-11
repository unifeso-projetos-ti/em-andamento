using AutoMapper;
using ForumUnifeso.src.API.Base;
using ForumUnifeso.src.API.Interface;
using ForumUnifeso.src.API.Model;
using ForumUnifeso.src.API.View;

namespace ForumUnifeso.src.API.Service
{
    public class ThreadForumService : IThreadForumService
    {
        private readonly IThreadForumRepository _threadForumRepository;        

        public ThreadForumService(IThreadForumRepository threadForumRepository) {
            _threadForumRepository = threadForumRepository;
        }

        public async Task<ThreadForum> AddAsync(ThreadForum threadForum)
        {
            return await _threadForumRepository.AddAsync(threadForum);
        }

        public Task<bool> DeleteAsync(ThreadForum threadForum)
        {
            return _threadForumRepository.DeleteAsync(threadForum);
        }

        public Task<bool> DeleteByIdAsync(int threadForumId)
        {
            return _threadForumRepository.DeleteByIdAsync(threadForumId);
        }

        public async Task<IEnumerable<ThreadForum>> GetAllAsync()
        {
            return await _threadForumRepository.GetAllAsync();
        }

        public async Task<ThreadForum?> GetByIdAsync(int threadForumId)
        {
            return await _threadForumRepository.GetByIdAsync(threadForumId);
        }

        public async Task<IEnumerable<ThreadForum>> GetByTitleAsync(string threadForumTitle)
        {
            return await _threadForumRepository.GetByTitleAsync(threadForumTitle);
        }

        public async Task<ThreadForum> UpdateAsync(ThreadForum threadForum)
        {
            return await _threadForumRepository.UpdateAsync(threadForum);
        }
    }
}