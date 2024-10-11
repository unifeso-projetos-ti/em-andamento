using ForumUnifeso.src.API.View;
using ForumUnifeso.src.API.Interface;
using ForumUnifeso.src.API.Model;
using Microsoft.AspNetCore.Mvc;
using AutoMapper;
using Microsoft.AspNetCore.Authorization;

namespace ForumUnifeso.src.API.Controller.ThreadForumController
{
    [Authorize]
    [ApiController]
    [Route("api/[controller]")]
    public class ThreadForumController : ControllerBase {

        private IThreadForumService _threadForumService;

        private readonly IMapper _mapper;

        public ThreadForumController(IThreadForumService threadForumService, IMapper mapper)
        {
            _threadForumService = threadForumService;
            _mapper = mapper;
        }

        [HttpPost("/add")]
        public async Task<IActionResult> PostThreadForum([FromBody] ThreadForumRequest threadForumRequest)
        {
            try 
            {
                if (threadForumRequest is null) {
                    return BadRequest("Valor de 'Thread' é nulo");
                }

                ThreadForum threadForum = _mapper.Map<ThreadForum>(threadForumRequest);
                ThreadForum threadForumSaved = await _threadForumService.AddAsync(threadForum);

                return Created("GetThreadForum", _mapper.Map<ThreadForumResponse>(threadForumSaved));
            } catch (Exception ex) {
                return StatusCode(500, ex.Message);
            }

        }

        [HttpGet("/all")]
        public async Task<ActionResult<IEnumerable<ThreadForumSimpleResponse>>> GetAllThreadForum() 
        {
            try
            {
                var threadsForum = await _threadForumService.GetAllAsync();
                return Ok(_mapper.Map<IEnumerable<ThreadForumSimpleResponse>>(threadsForum));
            }
            catch (Exception ex) {
                return StatusCode(500, ex.Message);
            }
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<ThreadForumResponse>> GetThreadForumById(int id)
        {
            try
            {
                var threadForum = await _threadForumService.GetByIdAsync(id);
                if (threadForum == null) {
                    return NotFound();
                }
                return Ok(_mapper.Map<ThreadForumResponse>(threadForum));
            }
            catch (Exception ex) {
                return StatusCode(500, ex.Message);
            }
        }

        [HttpGet("title/{title}")]
        public async Task<ActionResult<IEnumerable<ThreadForumSimpleResponse>>> GetThreadForumByTitle(string title)
        {
            try
            {
                var threadsForum = await _threadForumService.GetByTitleAsync(title);
                return Ok(_mapper.Map<IEnumerable<ThreadForumSimpleResponse>>(threadsForum));
            }
            catch (Exception ex) {
                return StatusCode(500, ex.Message);
            }
        }

        [HttpPut("/edit/{id}")]
        public async Task<ActionResult<ThreadForumResponse>> PutThreadForum(int id, ThreadForumRequest threadForumRequest)
        {
            try
            {   
                ThreadForum threadForum = _mapper.Map<ThreadForum>(threadForumRequest);
                threadForum.Id = id;
                var threadForumUpdated = await _threadForumService.UpdateAsync(threadForum);
                return Ok(_mapper.Map<ThreadForumResponse>(threadForumUpdated));
            }
            catch (Exception ex) {
                return StatusCode(500, ex.Message);
            }
        }

        [HttpDelete("/remove/{id}")]
        public async Task<ActionResult<bool>> DeleteThreadForumById(int id)
        {
            try
            {                       
                var threadForumDeleted = await _threadForumService.DeleteByIdAsync(id);
                return Ok(threadForumDeleted);
            }
            catch (Exception ex) {
                return StatusCode(500, ex.Message);
            }
        }
    } 
}