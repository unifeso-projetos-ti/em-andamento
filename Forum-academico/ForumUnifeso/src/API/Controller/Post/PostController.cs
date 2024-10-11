using ForumUnifeso.src.API.Interface;
using Microsoft.AspNetCore.Mvc;
using ForumUnifeso.src.API.Model;
using ForumUnifeso.src.API.View;
using AutoMapper;
using Microsoft.AspNetCore.Authorization;

namespace ForumUnifeso.src.API.Controller
{
    [Authorize]
    [ApiController]
    [Route("api/[controller]")]
    public class PostController : ControllerBase
    {
        private readonly IPostService _postService;
        private readonly IMapper _mapper;

        public PostController(IPostService postService, IMapper mapper)
        {
            _postService = postService;
            _mapper = mapper;
        }

        [HttpPost]
        public async Task<IActionResult> CreatePostAsync([FromBody] PostRequest postRequest)
        {
            if (postRequest is null)
            {
                return BadRequest("Post data is null.");
            }

            try
            {
                Post post = _mapper.Map<Post>(postRequest);

                await _postService.AddAsync(post);

                PostResponse response = _mapper.Map<PostResponse>(post);
                return CreatedAtAction(nameof(GetPostById), new { id = post.Id }, response);
            }
            catch (AutoMapperMappingException ex)
            {
                return StatusCode(500, "Mapping configuration issue.");
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetPostById(int id)
        {
            try
            {
                var post = await _postService.GetByIdAsync(id);
                if (post == null)
                {
                    return NotFound();
                }

                PostResponse response = _mapper.Map<PostResponse>(post);

                return Ok(response);
            }
            catch (AutoMapperMappingException ex)
            {
                return StatusCode(500, "Mapping configuration issue.");
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);

            }
        }

        [HttpGet]
        public async Task<IActionResult> GetAllPost()
        {

            try
            {
                IEnumerable<Post> post = await _postService.GetAllAsync();

                IEnumerable<PostResponse> response = _mapper.Map<IEnumerable<PostResponse>>(post);

                return Ok(response);
            }
            catch (AutoMapperMappingException ex)
            {
                return StatusCode(500, "Mapping configuration issue.");
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);

            }
        }

        [HttpPut]
        public async Task<IActionResult> UpdatePostAsync([FromBody] PostRequest postRequest)
        {
            if (postRequest is null)
            {
                return BadRequest("Post data is null.");
            }

            try
            {
                Post post = _mapper.Map<Post>(postRequest);

                await _postService.UpdateAsync(post);

                PostResponse response = _mapper.Map<PostResponse>(post);
                return Ok(response);
            }
            catch (AutoMapperMappingException ex)
            {
                return StatusCode(500, "Mapping configuration issue.");
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);

            }
        }

        [HttpDelete]
        public async Task<IActionResult> DeletePostAsync([FromBody] PostRequest postRequest)
        {
            if (postRequest is null)
            {
                return BadRequest("Post data is null.");
            }

            try
            {
                Post post = _mapper.Map<Post>(postRequest);

                await _postService.DeleteAsync(post);

                PostResponse response = _mapper.Map<PostResponse>(post);
                return NoContent();
            }
            catch (AutoMapperMappingException ex)
            {
                return StatusCode(500, "Mapping configuration issue.");
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);

            }
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeletePostByIdAsync(int id)
        {
            if (await _postService.GetByIdAsync(id) is null)
            {
                return BadRequest("Post data is null.");
            }

            try
            {

                await _postService.DeleteByIdAsync(id);

                return NoContent();
            }
            catch (AutoMapperMappingException ex)
            {
                return StatusCode(500, "Mapping configuration issue.");
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);

            }
        }
    }
}
